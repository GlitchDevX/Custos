from .models.flagged_content import FlaggedContent
from .models.reported_content import ReportedContent
from .llm.prompt_builder import PromptBuilder
from .llm.llm_adapter import LlmAdapter
from .llm.schemas import ReportAnalysis, report_analysis_schema

from .database_connector import DatabaseConnector

class Pipeline:
    
    def __init__(self):
        self.db = DatabaseConnector()
        self.llm = LlmAdapter("http://localhost:11434/api/generate", format=report_analysis_schema)
        self.prompt_builder = PromptBuilder()

    running = False
    total_reports = 0
    processed_reports = 0

    def get_status(self):
        return {
            "active": self.running,
            "total": self.total_reports,
            "processed": self.processed_reports,
            "ratio": 0 if self.total_reports == 0 else self.processed_reports / self.total_reports
        }

    def run(self):
        all_reports = self.db.get_all_reported_content()
        
        self.running = True
        self.total_reports = len(all_reports)
        self.processed_reports = 0

        results = list(map(self.process_content, all_reports))

        self.db.write_results(results)
        
        report_ids = list(map(lambda r: r.report_id, all_reports))
        self.db.remove_reports(report_ids)

        self.running = False

    def process_content(self, report: ReportedContent):
        message = report.content
        prompt = self.prompt_builder.build_prompt(message)

        print(f"Message: {message}")
        response: ReportAnalysis = self.llm.prompt_llm(prompt)
        
        valid_flags = ["SPAM, PROFANITY, HARASSMENT, MISINFORMATION, OTHER"]
        flags = ",".join(filter(lambda f: f in valid_flags, response["tags"]))
        
        print(f"Response: {response}\n")

        result = FlaggedContent()
        for (key, value) in filter(lambda i: not i[0].startswith('_'), report.__dict__.items()):
            result.__dict__[key] = value
        result.flags = flags
        result.false_report = flags == "" or flags == "OTHER"
        
        self.processed_reports += 1
        return result

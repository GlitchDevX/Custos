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

    def run(self):
        all_reports = self.db.get_all_reported_content()
        results = list(map(self.process_content, all_reports))

        self.db.write_results(results)

    def process_content(self, report: ReportedContent):
        message = report.content
        prompt = self.prompt_builder.build_prompt(message)

        print(f"Message: {message}")
        response: ReportAnalysis = self.llm.prompt_llm(prompt)
        flags_joined = ",".join(response["tags"])
        print(f"Response: {response}\n")

        result = FlaggedContent()
        for (key, value) in filter(lambda i: not i[0].startswith('_'), report.__dict__.items()):
            result.__dict__[key] = value
        result.flags = flags_joined

        return result

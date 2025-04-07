from .llm.prompt_builder import PromptBuilder
from .llm.llm_adapter import LlmAdapter
from .llm.schemas import report_analysis_schema

from .database_connector import DatabaseConnector


class Pipeline:
    
    def __init__(self):
        self.db = DatabaseConnector()
        self.llm = LlmAdapter("http://localhost:11434/api/generate", format=report_analysis_schema)
        self.prompt_builder = PromptBuilder()

    def run(self):
        all_reports = self.db.get_all_reported_content()
        result = list(map(self.process_report, all_reports))

        print(result)

    def process_report(self, report):
        message = report["content"]
        prompt = self.prompt_builder.build_prompt(message)

        print(f"Message: {message}")
        response = self.llm.prompt_llm(prompt)

        return response

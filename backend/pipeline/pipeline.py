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
        data = self.db.get_all()
        # for row in data:
        #     print(row)

        message = "Ayo bro you're so ass in this game xD"
        prompt = self.prompt_builder.build_prompt(message)

        print(f"Message: {message}")
        print(self.llm.prompt_llm(prompt))

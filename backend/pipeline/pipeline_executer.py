# this file will manage which pipelines to run according to the config.
# this will be executed by a sheduled gh action workflow

from llm_adapter import LlmAdapter
from database_connector import DatabaseConnector


class PipelineExecuter:
    
    def __init__(self):
        self.db = DatabaseConnector()
        self.llm = LlmAdapter("http://localhost:11434/api/generate")

    def run(self):
        data = self.db.get_all()
        # for row in data:
        #     print(row)

        print(self.llm.prompt_llm("How many 'R' are in Banana?"))

        


PipelineExecuter().run()
import threading
from app.utils.singleton_meta import SingletonMeta
from pipeline.pipeline import Pipeline

class PipelineSubmitter(metaclass=SingletonMeta):

    def __init__(self):
        self.pipeline = Pipeline()

    def run_pipeline(self):
        if self.pipeline.running:
            return { "code": "ALREADY_RUNNING", "text": "The Pipeline is already running." }, 409
        
        threading.Thread(target=self.pipeline.run).start()
        return { "code": "OK" }


    def get_status(self):
        return self.pipeline.get_status(), 200
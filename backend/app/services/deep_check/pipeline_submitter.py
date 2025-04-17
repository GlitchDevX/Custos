import atexit
from threading import Thread
from app.models.reported_content import ReportedContent
from app.utils.singleton_meta import SingletonMeta
from pipeline.pipeline import Pipeline

from app.config_reader import ConfigReader
from app.utils.common_responses import ENDPOINT_DISABLED

from apscheduler.schedulers.background import BackgroundScheduler


class PipelineSubmitter(metaclass=SingletonMeta):

    def __init__(self):
        self.config = ConfigReader("pipeline", self.reschedule_pipeline)
        self.pipeline = Pipeline()

        self.scheduler = BackgroundScheduler()
        self.schedule_pipeline()
        atexit.register(lambda: self.scheduler.shutdown())

    def run_pipeline(self):
        if not self.config.get("enabled"):
            return ENDPOINT_DISABLED
        
        if self.pipeline.running:
            return { "code": "ALREADY_RUNNING", "text": "The Pipeline is already running." }, 409

        Thread(target=self.pipeline.run).start()

        return { "code": "OK" }

    def check_content_instant(self, content: str):
        if not self.config.get("enabled"):
            return ENDPOINT_DISABLED

        model = ReportedContent(content=content)
        result = self.pipeline.process_content(model)
        split_flags = list(filter(lambda f: f != "", result.flags.split(',')))
        return { "flags": split_flags, "falseReport": result.false_report }, 200

    def get_status(self):
        return self.pipeline.get_status(), 200

    def reschedule_pipeline(self):
        self.scheduler.shutdown()
        self.scheduler = BackgroundScheduler()
        self.schedule_pipeline()

    def schedule_pipeline(self):
        self.scheduler.add_job(self.run_pipeline, 'interval', minutes=2)
        self.scheduler.start()

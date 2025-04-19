import atexit
import traceback
from threading import Thread

from app.models.reported_content import ReportedContent
from app.utils.singleton_meta import SingletonMeta
from pipeline.pipeline import Pipeline

from app.config_reader import ConfigReader
from app.utils.common_responses import ENDPOINT_DISABLED

from app.utils.scheduler_wrapper import scheduler
from apscheduler.schedulers.background import BackgroundScheduler

class PipelineSubmitter(metaclass=SingletonMeta):

    scheduler: BackgroundScheduler = None

    def __init__(self):
        self.config = ConfigReader("pipeline", self.reschedule_pipeline)
        self.pipeline = Pipeline()

        self.reschedule_pipeline()

    def run_pipeline(self):
        print("Should be triggering pipeline")
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
        print("Rescheduling pipeline")
        print(scheduler.get_jobs())
        scheduler.remove_all_jobs()
        self.schedule_pipeline()
        print(scheduler.get_jobs())

    def schedule_pipeline(self):
        if not self.config.get("scheduledExecution"):
            return

        interval_hours = self.config.get("executionIntervalHours")
        self.scheduler.add_job(self.run_pipeline, 'interval', minutes=interval_hours)
        self.scheduler.start()
        print("Scheduled pipeline")

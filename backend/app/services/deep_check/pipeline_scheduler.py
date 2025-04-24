import atexit

from app.config_reader import ConfigReader
from app.services.deep_check.pipeline_submitter import PipelineSubmitter

from apscheduler.schedulers.background import BackgroundScheduler


class PipelineScheduler:
    def __init__(self):
        self.scheduler = BackgroundScheduler(daemon=True)
        self.pipeline_submitter = PipelineSubmitter()
        self.config = ConfigReader("pipeline", self.reschedule_pipeline)

        self.schedule_pipeline()
        atexit.register(self.scheduler.shutdown)

    def reschedule_pipeline(self):
        self.scheduler.remove_all_jobs()
        self.schedule_pipeline()

    def schedule_pipeline(self):
        interval_hours = self.config.get("executionIntervalHours")
        self.scheduler.add_job(self.pipeline_submitter.run_pipeline, "interval", hours=interval_hours)
        self.scheduler.start()

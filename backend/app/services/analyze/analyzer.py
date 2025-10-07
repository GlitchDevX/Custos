from threading import Thread
from app.utils.logger import logger
from app.utils.singleton_meta import SingletonMeta
from app.services.metrics.metrics_counter import count_metric
from detoxify import Detoxify

from app.config_reader import ConfigReader
from app.utils.common_responses import ENDPOINT_DISABLED


class AnalyzerService(metaclass=SingletonMeta):
    """
    A service class for analyzing and labeling user content using
    the detoxify neuronal network.
    """

    config = ConfigReader("deep_analysis")
    loading_thread: Thread
    model: Detoxify | None = None

    def __init__(self):
        self.loading_thread = Thread(target=self._load_model)
        self.loading_thread.start()

    def _load_model(self): 
        try:
            self.model = Detoxify("multilingual")
            logger.info("Detoxify model loaded")
        except Exception as err:
            logger.warning(f"Could not get detoxify model. Error: {err}")

    def analyze_content(self, content: str):
        if not self.config.get("enabled"):
            return ENDPOINT_DISABLED
        
        if self.model is None:
            if self.loading_thread.is_alive():
                logger.warning("Could not analyze content, still waiting to load detoxify model")
                return {'code': "MODEL_TEMPORARY_UNAVAILABLE", 'text': "The detoxify model is still loading, please try again in a minute."}, 503
            else:
                logger.error("Could not analyze content, detoxify model is missing")
                return {'code': "MODEL_UNAVAILABLE", 'text': "The detoxify model is missing."}, 503

        count_metric('ANALYZER_EXECUTED')

        result = self.model.predict(content)
        excluded = self.config.get("labelsToExclude")
        threshold = self.config.get("threshold")

        labels = []
        for key, value in result.items():
            if key not in excluded and value > threshold:
                labels.append(key)

        if len(labels) > 0:
            count_metric('ANALYZER_TOXICITY_DETECTED')

        return {"labels": labels}

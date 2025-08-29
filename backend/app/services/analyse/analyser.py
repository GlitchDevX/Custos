from detoxify import Detoxify

from app.config_reader import ConfigReader
from app.models.metric import Metric
from app.utils.common_responses import ENDPOINT_DISABLED


class AnalyserService:
    """
    A service class for analyzing and labeling user content using
    the detoxify neuronal network.
    """

    config = ConfigReader("analyse")

    def __init__(self):
        if self.config.get("enabled"):
            self.model = Detoxify("multilingual")

    def analyse_content(self, content: str):
        if not self.config.get("enabled"):
            return ENDPOINT_DISABLED

        Metric.increase("ANALYZER_EXECUTED")

        result = self.model.predict(content)
        excluded = self.config.get("labelsToExclude")
        threshold = self.config.get("threshold")

        labels = []
        for key, value in result.items():
            if key not in excluded and value > threshold:
                labels.append(key)

        if len(labels) > 0:
            Metric.increase("ANALYZER_TOXICITY_DETECTED")

        return {"labels": labels}

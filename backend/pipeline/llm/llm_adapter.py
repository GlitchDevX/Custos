import json
import requests

from app.config import app_config

class LlmAdapter:

    def __init__(self, model="gemma3:4b", format="json"):
        self.url = app_config.config.LLM_URI + "/api/generate"
        self.model = model
        self.format = format

    def prompt_llm(self, prompt: str):
        body = {
          "model": self.model,
          "prompt": prompt,
          "stream": False,
          "format": self.format
        }
        headers={"Content-Type":"text"}
    
        response = requests.post(self.url, json=body, headers=headers, stream=True)
        response.raise_for_status()

        # make this a metric like avg_response_time
        print(response.elapsed)

        return json.loads(response.json()["response"])
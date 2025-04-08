import json
import requests

class LlmAdapter:

    def __init__(self, url="http://olama:11434/api/generate", model="gemma3:4b", format="json"):
        self.url = url
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
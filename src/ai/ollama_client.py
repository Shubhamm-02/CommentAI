import ollama
from loguru import logger
from src.config.settings import settings

class OllamaClient:
    def __init__(self):
        self.host = settings.OLLAMA_HOST
        self.model = settings.MODEL_NAME
        # Initialize client pointed at local host
        self.client = ollama.Client(host=self.host)
        
    def generate_response(self, system_prompt: str, user_prompt: str) -> str:
        """
        Sends the prompt to the local Ollama instance and returns the generated text.
        """
        try:
            response = self.client.chat(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ]
            )
            return response['message']['content'].strip()
        except Exception as e:
            logger.error(f"Failed to generate response from Ollama: {e}")
            return ""

from mistralai import Mistral
import google.generativeai as genai
from config import mistral_api_key, gemini_api_key

class APIClient:
    def __init__(self, mistral_api_key: str, gemini_api_key: str):
        self.mistral_client = Mistral(api_key=mistral_api_key)
        genai.configure(api_key=gemini_api_key)
        self.gemini_generation_config = {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 40,
            "max_output_tokens": 16192,
            "response_mime_type": "text/plain",
        }
        self.gemini_model = genai.GenerativeModel(
            model_name="gemini-2.0-flash-exp",
            generation_config=self.gemini_generation_config,
        )

api_client = APIClient(mistral_api_key, gemini_api_key)

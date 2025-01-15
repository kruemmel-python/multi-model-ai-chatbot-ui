from mistralai import Mistral
import google.generativeai as genai
from config import mistral_api_key, gemini_api_key
import logging

logger = logging.getLogger(__name__)

class APIClient:
    """
    Klasse zur Verwaltung der API-Clients für Mistral und Gemini.
    """

    def __init__(self, mistral_api_key: str, gemini_api_key: str):
        """
        Initialisiert die API-Clients für Mistral und Gemini.
        """
        try:
            self.mistral_client = Mistral(api_key=mistral_api_key)
            genai.configure(api_key=gemini_api_key)
            self.gemini_model = genai.GenerativeModel(
                model_name="gemini-2.0-flash-exp",
                generation_config={
                    "temperature": 1,
                    "top_p": 0.95,
                    "top_k": 40,
                    "max_output_tokens": 16192,
                    "response_mime_type": "text/plain",
                },
            )
            logger.info("API clients initialized successfully.")
        except Exception as e:
            logger.error(f"Error initializing API clients: {e}")
            raise

api_client = APIClient(mistral_api_key, gemini_api_key)
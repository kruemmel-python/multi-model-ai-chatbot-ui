from mistralai import Mistral
import google.generativeai as genai
from config import mistral_api_key, gemini_api_key
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class APIClient:
    """
    Klasse zur Verwaltung der API-Clients für Mistral und Gemini.

    Diese Klasse initialisiert die API-Clients für Mistral und Gemini mithilfe der bereitgestellten API-Schlüssel.
    Sie stellt sicher, dass die Clients korrekt konfiguriert sind und bereit für die Verwendung in anderen Teilen der Anwendung.

    Attributes:
        mistral_client (Mistral): Der Mistral API-Client.
        gemini_model (genai.GenerativeModel): Das Gemini-Modell für die Generierung von Inhalten.
    """

    def __init__(self, mistral_api_key: str, gemini_api_key: str):
        """
        Initialisiert die API-Clients für Mistral und Gemini.

        Args:
            mistral_api_key (str): Der API-Schlüssel für Mistral.
            gemini_api_key (str): Der API-Schlüssel für Gemini.

        Raises:
            Exception: Wenn die Initialisierung der API-Clients fehlschlägt.
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
        except Exception as e:
            logger.error(f"Fehler beim Initialisieren der API-Clients: {e}")
            raise

api_client = APIClient(mistral_api_key, gemini_api_key)

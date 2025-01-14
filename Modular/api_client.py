from mistralai import Mistral
import google.generativeai as genai
from config import mistral_api_key, gemini_api_key

class APIClient:
    """
    Eine Klasse zur Verwaltung von API-Clients für die Mistral- und Gemini-Plattformen.

    Attributes:
        mistral_client (Mistral): Ein Client-Objekt für die Mistral-API.
        gemini_generation_config (dict): Konfigurationsparameter für die Textgenerierung mit Gemini.
        gemini_model (GenerativeModel): Ein Modellobjekt für die Textgenerierung mit Gemini.
    """

    def __init__(self, mistral_api_key: str, gemini_api_key: str):
        """
        Initialisiert den APIClient mit API-Schlüsseln für Mistral und Gemini.

        Args:
            mistral_api_key (str): Der API-Schlüssel für die Mistral-API.
            gemini_api_key (str): Der API-Schlüssel für die Gemini-API.
        """
        # Initialisiere den Mistral-Client mit dem angegebenen API-Schlüssel.
        self.mistral_client = Mistral(api_key=mistral_api_key)
        
        # Konfiguriere den Gemini-Client mit dem angegebenen API-Schlüssel.
        genai.configure(api_key=gemini_api_key)
        
        # Festlegen der Generierungskonfiguration für das Gemini-Modell.
        self.gemini_generation_config = {
            "temperature": 1,  # Steuert die Kreativität der Ausgabe (höherer Wert = kreativere Ausgabe).
            "top_p": 0.95,  # Begrenzung der Wahrscheinlichkeitsmasse bei der Samplenauswahl.
            "top_k": 40,  # Begrenzung der Anzahl der berücksichtigten Token für die Auswahl.
            "max_output_tokens": 16192,  # Maximale Anzahl der generierten Token.
            "response_mime_type": "text/plain",  # MIME-Typ der Antwort.
        }
        
        # Initialisiere das Gemini-Modell mit dem Modellnamen und der Konfiguration.
        self.gemini_model = genai.GenerativeModel(
            model_name="gemini-2.0-flash-exp",
            generation_config=self.gemini_generation_config,
        )

# Erstellen eines APIClient-Objekts mit den angegebenen API-Schlüsseln.
api_client = APIClient(mistral_api_key, gemini_api_key)

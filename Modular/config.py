import os
import torch

# --- Konfiguration ---
# Festlegen des Geräts für die Berechnungen (CUDA wird bevorzugt, falls verfügbar).
device = "cuda:0" if torch.cuda.is_available() else "cpu"

# Bestimmen des Datentyps für die Torch-Operationen (float16 für CUDA, float32 für CPU).
torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

# ID des zu verwendenden Modells, hier ein Beispielmodell von OpenAI.
model_id = "openai/whisper-large-v3-turbo"

# --- API-Schlüssel und Modelle ---
# Abrufen des Mistral-API-Schlüssels aus Umgebungsvariablen, Standardwert bei Nichtvorhandensein.
mistral_api_key = os.environ.get('MISTRAL_API_KEY', 'Hier der KEY')

# Abrufen des Gemini-API-Schlüssels aus Umgebungsvariablen, Standardwert bei Nichtvorhandensein.
gemini_api_key = os.environ.get('GEMINI_API_KEY', 'Hier der KEY')

# IDs für die Mistral-Modelle, die in der Anwendung verwendet werden.
MISTRAL_CHAT_MODEL = "mistral-large-latest"  # Chat-Modell für Dialoge.
MISTRAL_IMAGE_MODEL = "pixtral-12b-2409"    # Bildmodell für visuelle Inhalte.

# Basis-URL für die Mistral-API-Endpunkte.
MISTRAL_API_URL = "https://api.mistral.ai/v1/chat/completions"

# --- OLLAMA Modelle ---
# Liste verfügbarer Modelle für die OLLAMA-Integration.
OLLAMA_MODELS = [
    "phi4-model:latest",                  # Neueste Version des phi4-Modells.
    "phi4:latest",                        # Neueste Version des phi4-Modells (Kurzform).
    "wizardlm2:7b-fp16",                  # WizardLM-Modell, 7 Milliarden Parameter, FP16.
    "unzensiert:latest",                  # Unzensiertes Modell, neueste Version.
    "llama2-uncensored:7b-chat-q8_0",     # LLaMA 2 Modell, unzensierte Variante für Chats.
    "teufel:latest",                      # Modell "Teufel", neueste Version.
    "Odin:latest",                        # Modell "Odin", neueste Version.
    "luzifer:latest",                     # Modell "Luzifer", neueste Version.
    "llama2-uncensored:latest"            # Neueste Version von LLaMA 2, unzensierte Variante.
]

# Standardmodell für OLLAMA, falls kein anderes Modell spezifiziert wird.
DEFAULT_OLLAMA_MODEL = "phi4:latest"

# --- Statusmeldungen ---
# Statusmeldungen für den Fortschritt bei der Verarbeitung von Anfragen.
STATUS_MESSAGE_GENERATING = "Antwort wird generiert..."  # Während der Verarbeitung.
STATUS_MESSAGE_COMPLETE = "Antwort generiert."           # Nach Abschluss.
STATUS_MESSAGE_ERROR = "Fehler: Die Anfrage konnte nicht verarbeitet werden."  # Bei Fehlern.

# --- Speicherpfade ---
# Verzeichnis für die Speicherung von Daten.
SAVE_DIR = ".gradio"

# Dateipfad für die gespeicherten Daten, kombiniert Verzeichnis und Dateiname.
SAVE_FILE = os.path.join(SAVE_DIR, "save.json")

import os
import torch
from dotenv import load_dotenv
import json

# Lade die Umgebungsvariablen aus der .env-Datei
load_dotenv()

# --- Konfiguration ---
device = "cuda:0" if torch.cuda.is_available() else "cpu"
torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

model_id = "openai/whisper-large-v3-turbo"

# --- API-Schlüssel und Modelle ---
mistral_api_key = os.getenv('MISTRAL_API_KEY')
gemini_api_key = os.getenv('GEMINI_API_KEY')

MISTRAL_CHAT_MODEL = "mistral-large-latest"
MISTRAL_IMAGE_MODEL = "pixtral-12b-2409"

MISTRAL_API_URL = "https://api.mistral.ai/v1/chat/completions"

OLLAMA_MODELS = [
    "phi4-model:latest",
    "phi4:latest",
    "wizardlm2:7b-fp16",
    "unzensiert:latest",
    "llama2-uncensored:7b-chat-q8_0",
    "teufel:latest",
    "Odin:latest",
    "luzifer:latest",
    "llama2-uncensored:latest"
]

DEFAULT_OLLAMA_MODEL = "phi4:latest"
STATUS_MESSAGE_GENERATING = "Antwort wird generiert..."
STATUS_MESSAGE_COMPLETE = "Antwort generiert."
STATUS_MESSAGE_ERROR = "Fehler: Die Anfrage konnte nicht verarbeitet werden."

SAVE_DIR = ".gradio"
SAVE_FILE = os.path.join(SAVE_DIR, "save.json")
CONFIG_FILE = os.path.join(SAVE_DIR, "config.json")

# --- Standardkonfigurationen ---
DEFAULT_CONFIG = {
    "enable_tts": False,
    "tts_speed": 150,  # Standardgeschwindigkeit für TTS
    "tts_volume": 0.9,  # Standardlautstärke für TTS
    "tts_voice": "com.apple.speech.synthesis.voice.Alex"  # Standardstimme für TTS (kann je nach Betriebssystem variieren)
}

def load_config() -> dict:
    """Lädt die Konfiguration aus einer JSON-Datei."""
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return DEFAULT_CONFIG
    return DEFAULT_CONFIG

def save_config(config: dict):
    """Speichert die Konfiguration in einer JSON-Datei."""
    os.makedirs(SAVE_DIR, exist_ok=True)
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=4)

config = load_config()
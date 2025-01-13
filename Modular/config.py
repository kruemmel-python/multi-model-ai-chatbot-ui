import os
import torch

# --- Konfiguration ---
device = "cuda:0" if torch.cuda.is_available() else "cpu"
torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

model_id = "openai/whisper-large-v3-turbo"

# --- API-Schlüssel und Modelle ---
mistral_api_key = os.environ.get('MISTRAL_API_KEY', 'Hier der KEY')
gemini_api_key = os.environ.get('GEMINI_API_KEY', 'Hier der KEY')

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

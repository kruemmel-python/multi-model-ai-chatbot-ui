from pydub import AudioSegment
import os
from model_pipeline import model_pipeline
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def process_audio(audio_file_path: str) -> str:
    """
    Verarbeitet eine Audiodatei und extrahiert den Text.

    Diese Funktion konvertiert eine Audiodatei in das WAV-Format und verwendet dann die Modell-Pipeline,
    um den Text aus der Audiodatei zu extrahieren.

    Args:
        audio_file_path (str): Der Pfad zur Audiodatei.

    Returns:
        str: Der extrahierte Text aus der Audiodatei.

    Raises:
        ValueError: Wenn die Verarbeitung der Audiodatei fehlschlägt.
    """
    try:
        audio = AudioSegment.from_file(audio_file_path)
        temp_audio_path = "temp_audio.wav"
        audio.export(temp_audio_path, format="wav")
        result = model_pipeline.pipe(temp_audio_path)
        os.remove(temp_audio_path)
        return result["text"]
    except Exception as e:
        logger.error(f"Fehler bei der Verarbeitung der Audiodatei: {e}")
        raise ValueError(f"Fehler bei der Verarbeitung der Audiodatei: {e}")

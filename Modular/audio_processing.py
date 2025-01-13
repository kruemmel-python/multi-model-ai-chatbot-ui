from pydub import AudioSegment
import os
from model_pipeline import model_pipeline

def process_audio(audio_file_path: str) -> str:
    """Verarbeitet eine Audiodatei und extrahiert den Text."""
    try:
        # Audio laden und konvertieren
        audio = AudioSegment.from_file(audio_file_path)
        temp_audio_path = "temp_audio.wav"
        audio.export(temp_audio_path, format="wav")  # Konvertieren in WAV
        # Transkription
        result = model_pipeline.pipe(temp_audio_path)
        os.remove(temp_audio_path)  # Temporäre Datei löschen
        return result["text"]
    except Exception as e:
        raise ValueError(f"Fehler bei der Verarbeitung der Audiodatei: {e}")

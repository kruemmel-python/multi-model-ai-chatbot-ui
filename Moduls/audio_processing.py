from pydub import AudioSegment
import os
from model_pipeline import model_pipeline
import logging

logger = logging.getLogger(__name__)

def process_audio(audio_file_path: str) -> str:
    """
    Verarbeitet eine Audiodatei und extrahiert den Text.
    """
    try:
        audio = AudioSegment.from_file(audio_file_path)
        temp_audio_path = "temp_audio.wav"
        audio.export(temp_audio_path, format="wav")
        result = model_pipeline.pipe(temp_audio_path)
        os.remove(temp_audio_path)
        logger.info(f"Audio processed successfully: {audio_file_path}")
        return result["text"]
    except Exception as e:
        logger.error(f"Error processing audio file: {e}")
        raise ValueError(f"Error processing audio file: {e}")
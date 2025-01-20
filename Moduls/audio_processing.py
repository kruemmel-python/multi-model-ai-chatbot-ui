import logging
from pydub import AudioSegment
import os
from openai import OpenAI

logger = logging.getLogger(__name__)

# Initialisieren Sie den OpenAI-Client
client = OpenAI()

def process_audio(audio_file_path: str) -> str:
    """
    Verarbeitet eine Audiodatei und extrahiert den Text.
    """
    try:
        logger.debug(f"Starte Audioverarbeitung für: {audio_file_path}")

        # Überprüfen, ob die Datei existiert
        if not os.path.exists(audio_file_path):
            raise FileNotFoundError(f"Audio file not found: {audio_file_path}")

        # Laden der Audiodatei mit pydub
        audio = AudioSegment.from_file(audio_file_path)
        logger.debug(f"Audio geladen: {len(audio)}ms")

        # Konvertieren der Audiodatei in MP3-Format
        temp_audio_path = "temp_audio.mp3"
        audio.export(temp_audio_path, format="mp3")
        logger.debug(f"Audio in temporäre Datei exportiert: {temp_audio_path}")

        # Überprüfen, ob die temporäre Audiodatei erstellt wurde
        if not os.path.exists(temp_audio_path):
            raise FileNotFoundError(f"Temporary audio file not created: {temp_audio_path}")

        # Transkription der Audiodatei mit OpenAI
        with open(temp_audio_path, "rb") as audio_file:
            transcription = client.audio.transcriptions.create(
                file=audio_file,
                model="whisper-1",
                response_format="verbose_json",
                timestamp_granularities=["word"]
            )

        # Entfernen der temporären Audiodatei
        os.remove(temp_audio_path)
        logger.debug(f"Temporäre Audio-Datei entfernt: {temp_audio_path}")

        logger.info(f"Audio processed successfully: {audio_file_path}")
        return transcription.text if transcription.text else ""  # Stelle sicher, dass nie ein leerer String zurückgegeben wird.
    except FileNotFoundError as fnf_error:
        logger.error(f"File not found: {fnf_error}")
        raise ValueError(f"File not found: {fnf_error}")
    except ValueError as ve:
        logger.error(f"Value error: {ve}")
        raise ValueError(f"Value error: {ve}")
    except Exception as e:
        logger.error(f"Error processing audio file: {e}")
        raise ValueError(f"Error processing audio file: {e}")

# Beispielaufruf der Funktion
if __name__ == "__main__":
    try:
        result = process_audio("temp_audio.wav")
        print(f"Extracted text: {result}")
    except ValueError as e:
        print(f"Error: {e}")

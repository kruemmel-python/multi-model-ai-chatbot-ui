from pydub import AudioSegment
import os
from model_pipeline import model_pipeline

def process_audio(audio_file_path: str) -> str:
    """
    Verarbeitet eine Audiodatei und extrahiert den Text durch eine Transkriptionspipeline.

    Args:
        audio_file_path (str): Der Dateipfad der Eingabe-Audiodatei.

    Returns:
        str: Der transkribierte Text aus der Audiodatei.

    Raises:
        ValueError: Wenn ein Fehler bei der Verarbeitung oder Transkription der Audiodatei auftritt.
    """
    try:
        # Audiodatei laden und in ein bearbeitbares Format konvertieren.
        audio = AudioSegment.from_file(audio_file_path)  # Unterstützt verschiedene Audioformate.
        
        # Temporärer Pfad für die WAV-Datei, da Transkriptionsmodelle häufig WAV-Dateien erfordern.
        temp_audio_path = "temp_audio.wav"
        
        # Exportieren der Audiodatei in das WAV-Format.
        audio.export(temp_audio_path, format="wav")
        
        # Transkription der WAV-Datei durch die Model-Pipeline.
        result = model_pipeline.pipe(temp_audio_path)
        
        # Entfernen der temporären WAV-Datei, um Speicherplatz freizugeben.
        os.remove(temp_audio_path)
        
        # Rückgabe des extrahierten Textes aus der Transkription.
        return result["text"]
    except Exception as e:
        # Fehlerbehandlung: Gibt eine verständliche Fehlermeldung aus, wenn ein Problem auftritt.
        raise ValueError(f"Fehler bei der Verarbeitung der Audiodatei: {e}")

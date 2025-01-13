from PIL import Image
from typing import Optional, Generator, List, Tuple
from helpers import encode_image, format_chat_message
from api_client import api_client
from audio_processing import process_audio
import os
import google.generativeai as genai

class GeminiFunctions:
    def __init__(self):
        pass

    def upload_to_gemini(self, image: Image.Image):
        """Lädt ein Bild zur Gemini API hoch."""
        image_path = "temp_image.jpg"
        image.save(image_path)
        sample_file = genai.upload_file(path=image_path, display_name="Hochgeladenes Bild")
        print(f"Hochgeladene Datei '{sample_file.display_name}' as: {sample_file.uri}")
        os.remove(image_path)
        return sample_file

    def chat_with_gemini(
        self,
        user_input: str,
        chat_history: List[Tuple[str, str]],
        image: Optional[Image.Image] = None,
        audio_file: Optional[str] = None
    ) -> Generator[Tuple[List[Tuple[str, str]], str], None, None]:
        if not user_input.strip() and not audio_file:
            yield chat_history, "Bitte geben Sie eine Nachricht ein oder laden Sie eine Audiodatei hoch."
            return

        if audio_file:
            try:
                user_input = process_audio(audio_file)  # Audio in Text umwandeln
            except Exception as e:
                chat_history.append((None, f"Fehler bei der Verarbeitung der Audiodatei: {e}"))
                yield chat_history, ""
                return

        chat_history.append((user_input, None))
        yield chat_history, ""

        # Chatverlauf initialisieren
        history = [{"role": "user", "parts": [user_input]}]

        if image:
            try:
                sample_file = self.upload_to_gemini(image)
                history[0]["parts"].append(sample_file)
            except Exception as e:
                chat_history.append((None, f"Fehler beim Hochladen des Bildes: {e}"))
                yield chat_history, ""
                return

        try:
            # Chat mit Gemini starten
            chat_session = api_client.gemini_model.start_chat(history=history)
            response_text = chat_session.send_message(user_input).text
            chat_history.append((None, format_chat_message(response_text)))
        except Exception as e:
            chat_history.append((None, f"Fehler bei der Verarbeitung der Anfrage: {e}"))

        yield chat_history, ""

    def analyze_image_gemini(self, image: Optional[Image.Image], chat_history: List[Tuple[str, str]], user_input: str) -> List[Tuple[str, str]]:
        """Analysiert ein Bild mit Gemini."""
        if image is None:
            chat_history.append((None, "Bitte laden Sie ein Bild hoch."))
            return chat_history
        try:
            sample_file = self.upload_to_gemini(image)
            response = api_client.gemini_model.generate_content([f"{user_input} Beschreiben Sie das Bild mit einer kreativen Beschreibung. Bitte in German antworten.", sample_file])
            response_text = response.text
            chat_history.append((None, format_chat_message(response_text)))
        except Exception as e:
            chat_history.append((None, f"Fehler bei der Bildanalyse: {e}"))

        return chat_history

gemini_functions = GeminiFunctions()

from PIL import Image
from typing import Optional, Generator, List, Tuple
from helpers import encode_image, format_chat_message
from api_client import api_client
from audio_processing import process_audio
import os
import google.generativeai as genai

class GeminiFunctions:
    """
    Eine Klasse zur Integration und Nutzung von Gemini-Funktionen, einschließlich
    Bild-Upload, Chat-Interaktionen und Bildanalyse.
    """

    def __init__(self):
        """Initialisiert eine Instanz der GeminiFunctions-Klasse."""
        pass

    def upload_to_gemini(self, image: Image.Image):
        """
        Lädt ein Bild zur Gemini API hoch.

        Args:
            image (Image.Image): Das hochzuladende Bild.

        Returns:
            object: Informationen über die hochgeladene Datei.

        Raises:
            Exception: Bei Fehlern während des Uploads.
        """
        image_path = "temp_image.jpg"
        # Bild temporär speichern, um es hochzuladen.
        image.save(image_path)
        try:
            sample_file = genai.upload_file(path=image_path, display_name="Hochgeladenes Bild")
            print(f"Hochgeladene Datei '{sample_file.display_name}' als: {sample_file.uri}")
            return sample_file
        finally:
            # Temporäre Datei entfernen.
            os.remove(image_path)

    def chat_with_gemini(
        self,
        user_input: str,
        chat_history: List[Tuple[str, str]],
        image: Optional[Image.Image] = None,
        audio_file: Optional[str] = None
    ) -> Generator[Tuple[List[Tuple[str, str]], str], None, None]:
        """
        Startet einen Chat mit Gemini unter Berücksichtigung von Eingabe, Bild und Audiodatei.

        Args:
            user_input (str): Die Texteingabe des Benutzers.
            chat_history (List[Tuple[str, str]]): Der bisherige Chatverlauf.
            image (Optional[Image.Image]): Ein optionales Bild für die Interaktion.
            audio_file (Optional[str]): Eine optionale Audiodatei für die Interaktion.

        Yields:
            Tuple[List[Tuple[str, str]], str]: Aktualisierter Chatverlauf und Statusnachricht.
        """
        if not user_input.strip() and not audio_file:
            yield chat_history, "Bitte geben Sie eine Nachricht ein oder laden Sie eine Audiodatei hoch."
            return

        if audio_file:
            try:
                # Audiodatei in Text umwandeln.
                user_input = process_audio(audio_file)
            except Exception as e:
                chat_history.append((None, f"Fehler bei der Verarbeitung der Audiodatei: {e}"))
                yield chat_history, ""
                return

        chat_history.append((user_input, None))  # Benutzer-Eingabe hinzufügen.
        yield chat_history, ""

        # Initialisiere den Chatverlauf für Gemini.
        history = [{"role": "user", "parts": [user_input]}]

        if image:
            try:
                # Bild zur Gemini-API hochladen und zum Verlauf hinzufügen.
                sample_file = self.upload_to_gemini(image)
                history[0]["parts"].append(sample_file)
            except Exception as e:
                chat_history.append((None, f"Fehler beim Hochladen des Bildes: {e}"))
                yield chat_history, ""
                return

        try:
            # Interaktion mit Gemini starten.
            chat_session = api_client.gemini_model.start_chat(history=history)
            response_text = chat_session.send_message(user_input).text
            chat_history.append((None, format_chat_message(response_text)))
        except Exception as e:
            chat_history.append((None, f"Fehler bei der Verarbeitung der Anfrage: {e}"))

        yield chat_history, ""

    def analyze_image_gemini(
        self, 
        image: Optional[Image.Image], 
        chat_history: List[Tuple[str, str]], 
        user_input: str
    ) -> List[Tuple[str, str]]:
        """
        Analysiert ein Bild mit der Gemini-API.

        Args:
            image (Optional[Image.Image]): Das Bild, das analysiert werden soll.
            chat_history (List[Tuple[str, str]]): Der bisherige Chatverlauf.
            user_input (str): Benutzer-Input für die Bildanalyse.

        Returns:
            List[Tuple[str, str]]: Der aktualisierte Chatverlauf.
        """
        if image is None:
            chat_history.append((None, "Bitte laden Sie ein Bild hoch."))
            return chat_history

        try:
            # Bild hochladen und Anfrage an die Gemini-API senden.
            sample_file = self.upload_to_gemini(image)
            response = api_client.gemini_model.generate_content([
                f"{user_input} Beschreiben Sie das Bild mit einer kreativen Beschreibung. Bitte in German antworten.",
                sample_file
            ])
            response_text = response.text
            chat_history.append((None, format_chat_message(response_text)))
        except Exception as e:
            chat_history.append((None, f"Fehler bei der Bildanalyse: {e}"))

        return chat_history

# Instanziierung eines GeminiFunctions-Objekts.
gemini_functions = GeminiFunctions()

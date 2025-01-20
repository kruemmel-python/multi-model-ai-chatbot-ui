import asyncio
import logging
import os
from functools import lru_cache
from typing import List, Tuple, Optional, Generator
import google.generativeai as genai
from PIL import Image
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import PythonLexer
from black import format_str, FileMode
from helpers import format_chat_message  # Import der format_chat_message-Funktion
from api_client import api_client
from config import config
from gtts import gTTS
from playsound import playsound
from audio_processing import process_audio  # Import der process_audio-Funktion

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class GeminiFunctions:
    def __init__(self):
        pass

    def _speak_text(self, text: str, config: dict) -> None:
        """
        Konvertiert Text in Sprache und spielt diese ab.

        Args:
            text (str): Der zu sprechende Text.
            config (dict): Die Konfiguration für TTS (Geschwindigkeit, Lautstärke, Stimme).
        """
        try:
            tts = gTTS(text, lang='de')
            temp_file = "temp_tts.mp3"
            temp_file_path = os.path.join(os.path.dirname(__file__), temp_file)
            tts.save(temp_file_path)
            logger.debug(f"TTS Datei gespeichert: {temp_file_path}")

            # Verwenden Sie playsound zum Abspielen der MP3-Datei
            playsound(temp_file_path)

            os.remove(temp_file_path)
            logger.debug(f"Temporäre Datei gelöscht: {temp_file_path}")
        except Exception as e:
            logger.error(f"Error during TTS conversion: {e}")

    async def _async_speak_text(self, text: str, config: dict):
        """
        Asynchrone Funktion zum Sprechen von Text.
        """
        loop = asyncio.get_running_loop()
        await loop.run_in_executor(None, self._speak_text, text, config)

    def upload_to_gemini(self, image: Image.Image):
        """
        Lädt ein Bild zur Gemini API hoch.

        Args:
            image (Image.Image): Das hochzuladende Bild.

        Returns:
            sample_file: Die hochgeladene Datei.

        Raises:
            Exception: Wenn das Hochladen des Bildes fehlschlägt.
        """
        try:
            image_path = "temp_image.jpg"
            image.save(image_path)
            sample_file = genai.upload_file(path=image_path, display_name="Hochgeladenes Bild")
            logger.info(f"Hochgeladene Datei '{sample_file.display_name}' as: {sample_file.uri}")
            os.remove(image_path)
            return sample_file
        except Exception as e:
            logger.error(f"Fehler beim Hochladen des Bildes: {e}")
            raise

    def chat_with_gemini(
        self,
        user_input: str,
        chat_history: List[Tuple[str, str]],
        image: Optional[Image.Image] = None,
        audio_file: Optional[str] = None,
        enable_tts: bool = False  # Neues Argument hinzugefügt
    ) -> Tuple[List[Tuple[str, str]], str]:
        """
        Chattet mit dem Gemini-Modell.

        Args:
            user_input (str): Die Benutzereingabe.
            chat_history (List[Tuple[str, str]]): Der Chatverlauf.
            image (Optional[Image.Image]): Das hochzuladende Bild.
            audio_file (Optional[str]): Der Pfad zur Audiodatei.
            enable_tts (bool): Aktiviert oder deaktiviert TTS.

        Returns:
            Tuple[List[Tuple[str, str]], str]: Der aktualisierte Chatverlauf und die Antwort.
        """
        if not user_input.strip() and not audio_file:
            return chat_history, "Bitte geben Sie eine Nachricht ein oder laden Sie eine Audiodatei hoch."

        if audio_file:
            try:
                user_input = process_audio(audio_file)
            except Exception as e:
                chat_history.append((None, f"Fehler bei der Verarbeitung der Audiodatei: {e}"))
                return chat_history, ""

        chat_history.append((user_input, None))

        history = [{"role": "user", "parts": [user_input]}]

        if image:
            try:
                sample_file = self.upload_to_gemini(image)
                history[0]["parts"].append(sample_file)
            except Exception as e:
                chat_history.append((None, f"Fehler beim Hochladen des Bildes: {e}"))
                return chat_history, ""

        try:
            chat_session = api_client.gemini_model.start_chat(history=history)
            response_text = chat_session.send_message(user_input).text
            chat_history.append((None, format_chat_message(response_text)))

            if enable_tts:
                asyncio.run(self._async_speak_text(response_text, config))

        except Exception as e:
            chat_history.append((None, f"Fehler bei der Verarbeitung der Anfrage: {e}"))

        return chat_history, ""


    def analyze_image_gemini(self, image: Optional[Image.Image], chat_history: List[Tuple[str, str]], user_input: str, tts_enabled: bool) -> List[Tuple[str, str]]:
        """
        Analysiert ein Bild mit Gemini.

        Args:
            image (Optional[Image.Image]): Das zu analysierende Bild.
            chat_history (List[Tuple[str, str]]): Der Chatverlauf.
            user_input (str): Die Benutzereingabe.
            tts_enabled (bool): Aktiviert oder deaktiviert TTS.

        Returns:
            List[Tuple[str, str]]: Der aktualisierte Chatverlauf.
        """
        if image is None:
            chat_history.append((None, "Bitte laden Sie ein Bild hoch."))
            return chat_history
        try:
            sample_file = self.upload_to_gemini(image)
            response = api_client.gemini_model.generate_content([f"{user_input} Beschreiben Sie das Bild mit einer kreativen Beschreibung. Bitte in Deutsch antworten.", sample_file])
            response_text = response.text
            chat_history.append((None, format_chat_message(response_text)))  # Entfernt `speak=config.get("enable_tts", False)`
        except Exception as e:
            chat_history.append((None, f"Fehler bei der Bildanalyse: {e}"))

        return chat_history


    def format_code(self, code_input: str) -> str:
        """
        Formatiert den gegebenen Python-Code mit Pygments.

        Args:
            code_input (str): Der Eingabe-Code.

        Returns:
            str: Der formatierte Code.
        """
        try:
            formatter = HtmlFormatter(style='colorful')
            highlighted_code = highlight(code_input, PythonLexer(), formatter)
            return highlighted_code
        except Exception as e:
            logger.error(f"Fehler beim Formatieren des Codes: {e}")
            return f"<pre>{code_input}</pre>"

    def save_code(self, code_input: str, filename: str) -> None:
        """
        Speichert den gegebenen Code in einer Datei.

        Args:
            code_input (str): Der Eingabe-Code.
            filename (str): Der Dateiname.
        """
        with open(filename, 'w') as file:
            file.write(code_input)

    def load_code(self, filename: str) -> str:
        """
        Lädt den Code aus einer Datei.

        Args:
            filename (str): Der Dateiname.

        Returns:
            str: Der geladene Code.
        """
        with open(filename, 'r') as file:
            return file.read()

    def format_code_with_black(self, code_input: str) -> str:
        """
        Formatiert den gegebenen Code mit Black.

        Args:
            code_input (str): Der Eingabe-Code.

        Returns:
            str: Der formatierte Code.
        """
        try:
            formatted_code = format_str(code_input, mode=FileMode())
            return formatted_code
        except Exception as e:
            logger.error(f"Fehler beim Formatieren des Codes mit black: {e}")
            return code_input

    @lru_cache(maxsize=100)
    def analyze_code(self, code_input: str) -> str:
        """
        Analysiert den gegebenen Python-Code und gibt Feedback.

        Args:
            code_input (str): Der Eingabe-Code.

        Returns:
            str: Das Feedback zum Code.
        """
        try:
            prompt = f"Analysiere diesen Python-Code und gib Feedback:\n\n{code_input}\n\nAntworte auf Deutsch und mit Zeilenumbrüchen."
            response = api_client.gemini_model.generate_content(prompt)
            return response.text if response is not None else "Fehler während der Analyse."
        except Exception as e:
            logger.error(f"Fehler während der Analyse: {e}")
            return str(e)

    @lru_cache(maxsize=100)
    def suggest_code_improvements(self, code_input: str) -> str:
        """
        Schlägt Verbesserungen für den gegebenen Python-Code vor.

        Args:
            code_input (str): Der Eingabe-Code.

        Returns:
            str: Die vorgeschlagenen Verbesserungen.
        """
        try:
            prompt = f"Schlage Verbesserungen für diesen Python-Code vor:\n\n{code_input}\n\nAntworte auf Deutsch und mit Zeilenumbrüchen."
            response = api_client.gemini_model.generate_content(prompt)
            return response.text if response is not None else "Fehler während der Generierung von Vorschlägen."
        except Exception as e:
            logger.error(f"Fehler während der Generierung von Vorschlägen: {e}")
            return str(e)

    def update_model(self, model_name: str) -> None:
        """
        Aktualisiert das Gemini-Modell basierend auf der Auswahl.

        Args:
            model_name (str): Der Name des ausgewählten Modells.
        """
        global model
        model = setup_api(GEMINI_API_KEY)
        model.model_name = model_name

gemini_functions = GeminiFunctions()

import requests
import json
from typing import List, Tuple, Generator, Optional
from PIL import Image
from helpers import encode_image, format_chat_message
from api_client import api_client
from config import MISTRAL_CHAT_MODEL, MISTRAL_IMAGE_MODEL, MISTRAL_API_URL, mistral_api_key
from audio_processing import process_audio

class MistralFunctions:
    """
    Eine Klasse zur Interaktion mit der Mistral-API, einschließlich Chat, Bildanalyse und Bildvergleich.
    """

    def __init__(self):
        """Initialisiert eine Instanz der MistralFunctions-Klasse."""
        pass

    def chat_with_mistral(
        self, 
        user_input: str, 
        chat_history: List[Tuple[str, str]], 
        image: Optional[Image.Image] = None, 
        audio_file: Optional[str] = None
    ) -> Generator[Tuple[List[Tuple[str, str]], str], None, None]:
        """
        Führt einen Chat mit Mistral durch, unterstützt Text-, Bild- und Audioeingaben.

        Args:
            user_input (str): Der Textinput des Benutzers.
            chat_history (List[Tuple[str, str]]): Der bisherige Chatverlauf.
            image (Optional[Image.Image]): Ein optionales Bild für die Konversation.
            audio_file (Optional[str]): Eine optionale Audiodatei für die Konversation.

        Yields:
            Tuple[List[Tuple[str, str]], str]: Aktualisierter Chatverlauf und Statusmeldung.
        """
        if not user_input.strip() and not audio_file:
            yield chat_history, "Bitte geben Sie eine Nachricht ein oder laden Sie eine Audiodatei hoch."
            return

        # Verarbeitung von Audiodateien
        if audio_file:
            try:
                user_input = process_audio(audio_file)
            except Exception as e:
                chat_history.append((None, f"Fehler bei der Verarbeitung der Audiodatei: {e}"))
                yield chat_history, ""
                return

        # Benutzeranfrage zum Chatverlauf hinzufügen
        chat_history.append((user_input, None))
        yield chat_history, ""

        messages = [{"role": "user", "content": user_input}]

        # Verarbeitung von Bildern
        if image:
            try:
                image_base64 = encode_image(image)
                messages[0]["content"] = [
                    {"type": "text", "text": user_input},
                    {"type": "image_url", "image_url": f"data:image/jpeg;base64,{image_base64}"},
                ]
            except Exception as e:
                chat_history.append((None, f"Fehler beim Hochladen des Bildes: {e}"))
                yield chat_history, ""
                return

        # API-Anfrage an die Mistral-API senden
        try:
            headers = {
                "Content-Type": "application/json",
                "Accept": "application/json",
                "Authorization": f"Bearer {mistral_api_key}",
            }
            payload = {
                "model": MISTRAL_CHAT_MODEL,
                "messages": messages,
                "temperature": 1,
                "top_p": 0.95,
                "max_tokens": 16192,
                "stream": True
            }

            response = requests.post(MISTRAL_API_URL, headers=headers, json=payload, stream=True)
            response.raise_for_status()
            full_response = ""

            # Verarbeitung der Antwort in Echtzeit
            for chunk in response.iter_lines():
                if chunk:
                    try:
                        if chunk == b"data: [DONE]":
                            break

                        if chunk.strip():
                            chunk_data = json.loads(chunk.decode('utf-8').replace('data: ', ''))
                            if 'choices' in chunk_data and chunk_data['choices']:
                                delta_content = chunk_data['choices'][0]['delta'].get('content', '')
                                if delta_content:
                                    full_response += delta_content
                                    formatted_response = format_chat_message(full_response)
                                    chat_history[-1] = (user_input, formatted_response)
                                    yield chat_history, ""
                    except json.JSONDecodeError:
                        continue

            # Abschlussnachricht oder Fehlermeldung
            if full_response:
                chat_history[-1] = (user_input, format_chat_message(full_response))
                yield chat_history, ""
            else:
                chat_history.append((None, "Keine Antwort vom Modell erhalten."))
                yield chat_history, ""
        except requests.exceptions.RequestException as e:
            chat_history.append((None, f"Fehler bei der Verarbeitung der Anfrage: {e}"))
            yield chat_history, ""
        except Exception as e:
            chat_history.append((None, f"Unbekannter Fehler: {e}. Bitte versuchen Sie es nochmal."))
            yield chat_history, ""

    def analyze_image_mistral(
        self, 
        image: Optional[Image.Image], 
        chat_history: List[Tuple[str, str]], 
        user_input: str, 
        prompt: str
    ) -> List[Tuple[str, str]]:
        """
        Analysiert ein Bild mit Mistral.

        Args:
            image (Optional[Image.Image]): Das zu analysierende Bild.
            chat_history (List[Tuple[str, str]]): Der bisherige Chatverlauf.
            user_input (str): Der Benutzerinput.
            prompt (str): Der spezifische Prompt für die Bildanalyse.

        Returns:
            List[Tuple[str, str]]: Der aktualisierte Chatverlauf.
        """
        if image is None:
            chat_history.append((None, "Bitte laden Sie ein Bild hoch."))
            return chat_history

        try:
            image_base64 = encode_image(image)
            messages = [
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": f"{user_input} {prompt}"},
                        {"type": "image_url", "image_url": f"data:image/jpeg;base64,{image_base64}"},
                    ],
                }
            ]

            chat_response = api_client.mistral_client.chat.complete(
                model=MISTRAL_IMAGE_MODEL,
                messages=messages
            )

            response_text = chat_response.choices[0].message.content
            chat_history.append((None, format_chat_message(response_text)))
        except Exception as e:
            chat_history.append((None, f"Unbekannter Fehler bei der Bildanalyse: {e}. Bitte versuchen Sie es nochmal."))

        return chat_history

    def compare_images_mistral(
        self, 
        image1: Optional[Image.Image], 
        image2: Optional[Image.Image], 
        chat_history: List[Tuple[str, str]]
    ) -> List[Tuple[str, str]]:
        """
        Vergleicht zwei Bilder mit Mistral.

        Args:
            image1 (Optional[Image.Image]): Das erste Bild.
            image2 (Optional[Image.Image]): Das zweite Bild.
            chat_history (List[Tuple[str, str]]): Der bisherige Chatverlauf.

        Returns:
            List[Tuple[str, str]]: Der aktualisierte Chatverlauf.
        """
        if image1 is None or image2 is None:
            chat_history.append((None, "Bitte laden Sie zwei Bilder hoch."))
            return chat_history

        try:
            image1_base64 = encode_image(image1)
            image2_base64 = encode_image(image2)
            messages = [
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "Was sind die Unterschiede zwischen den beiden Bildern? Bitte in Deutsch antworten."},
                        {"type": "image_url", "image_url": f"data:image/jpeg;base64,{image1_base64}"},
                        {"type": "image_url", "image_url": f"data:image/jpeg;base64,{image2_base64}"},
                    ],
                }
            ]

            chat_response = api_client.mistral_client.chat.complete(
                model=MISTRAL_IMAGE_MODEL,
                messages=messages
            )

            response_text = chat_response.choices[0].message.content
            chat_history.append((None, format_chat_message(response_text)))
        except Exception as e:
            chat_history.append((None, f"Unbekannter Fehler beim Vergleich der Bilder: {e}. Bitte versuchen Sie es nochmal."))

        return chat_history

# Instanziierung eines MistralFunctions-Objekts.
mistral_functions = MistralFunctions()

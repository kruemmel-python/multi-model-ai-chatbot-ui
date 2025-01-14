from PIL import Image
import base64
from io import BytesIO

def encode_image(image: Image.Image) -> str:
    """
    Kodiert ein Bild in einen Base64-String.

    Args:
        image (Image.Image): Das zu kodierende Bild.

    Returns:
        str: Der Base64-kodierte String des Bildes.

    Beschreibung:
        Diese Funktion wandelt ein PIL-Image-Objekt in einen Base64-String um, 
        der beispielsweise für die Übertragung oder Speicherung in textbasierten Formaten 
        wie JSON verwendet werden kann.
    """
    # Erstelle einen gepufferten Stream für die Bilddaten.
    buffered = BytesIO()
    # Speichere das Bild im JPEG-Format in den Puffer.
    image.save(buffered, format="JPEG")
    # Kodiert die Binärdaten des Puffers in Base64 und gibt diese als String zurück.
    return base64.b64encode(buffered.getvalue()).decode('utf-8')

def format_chat_message(text: str) -> str:
    """
    Formatiert eine Chatnachricht mit einem benutzerdefinierten HTML-Stil.

    Args:
        text (str): Der Text der Nachricht.

    Returns:
        str: Der formatierte Text als HTML-String.

    Beschreibung:
        Diese Funktion formatiert den übergebenen Text in einen HTML-Block mit 
        einem dunklen Hintergrund, Padding und abgerundeten Ecken, um ein 
        ansprechendes Design für Chatnachrichten zu gewährleisten.
    """
    return f"<div style='background-color:#333333; padding: 10px; margin-bottom: 5px; border-radius: 5px;'>{text}</div>"

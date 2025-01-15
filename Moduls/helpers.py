from PIL import Image
import base64
from io import BytesIO
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def encode_image(image: Image.Image) -> str:
    """
    Kodiert ein Bild in Base64.

    Args:
        image (Image.Image): Das zu kodierende Bild.

    Returns:
        str: Das Base64-kodierte Bild.

    Raises:
        Exception: Wenn die Kodierung des Bildes fehlschlägt.
    """
    try:
        buffered = BytesIO()
        image.save(buffered, format="JPEG")
        return base64.b64encode(buffered.getvalue()).decode('utf-8')
    except Exception as e:
        logger.error(f"Fehler beim Kodieren des Bildes: {e}")
        raise

def format_chat_message(text: str) -> str:
    """
    Formatiert eine Chatnachricht mit benutzerdefiniertem Stil.

    Args:
        text (str): Der Text der Chatnachricht.

    Returns:
        str: Die formatierte Chatnachricht.
    """
    return f"<div style='background-color:#333333; padding: 10px; margin-bottom: 5px; border-radius: 5px;'>{text}</div>"
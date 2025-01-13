from PIL import Image
import base64
from io import BytesIO

def encode_image(image: Image.Image) -> str:
    """Kodiert ein Bild in Base64."""
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode('utf-8')

def format_chat_message(text: str) -> str:
    """Formatiert eine Chatnachricht mit benutzerdefiniertem Stil."""
    return f"<div style='background-color:#333333; padding: 10px; margin-bottom: 5px; border-radius: 5px;'>{text}</div>"

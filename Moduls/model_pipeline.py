from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
from config import device, torch_dtype, model_id
import torch
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class ModelPipeline:
    """
    Klasse zur Verwaltung der Modell-Pipeline.

    Diese Klasse initialisiert die Modell-Pipeline für die Spracherkennung.

    Attributes:
        model (AutoModelForSpeechSeq2Seq): Das Modell für die Spracherkennung.
        processor (AutoProcessor): Der Prozessor für die Spracherkennung.
        pipe (pipeline): Die Pipeline für die Spracherkennung.
    """

    def __init__(self, model_id: str, device: str, torch_dtype: torch.dtype):
        """
        Initialisiert die Modell-Pipeline.

        Args:
            model_id (str): Die ID des Modells.
            device (str): Das Gerät (CPU oder GPU).
            torch_dtype (torch.dtype): Der Datentyp für die Berechnungen.

        Raises:
            Exception: Wenn die Initialisierung der Modell-Pipeline fehlschlägt.
        """
        try:
            self.model = AutoModelForSpeechSeq2Seq.from_pretrained(
                model_id, torch_dtype=torch_dtype, low_cpu_mem_usage=True, use_safetensors=True
            )
            self.model.to(device)
            self.processor = AutoProcessor.from_pretrained(model_id)
            self.pipe = pipeline(
                "automatic-speech-recognition",
                model=self.model,
                tokenizer=self.processor.tokenizer,
                feature_extractor=self.processor.feature_extractor,
                torch_dtype=torch_dtype,
                device=device,
            )
        except Exception as e:
            logger.error(f"Fehler beim Initialisieren der Modell-Pipeline: {e}")
            raise

model_pipeline = ModelPipeline(model_id, device, torch_dtype)

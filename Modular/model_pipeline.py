from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
from config import device, torch_dtype, model_id
import torch

class ModelPipeline:
    """
    Eine Klasse zur Erstellung und Initialisierung einer Modellpipeline für automatische Spracherkennung.

    Attributes:
        model (AutoModelForSpeechSeq2Seq): Das vortrainierte Modell für Speech-to-Text.
        processor (AutoProcessor): Der Prozessor für das Modell, der Tokenizer und Feature-Extraktor enthält.
        pipe (pipeline): Die Transformers-Pipeline für automatische Spracherkennung.
    """

    def __init__(self, model_id: str, device: str, torch_dtype: torch.dtype):
        """
        Initialisiert die Modellpipeline für automatische Spracherkennung.

        Args:
            model_id (str): Die ID des vortrainierten Modells.
            device (str): Das Gerät, auf dem das Modell ausgeführt wird (z. B. "cuda:0" oder "cpu").
            torch_dtype (torch.dtype): Der Datentyp für die Berechnungen (z. B. torch.float16 oder torch.float32).
        """
        # Laden des vortrainierten Modells mit reduzierter Speichernutzung und safetensors.
        self.model = AutoModelForSpeechSeq2Seq.from_pretrained(
            model_id, 
            torch_dtype=torch_dtype, 
            low_cpu_mem_usage=True, 
            use_safetensors=True
        )
        # Verschieben des Modells auf das angegebene Gerät (GPU oder CPU).
        self.model.to(device)

        # Laden des Prozessors, der Tokenizer und Feature-Extraktor enthält.
        self.processor = AutoProcessor.from_pretrained(model_id)

        # Initialisieren der Transformers-Pipeline für automatische Spracherkennung.
        self.pipe = pipeline(
            "automatic-speech-recognition",  # Task: Spracherkennung.
            model=self.model,                # Das vortrainierte Modell.
            tokenizer=self.processor.tokenizer,  # Der Tokenizer des Prozessors.
            feature_extractor=self.processor.feature_extractor,  # Der Feature-Extraktor.
            torch_dtype=torch_dtype,         # Datentyp für die Berechnungen.
            device=device                    # Gerät, auf dem die Berechnungen ausgeführt werden.
        )

# Instanziierung der Modellpipeline mit den konfigurierten Parametern.
model_pipeline = ModelPipeline(model_id, device, torch_dtype)

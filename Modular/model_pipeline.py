from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
from config import device, torch_dtype, model_id
import torch

class ModelPipeline:
    def __init__(self, model_id: str, device: str, torch_dtype: torch.dtype):
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

model_pipeline = ModelPipeline(model_id, device, torch_dtype)

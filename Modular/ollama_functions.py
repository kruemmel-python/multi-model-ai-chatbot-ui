import subprocess
import re
from typing import Generator, Optional, Tuple
import gradio as gr
from PyPDF2 import PdfReader
from helpers import format_chat_message
from config import OLLAMA_MODELS, DEFAULT_OLLAMA_MODEL, STATUS_MESSAGE_GENERATING, STATUS_MESSAGE_COMPLETE, STATUS_MESSAGE_ERROR
from audio_processing import process_audio

class OllamaFunctions:
    def __init__(self):
        pass

    def clean_output(self, output: str) -> str:
        """Entfernt Steuerzeichen aus der Ollama-Ausgabe."""
        cleaned_output = re.sub(r'(?:\x1B[@-_]|[\x1B\x9B][0-?]*[ -/]*[@-~])', '', output)
        cleaned_output = re.sub(r'\?\d+[lh]', '', cleaned_output)
        cleaned_output = re.sub(r'[\u2800-\u28FF]', '', cleaned_output)
        cleaned_output = re.sub(r'\r', '', cleaned_output)
        cleaned_output = re.sub(r'2K1G ?(?:2K1G)*!?', '', cleaned_output)
        return cleaned_output

    def format_as_codeblock(self, output: str) -> str:
        """Formatiert die Ausgabe als Markdown-Codeblock."""
        return f"```\n{output}\n```"

    def run_ollama_live(self, prompt: str, model: str) -> Generator[str, None, None]:
        """Führt Ollama aus und gibt die Ausgabe live zurück."""
        try:
            process = subprocess.Popen(
                ["ollama", "run", model],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1,
                encoding='utf-8',
            )
            process.stdin.write(prompt + "\n")
            process.stdin.close()

            buffer = ""
            for line in iter(process.stdout.readline, ''):
                clean_line = self.clean_output(line)
                if clean_line:
                    buffer += clean_line + "\n"
                    yield self.format_as_codeblock(buffer)

            process.stdout.close()
            process.wait()

        except Exception as e:
            yield f"**Fehler:** {str(e)}"

    def process_uploaded_file(self, file: gr.File) -> str:
        """Verarbeitet hochgeladene TXT- und PDF-Dateien."""
        if file.name.endswith(".txt"):
            with open(file.name, 'r', encoding='utf-8') as f:
                return f.read()
        elif file.name.endswith(".pdf"):
            try:
                reader = PdfReader(file.name)
                content = ""
                for page in reader.pages:
                    content += page.extract_text()
                return content
            except Exception as e:
                raise ValueError(f"Fehler beim Lesen der PDF-Datei: {e}")
        else:
            raise ValueError("Nur TXT- und PDF-Dateien werden unterstützt.")

    def chatbot_interface(self, input_text: str, model: str, file: Optional[gr.File], audio_file: Optional[gr.File] = None) -> Generator[Tuple[str, str], None, None]:
        """Schnittstelle für die Ollama-Chatbot-Funktion."""
        yield "", STATUS_MESSAGE_GENERATING

        if file:
            try:
                input_text = self.process_uploaded_file(file)
            except ValueError as e:
                yield f"**Fehler:** {str(e)}", STATUS_MESSAGE_ERROR
                return
            except Exception as e:
                yield f"**Unerwarteter Fehler:** {str(e)}", STATUS_MESSAGE_ERROR
                return

        if audio_file:
            try:
                input_text = process_audio(audio_file)  # Übergibt den Dateipfad direkt
            except Exception as e:
                yield f"**Fehler bei der Verarbeitung der Audiodatei:** {str(e)}", STATUS_MESSAGE_ERROR
                return

        try:
            for chunk in self.run_ollama_live(input_text, model):
                yield chunk, STATUS_MESSAGE_GENERATING
            yield chunk, STATUS_MESSAGE_COMPLETE
        except Exception as e:
            yield f"**Fehler bei der Kommunikation mit Ollama:** {str(e)}", STATUS_MESSAGE_ERROR

ollama_functions = OllamaFunctions()

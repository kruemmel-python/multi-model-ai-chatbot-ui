import subprocess
import re
from typing import Generator, Optional, Tuple
import gradio as gr
from PyPDF2 import PdfReader
from helpers import format_chat_message
from config import OLLAMA_MODELS, DEFAULT_OLLAMA_MODEL, STATUS_MESSAGE_GENERATING, STATUS_MESSAGE_COMPLETE, STATUS_MESSAGE_ERROR
from audio_processing import process_audio
import difflib

class OllamaFunctions:
    """
    Eine Klasse zur Verwaltung und Nutzung von Ollama-Funktionen, einschließlich Verarbeitung
    von Dokumenten, Audiodateien und Live-Kommunikation mit dem Ollama-Modell.
    """

    def __init__(self):
        """Initialisiert eine Instanz der OllamaFunctions-Klasse."""
        pass

    def clean_output(self, output: str) -> str:
        """
        Entfernt Steuerzeichen und unnötige Inhalte aus der Ausgabe von Ollama.

        Args:
            output (str): Die ursprüngliche Ausgabe.

        Returns:
            str: Die bereinigte Ausgabe.
        """
        cleaned_output = re.sub(r'(?:\x1B[@-_]|[\x1B\x9B][0-?]*[ -/]*[@-~])', '', output)
        cleaned_output = re.sub(r'\?\d+[lh]', '', cleaned_output)
        cleaned_output = re.sub(r'[\u2800-\u28FF]', '', cleaned_output)
        cleaned_output = re.sub(r'\r', '', cleaned_output)
        cleaned_output = re.sub(r'2K1G ?(?:2K1G)*!?', '', cleaned_output)
        return cleaned_output

    def format_as_codeblock(self, output: str) -> str:
        """
        Formatiert die Ausgabe als Markdown-Codeblock.

        Args:
            output (str): Der Text, der formatiert werden soll.

        Returns:
            str: Der Text als Markdown-Codeblock.
        """
        return f"```\n{output}\n```"

    def format_output(self, output: str) -> str:
        """
        Formatiert die Ausgabe mit Zeilenumbrüchen und erkennt Codeblöcke.

        Args:
            output (str): Die ursprüngliche Ausgabe.

        Returns:
            str: Die formatierte Ausgabe.
        """
        output = re.sub(r'\s+', ' ', output)  # Reduziert Mehrfach-Leerzeichen.
        output = re.sub(r'(.{80,}?)(\s+|$)', r'\1\n', output)  # Fügt Zeilenumbrüche ein.
        code_blocks = re.findall(r'```(.*?)```', output, re.DOTALL)
        for block in code_blocks:
            formatted_block = self.format_as_codeblock(block.strip())
            output = output.replace(f'```{block}```', formatted_block)
        return output

    def run_ollama_live(self, prompt: str, model: str) -> Generator[str, None, None]:
        """
        Führt das Ollama-Modell aus und streamt die Ausgabe in Echtzeit.

        Args:
            prompt (str): Der Eingabetext für das Modell.
            model (str): Der Name des Ollama-Modells.

        Yields:
            str: Die gestreamte Ausgabe des Modells.
        """
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
                    yield self.format_output(buffer)

            process.stdout.close()
            process.wait()
        except Exception as e:
            yield f"**Fehler:** {str(e)}"

    def process_uploaded_file(self, file: gr.File) -> str:
        """
        Verarbeitet eine hochgeladene Datei (TXT oder PDF).

        Args:
            file (gr.File): Die hochgeladene Datei.

        Returns:
            str: Der Inhalt der Datei als Text.

        Raises:
            ValueError: Wenn die Datei nicht unterstützt wird oder Fehler auftreten.
        """
        if file.name.endswith(".txt"):
            with open(file.name, 'r', encoding='utf-8') as f:
                return f.read()
        elif file.name.endswith(".pdf"):
            try:
                reader = PdfReader(file.name)
                content = "".join(page.extract_text() for page in reader.pages)
                return content
            except Exception as e:
                raise ValueError(f"Fehler beim Lesen der PDF-Datei: {e}")
        else:
            raise ValueError("Nur TXT- und PDF-Dateien werden unterstützt.")

    def compare_documents(self, file1: gr.File, file2: gr.File) -> str:
        """
        Vergleicht den Inhalt zweier hochgeladener Dokumente.

        Args:
            file1 (gr.File): Das erste Dokument.
            file2 (gr.File): Das zweite Dokument.

        Returns:
            str: Unterschiede zwischen den Dokumenten als formatierter Codeblock.
        """
        try:
            content1 = self.process_uploaded_file(file1)
            content2 = self.process_uploaded_file(file2)
            diff = difflib.unified_diff(
                content1.splitlines(),
                content2.splitlines(),
                fromfile='File1',
                tofile='File2',
                lineterm=''
            )
            return self.format_as_codeblock('\n'.join(diff))
        except ValueError as e:
            return f"**Fehler:** {str(e)}"
        except Exception as e:
            return f"**Unerwarteter Fehler:** {str(e)}"

    def chatbot_interface(
        self, 
        input_text: str, 
        model: str, 
        file1: Optional[gr.File] = None, 
        file2: Optional[gr.File] = None, 
        audio_file: Optional[gr.File] = None
    ) -> Generator[Tuple[str, str], None, None]:
        """
        Schnittstelle für den Ollama-Chatbot mit Unterstützung für Text, Dateien und Audiodateien.

        Args:
            input_text (str): Der Texteingabe des Benutzers.
            model (str): Das Ollama-Modell.
            file1 (Optional[gr.File]): Die erste hochgeladene Datei (optional).
            file2 (Optional[gr.File]): Die zweite hochgeladene Datei (optional).
            audio_file (Optional[gr.File]): Eine hochgeladene Audiodatei (optional).

        Yields:
            Tuple[str, str]: Status und generierte Antworten.
        """
        yield "", STATUS_MESSAGE_GENERATING

        if file1 and file2:
            try:
                content1 = self.process_uploaded_file(file1)
                content2 = self.process_uploaded_file(file2)
                combined_input = f"{input_text}\n\nVergleichen Sie die folgenden beiden Dokumente:\n\nDokument 1:\n{content1}\n\nDokument 2:\n{content2}"
            except ValueError as e:
                yield f"**Fehler:** {str(e)}", STATUS_MESSAGE_ERROR
                return
            except Exception as e:
                yield f"**Unerwarteter Fehler:** {str(e)}", STATUS_MESSAGE_ERROR
                return
        elif file1 or file2:
            try:
                content = self.process_uploaded_file(file1 or file2)
                combined_input = f"{input_text}\n\nInhalt des Dokuments:\n{content}"
            except ValueError as e:
                yield f"**Fehler:** {str(e)}", STATUS_MESSAGE_ERROR
                return
            except Exception as e:
                yield f"**Unerwarteter Fehler:** {str(e)}", STATUS_MESSAGE_ERROR
                return
        elif audio_file:
            try:
                audio_content = process_audio(audio_file)
                combined_input = f"{input_text}\n\nInhalt der Audiodatei:\n{audio_content}"
            except Exception as e:
                yield f"**Fehler bei der Verarbeitung der Audiodatei:** {str(e)}", STATUS_MESSAGE_ERROR
                return
        else:
            combined_input = input_text

        try:
            for chunk in self.run_ollama_live(combined_input, model):
                yield chunk, STATUS_MESSAGE_GENERATING
            yield chunk, STATUS_MESSAGE_COMPLETE
        except Exception as e:
            yield f"**Fehler bei der Kommunikation mit Ollama:** {str(e)}", STATUS_MESSAGE_ERROR

# Instanziierung eines OllamaFunctions-Objekts.
ollama_functions = OllamaFunctions()

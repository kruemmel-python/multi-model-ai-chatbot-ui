import gradio as gr
from PyPDF2 import PdfReader
import logging

# Logger einrichten
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class FComponent:
    def __init__(self):
        self.component = gr.File(
            label="Datei hochladen",
            file_types=[".txt", ".md", ".py", ".cpp", ".h", ".c", ".java",
                        ".js", ".cs", ".go", ".html", ".css", ".json",
                        ".xml", ".yaml", ".sh", ".pdf"],
            type="filepath"  # Korrektur des Typs auf 'filepath'
        )


    def get_config(self):
        return {
            "label": self.component.label,
            "type": "file",
            "file_types": self.component.file_types
        }

    def accept_file_types(self, file_types):
        """Überprüft, ob die angegebenen Dateitypen zulässig sind."""
        return all(file_type in self.get_config()["file_types"] for file_type in file_types)

    def preprocess(self, file):
        """Verarbeitung der hochgeladenen Datei."""
        if file.name.endswith(".txt"):
            return self._read_text_file(file.name)
        elif file.name.endswith(".pdf"):
            return self._read_pdf_file(file.name)
        elif file.name.endswith((".py", ".cpp", ".h", ".c", ".java", ".js", ".cs", ".go",
                                ".html", ".css", ".md", ".json", ".xml", ".yaml", ".sh")):
            return self._read_text_file(file.name)
        else:
            raise ValueError("Nur TXT-, PDF- und andere textbasierte Dateien werden unterstützt.")

    def _read_text_file(self, filename):
        """Liest eine Textdatei und gibt den Inhalt zurück."""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            logger.error(f"Fehler beim Lesen der Datei: {e}")
            raise ValueError(f"Fehler beim Lesen der Datei: {e}")

    def _read_pdf_file(self, filename):
        """Liest eine PDF-Datei und extrahiert Text."""
        try:
            reader = PdfReader(filename)
            content = ""
            for page in reader.pages:
                content += page.extract_text() or ""
            return content
        except Exception as e:
            logger.error(f"Fehler beim Lesen der PDF-Datei: {e}")
            raise ValueError(f"Fehler beim Lesen der PDF-Datei: {e}")

    def postprocess(self, file):
        """Hier könnten zusätzliche Verarbeitungsschritte hinzugefügt werden."""
        pass



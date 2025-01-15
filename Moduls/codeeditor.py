import os
import sys
import logging
import gradio as gr
import google.generativeai as genai
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
from dotenv import load_dotenv
from functools import lru_cache
from black import format_str, FileMode
from typing import Optional
from logging_config import setup_logging

# Setup Logging
setup_logging()

# Load environment variables from .env file
load_dotenv()

# Gemini API Key Setup
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    logger.error("GEMINI_API_KEY ist nicht als Umgebungsvariable gesetzt.")
    sys.exit(1)

# Setup API
def setup_api(gemini_api_key: str) -> Optional[genai.GenerativeModel]:
    """
    Konfiguriert die Gemini API mit dem bereitgestellten API-Schlüssel.
    """
    try:
        if not gemini_api_key:
            raise ValueError("GEMINI_API_KEY ist ungültig oder leer.")

        genai.configure(api_key=gemini_api_key)
        model = genai.GenerativeModel('gemini-pro')
        logger.info("Gemini API configured successfully.")
        return model
    except Exception as e:
        logger.error(f"Fehler beim Konfigurieren der Gemini API: {e}")
        sys.exit(1)

# Configure Gemini API
model = setup_api(GEMINI_API_KEY)

# Helper functions
def format_code(code_input: str) -> str:
    """
    Formatiert den gegebenen Python-Code mit Pygments.
    """
    try:
        formatter = HtmlFormatter(style='colorful')
        highlighted_code = highlight(code_input, PythonLexer(), formatter)
        return highlighted_code
    except Exception as e:
        logger.error(f"Fehler beim Formatieren des Codes: {e}")
        return f"<pre>{code_input}</pre>"

def save_code(code_input: str, filename: str) -> None:
    """
    Speichert den gegebenen Code in einer Datei.
    """
    with open(filename, 'w') as file:
        file.write(code_input)

def load_code(filename: str) -> str:
    """
    Lädt den Code aus einer Datei.
    """
    with open(filename, 'r') as file:
        return file.read()

def format_code_with_black(code_input: str) -> str:
    """
    Formatiert den gegebenen Code mit Black.
    """
    try:
        formatted_code = format_str(code_input, mode=FileMode())
        return formatted_code
    except Exception as e:
        logger.error(f"Fehler beim Formatieren des Codes mit black: {e}")
        return code_input

# Gemini Functionality
class GeminiFunctions:
    """
    Klasse zur Verwaltung der Gemini API-Funktionalitäten.
    """

    def __init__(self, model: genai.GenerativeModel):
        """
        Initialisiert die GeminiFunctions mit dem angegebenen Modell.
        """
        self.model = model

    @lru_cache(maxsize=100)
    def analyze_code(self, code_input: str) -> str:
        """
        Analysiert den gegebenen Python-Code und gibt Feedback.
        """
        try:
            prompt = f"Analysiere diesen Python-Code und gib Feedback:\n\n{code_input}\n\nAntworte auf Deutsch und mit Zeilenumbrüchen."
            response = self.model.generate_content(prompt)
            return response.text if response is not None else "Fehler während der Analyse."
        except Exception as e:
            logger.error(f"Fehler während der Analyse: {e}")
            return str(e)

    @lru_cache(maxsize=100)
    def suggest_code_improvements(self, code_input: str) -> str:
        """
        Schlägt Verbesserungen für den gegebenen Python-Code vor.
        """
        try:
            prompt = f"Schlage Verbesserungen für diesen Python-Code vor:\n\n{code_input}\n\nAntworte auf Deutsch und mit Zeilenumbrüchen."
            response = self.model.generate_content(prompt)
            return response.text if response is not None else "Fehler während der Generierung von Vorschlägen."
        except Exception as e:
            logger.error(f"Fehler während der Generierung von Vorschlägen: {e}")
            return str(e)

def update_model(model_name: str) -> None:
    """
    Aktualisiert das Gemini-Modell basierend auf der Auswahl.
    """
    global model
    model = setup_api(GEMINI_API_KEY)
    model.model_name = model_name

gemini_functions = GeminiFunctions(model)

# Gradio UI
def create_app() -> gr.Blocks:
    """
    Erstellt die Gradio-Benutzeroberfläche.
    """
    with gr.Blocks(css="style.css") as app:
        gr.Markdown("""
        <h1>Code Analyzer & Generator mit Gemini AI</h1>
        """, elem_classes="markdown-text")

        # Input Code Editor
        code_input = gr.Code(label="Code Eingabe", language="python", lines=10, elem_classes="code-output")

        # Buttons
        with gr.Row():
            analyze_button = gr.Button("Code analysieren", variant="primary", elem_classes="button-font")
            suggest_button = gr.Button("Vorschläge generieren", variant="secondary", elem_classes="button-font")

        # Outputs
        analysis_output = gr.Code(label="Analyse", language="python", lines=10, elem_classes="code-output")
        suggestions_output = gr.Code(label="Vorschläge", language="python", lines=10, elem_classes="code-output")

        # Button Click Events
        analyze_button.click(fn=gemini_functions.analyze_code, inputs=code_input, outputs=analysis_output)
        suggest_button.click(fn=gemini_functions.suggest_code_improvements, inputs=code_input, outputs=suggestions_output)

        # Save and Load Code
        save_button = gr.Button("Code speichern", variant="primary", elem_classes="button-font")
        load_button = gr.Button("Code laden", variant="secondary", elem_classes="button-font")
        filename_input = gr.Textbox(label="Dateiname", placeholder="Geben Sie den Dateinamen ein", elem_classes="code-output")

        save_button.click(fn=save_code, inputs=[code_input, filename_input])
        load_button.click(fn=load_code, inputs=filename_input, outputs=code_input)

        # Model Selection
        model_selection = gr.Dropdown(choices=["gemini-pro", "gemini-lite"], label="Gemini Modell", value="gemini-pro", elem_classes="code-output")
        model_selection.change(fn=update_model, inputs=model_selection)

        # Format Code with Black
        format_button = gr.Button("Code mit black formatieren", variant="secondary", elem_classes="button-font")
        format_button.click(fn=format_code_with_black, inputs=code_input, outputs=code_input)

    return app

# Run the App
if __name__ == "__main__":
    app = create_app()
    app.launch(share=True, server_name="localhost", server_port=9560)
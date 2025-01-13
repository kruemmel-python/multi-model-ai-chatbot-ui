# Mitral API GRADIO

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Dieses Projekt ist eine modularisierte Anwendung, die verschiedene Funktionen für die Verarbeitung und Analyse von Bildern, Audiodateien und Texten bietet. Die Anwendung verwendet [Gradio](https://gradio.app/) für die Benutzeroberfläche und integriert verschiedene KI-Modelle für die Verarbeitung.

## Inhalt

- [Installation](#installation)
- [Module](#module)
    - [config](#config)
    - [model_pipeline](#model_pipeline)
    - [api_client](#api_client)
    - [helpers](#helpers)
    - [audio_processing](#audio_processing)
    - [file_creator](#file_creator)
    - [mistral_functions](#mistral_functions)
    - [gemini_functions](#gemini_functions)
    - [chat_manager](#chat_manager)
    - [ollama_functions](#ollama_functions)
    - [gradio_interface](#gradio_interface)
- [Verwendung](#verwendung)
- [Lizenz](#lizenz)

## Installation

Um das Projekt zu installieren, klonen Sie das Repository und installieren Sie die erforderlichen Abhängigkeiten:

```bash
git clone https://github.com/kruemmel-python/multi-model-ai-chatbot-ui.git
cd Mitral-API-GRADIO
pip install -r requirements.txt
```

## Module

### `config`

Das `config`-Modul enthält Konfigurationsparameter und Umgebungsvariablen für das Projekt. Es definiert API-Schlüssel, Modell-IDs und andere wichtige Konfigurationen, die für die Ausführung der Anwendung notwendig sind.

### `model_pipeline`

Das `model_pipeline`-Modul initialisiert und verwaltet die Modell-Pipeline für die Verarbeitung von Audiodateien. Es verwendet die [transformers](https://huggingface.co/docs/transformers/index)-Bibliothek, um Modelle zu laden und zu verwenden.

### `api_client`

Das `api_client`-Modul verwaltet die API-Clients für die Interaktion mit verschiedenen KI-Modellen wie Mistral und Gemini. Es stellt Funktionen bereit, um Anfragen an die APIs zu senden und Antworten zu verarbeiten.

### `helpers`

Das `helpers`-Modul enthält Hilfsfunktionen, die in verschiedenen Teilen des Projekts verwendet werden. Es bietet Funktionen zum Kodieren von Bildern und Formatieren von Chatnachrichten.

### `audio_processing`

Das `audio_processing`-Modul verarbeitet Audiodateien und extrahiert Text aus Audiodateien. Es verwendet die [pydub](https://github.com/jiaaro/pydub)-Bibliothek, um Audiodateien zu konvertieren und zu verarbeiten.

### `file_creator`

Das `file_creator`-Modul erstellt verschiedene Dateiformate (Excel, Word, PDF, PowerPoint, CSV) basierend auf von KI generiertem Inhalt. Es verwendet Bibliotheken wie [openpyxl](https://openpyxl.readthedocs.io/en/stable/), [docx](https://python-docx.readthedocs.io/en/latest/), [fpdf](https://pyfpdf.github.io/fpdf2/), [pptx](https://python-pptx.readthedocs.io/en/latest/) und `csv`.

### `mistral_functions`

Das `mistral_functions`-Modul enthält Funktionen, die spezifisch für die Interaktion mit dem Mistral-Modell sind. Es bietet Funktionen zum Chatten, Analysieren von Bildern und Vergleichen von Bildern.

### `gemini_functions`

Das `gemini_functions`-Modul enthält Funktionen, die spezifisch für die Interaktion mit dem Gemini-Modell sind. Es bietet Funktionen zum Chatten und Analysieren von Bildern.

### `chat_manager`

Das `chat_manager`-Modul verwaltet den Chatverlauf, einschließlich Speichern, Laden, Löschen und Erstellen neuer Chats. Es speichert den Chatverlauf in einer JSON-Datei.

### `ollama_functions`

Das `ollama_functions`-Modul enthält Funktionen, die spezifisch für die Interaktion mit dem Ollama-Modell sind. Es bietet Funktionen zum Chatten und Verarbeiten von hochgeladenen Dateien.

### `gradio_interface`

Das `gradio_interface`-Modul definiert die Benutzeroberfläche der Anwendung mit Gradio. Es integriert alle oben genannten Module und stellt eine benutzerfreundliche Oberfläche für die Interaktion mit den verschiedenen Funktionen bereit.

## Verwendung

Um die Anwendung zu starten, führen Sie das folgende Kommando aus:

```bash
python gradio_interface.py
```

Die Anwendung wird auf `localhost` auf Port `8779` gestartet. Sie können die Anwendung im Browser unter [http://localhost:8779](http://localhost:8779) aufrufen.

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert. Weitere Informationen finden Sie in der [LICENSE](LICENSE) Datei.


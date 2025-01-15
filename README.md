
# Multi-Model AI Chatbot UI

## Beschreibung
Multi-Model AI Chatbot UI ist eine innovative Benutzeroberfläche, die mehrere KI-Modelle integriert, darunter Mistral, Gemini und Ollama. Mit Funktionen zur Bild- und Audioanalyse sowie zur Dateierstellung bietet diese Anwendung eine multimodale und interaktive Plattform für die Erstellung und Verwaltung von KI-generierten Inhalten.

**GitHub Repository:** [Multi-Model AI Chatbot UI](https://github.com/kruemmel-python/multi-model-ai-chatbot-ui)

## Features
* **Integration mehrerer KI-Modelle:** Unterstützung für Mistral, Gemini und Ollama.
* **Multimodale Eingaben:** Verarbeiten von Text, Bildern und Audiodateien.
* **Interaktive Benutzeroberfläche:** Einfach zu bedienendes Gradio-Interface.
* **Fortschrittliche Bild- und Audioanalyse:** Nutzung von Modellen wie OpenAI Whisper.
* **Dateierstellung:** Erstellung von Excel-, Word-, PDF-, PowerPoint- und CSV-Dateien.
* **Code-Editor:** Echtzeit-Codeanalyse und Verbesserungsvorschläge mit Gemini.
* **Gespeicherte Chats:** Speicherung und Wiederherstellung von Chatverläufen.
* **Automatische Modellkonfiguration:** Anpassung von Modellen an spezifische Aufgaben.

## Installation

### Voraussetzungen
* Python 3.12 oder höher
* Paketmanager: pip
* Virtuelle Umgebung (empfohlen): virtualenv

### Schritte
1. **Repository klonen:**
    ```bash
    git clone https://github.com/kruemmel-python/multi-model-ai-chatbot-ui.git
    cd multi-model-ai-chatbot-ui
    ```

2. **Virtuelle Umgebung erstellen:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Für Linux/MacOS
    venv\Scripts\activate   # Für Windows
    ```

3. **Abhängigkeiten installieren:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Umgebungsvariablen konfigurieren:**
    * Erstelle eine `.env`-Datei im Projektverzeichnis.
    * Füge folgende Schlüssel hinzu:
        ```env
        GEMINI_API_KEY=dein_gemini_api_schlüssel
        MISTRAL_API_KEY=dein_mistral_api_schlüssel
        ```

5. **Anwendung starten:**
    ```bash
    python gradio_interface.py
    ```

6. **Zugriff auf die Anwendung:**
    Öffne deinen Browser und navigiere zu `http://localhost:3379`.

## Verwendung
### Hauptfunktionen
* **Chatbot-Interaktionen:**
    * Wähle ein Modell (Mistral, Gemini, Ollama) aus.
    * Eingabe über Textfeld, Bild oder Audio.
* **Dateierstellung:**
    * Wähle das gewünschte Format (Excel, Word, PDF, PowerPoint, CSV).
    * Gib den gewünschten Inhalt ein.
    * Lade die generierte Datei herunter.
* **Code-Editor:**
    * Analysiere Python-Code in Echtzeit.
    * Erhalte Verbesserungsvorschläge.
    * Speichere und lade deinen Code direkt in der Benutzeroberfläche.
* **Bild- und Audioanalyse:**
    * Lade Bilder hoch, um eine kreative Beschreibung zu erhalten.
    * Extrahiere Text aus Audiodateien mit dem eingebauten Whisper-Modell.

## Technologien
* **Programmiersprachen:** Python 3.12
* **Frameworks und Bibliotheken:**
    * Gradio (Benutzeroberfläche)
    * Transformers (Modelle und Pipelines)
    * OpenAI Whisper (Audioanalyse)
    * Pydub, FPDF, OpenPyXL (Dateiverarbeitung)
    * Loguru, Unittest (Logging und Tests)

## Contributing
Beiträge sind willkommen! Bitte folge diesen Schritten, um mitzuwirken:

1. Forke das Repository.
2. Erstelle einen neuen Branch:
   ```bash
   git checkout -b feature/dein-feature
   ```
3. Committe deine Änderungen:
   ```bash
   git commit -m "Dein Kommentar"
   ```
4. Push den Branch:
    ```bash
    git push origin feature/dein-feature
    ```
5. Erstelle einen Pull-Request.

## Lizenz
Dieses Projekt ist unter der MIT-Lizenz lizenziert. Weitere Details findest du in der [LICENSE](LICENSE) Datei.

## Autor
Ralf Krümmel
[GitHub-Profil](https://github.com/kruemmel-python)

Bei Fragen oder Anmerkungen, zögere nicht, mich zu kontaktieren!

## Codestruktur
* **`api_client.py`**: Diese Datei enthält die `APIClient`-Klasse, die die API-Clients für Mistral und Gemini verwaltet.
* **`audio_processing.py`**: Diese Datei enthält die Funktion `process_audio`, die Audiodateien verarbeitet und Text extrahiert.
* **`chat_manager.py`**: Diese Datei enthält die `ChatManager`-Klasse, die Methoden zur Verwaltung von Chatverläufen bietet.
* **`codeeditor.py`**: Diese Datei enthält die Funktionen zur Analyse und Verbesserung von Python-Code sowie die Gradio-Benutzeroberfläche für den Code-Editor.
* **`config.py`**: Diese Datei enthält Konfigurationsparameter und API-Schlüssel.
* **`file_creator.py`**: Diese Datei enthält die `FileCreator`-Klasse, die Methoden zur Erstellung von Dateien mit KI-generierten Inhalten bietet.
* **`gemini_functions.py`**: Diese Datei enthält die `GeminiFunctions`-Klasse, die Methoden zur Verwaltung der Gemini-API-Funktionalitäten bietet.
* **`gradio_interface.py`**: Diese Datei enthält die Funktion `create_gradio_interface`, die die Gradio-Benutzeroberfläche erstellt.
* **`helpers.py`**: Diese Datei enthält Hilfsfunktionen wie `encode_image` und `format_chat_message`.
* **`logging_config.py`**: Diese Datei enthält die Funktion `setup_logging`, die das Logging für die Anwendung konfiguriert.
* **`mistral_functions.py`**: Diese Datei enthält die `MistralFunctions`-Klasse, die Methoden zur Verwaltung der Mistral-Funktionalitäten bietet.
* **`model_pipeline.py`**: Diese Datei enthält die `ModelPipeline`-Klasse, die die Modell-Pipeline für die Spracherkennung verwaltet.
* **`ollama_functions.py`**: Diese Datei enthält die `OllamaFunctions`-Klasse, die Methoden zur Verwaltung der Ollama-Funktionalitäten bietet.
* **`test_audio_processing.py`**: Diese Datei enthält Unit-Tests für die Funktion `process_audio`.
* **`test_chat_manager.py`**: Diese Datei enthält Unit-Tests für die `ChatManager`-Klasse.
* **`test_gemini_functions.py`**: Diese Datei enthält Unit-Tests für die `GeminiFunctions`-Klasse.
* **`test_mistral_functions.py`**: Diese Datei enthält Unit-Tests für die `MistralFunctions`-Klasse.
* **`test_ollama_functions.py`**: Diese Datei enthält Unit-Tests für die `OllamaFunctions`-Klasse.
```

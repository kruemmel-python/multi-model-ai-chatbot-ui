# Multi-Model AI Chatbot UI

[![GitHub Issues](https://img.shields.io/github/issues/kruemmel-python/multi-model-ai-chatbot-ui)](https://github.com/kruemmel-python/multi-model-ai-chatbot-ui/issues)
[![GitHub Pull Requests](https://img.shields.io/github/pulls/kruemmel-python/multi-model-ai-chatbot-ui)](https://github.com/kruemmel-python/multi-model-ai-chatbot-ui/pulls)
[![License](https://img.shields.io/github/license/kruemmel-python/multi-model-ai-chatbot-ui)](https://github.com/kruemmel-python/multi-model-ai-chatbot-ui/blob/main/LICENSE)

Dieses Repository enthält eine umfassende Benutzeroberfläche für Chatbots, die mehrere KI-Modelle integriert, darunter Mistral, Gemini und Ollama. Die Anwendung unterstützt sowohl textbasierte Interaktionen als auch die Verarbeitung von Audio- und Bilddateien. Zusätzlich bietet sie Funktionen zur Dateierstellung (Excel, Word, PDF, PowerPoint, CSV) und einen Code-Editor mit integrierter Analyse und Verbesserung durch KI.

## Funktionen

-   **Multi-Modell-Unterstützung:** Integriert Mistral, Gemini und Ollama für vielseitige Chatbot-Funktionen.
-   **Audioverarbeitung:** Transkribiert Audioeingaben mit Whisper und nutzt die transkribierten Texte für die Chatinteraktion.
-   **Bildanalyse:** Analysiert und beschreibt Bilder mit Mistral und Gemini.
-   **Chatverlauf:** Speichert und lädt Chatverläufe für jede KI-Modellinstanz.
-   **Dateierstellung:** Generiert Excel-, Word-, PDF-, PowerPoint- und CSV-Dateien basierend auf Benutzeranfragen.
-   **Code-Editor:** Bietet eine Benutzeroberfläche zum Bearbeiten, Analysieren und Formatieren von Python-Code.
-   **Gradio-UI:** Erstellt eine intuitive und interaktive Benutzeroberfläche mit Gradio.
-   **Umfassendes Logging:** Nutzt `loguru` und `logging` für detaillierte Fehlerprotokolle und Debugging.
-   **Dokumentenvergleich:** Möglichkeit, zwei Dokumente (TXT oder PDF) zu vergleichen und die Unterschiede anzuzeigen.
-   **Code-Formatierung:** Integration mit `black` zur automatischen Formatierung von Python-Code.
-   **Live-Streaming:** Bietet eine Live-Streaming-Funktionalität für Ollama-Antworten.

## Installation

1.  **Repository klonen:**

    ```bash
    git clone https://github.com/kruemmel-python/multi-model-ai-chatbot-ui.git
    cd multi-model-ai-chatbot-ui
    ```

2.  **Virtuelle Umgebung erstellen (empfohlen):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # Auf Linux/macOS
    venv\Scripts\activate  # Auf Windows
    ```

3.  **Abhängigkeiten installieren:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **API-Schlüssel einrichten:**
    - Erstelle eine `.env` Datei im Hauptverzeichnis.
    - Füge deine API-Schlüssel hinzu:

    ```env
    MISTRAL_API_KEY=dein_mistral_api_key
    GEMINI_API_KEY=dein_gemini_api_key
    ```
   - Falls Sie einen Ollama Server auf einem anderen Rechner betreiben, muss in der Datei `ollama_functions.py` in Zeile 13, die Variable `subprocess.Popen` angepasst werden, z.B.:
```python
            process = subprocess.Popen(
                ["ssh", "benutzername@ip-des-servers", "ollama", "run", model],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1,
                encoding='utf-8',
            )
```
    - Anstelle von `benutzername@ip-des-servers` muss Ihre tatsächliche Benutzername und die IP Adresse des Servers eingesetzt werden.
    - Dies ist Optional!

## Verwendung

1.  **Anwendung starten:**

    ```bash
    python gradio_interface.py
    ```

2.  **Zugriff über den Browser:**
    -   Die Anwendung wird unter der angegebenen Adresse und Port (standardmäßig `http://localhost:3379`) im Browser gestartet.

## Struktur des Projekts

-   **`api_client.py`**: Definiert die Klasse `APIClient` zur Verwaltung der API-Clients für Mistral und Gemini.
-   **`audio_processing.py`**: Enthält die Funktion `process_audio` zur Verarbeitung von Audiodateien mit dem Whisper-Modell.
-   **`chat_manager.py`**: Definiert die Klasse `ChatManager` zur Verwaltung von Chat-Verläufen.
-   **`codeeditor.py`**: Implementiert den Code-Editor mit Gemini-Integration für Code-Analyse und Verbesserung.
-   **`config.py`**: Konfigurationsdatei mit API-Schlüsseln, Modelleinstellungen und Speicherorten.
-   **`file_creator.py`**: Definiert die Klasse `FileCreator` zur Erstellung von Dateien (Excel, Word, PDF, PowerPoint, CSV) mit KI-generiertem Inhalt.
-   **`gemini_functions.py`**: Implementiert die Gemini-Funktionalitäten, einschließlich Chat, Bildanalyse und Code-Analyse.
-   **`gradio_interface.py`**: Hauptdatei zur Erstellung und Ausführung der Gradio-Benutzeroberfläche.
-   **`helpers.py`**: Enthält Hilfsfunktionen wie `encode_image` und `format_chat_message`.
-   **`logging_config.py`**: Konfiguriert die Log-Einstellungen für die Anwendung.
-   **`mistral_functions.py`**: Implementiert die Mistral-Funktionalitäten, einschließlich Chat und Bildanalyse.
-   **`model_pipeline.py`**: Initialisiert die Spracherkennungspipeline mit Whisper.
-   **`ollama_functions.py`**: Implementiert die Ollama-Funktionalitäten, einschließlich Chat und Dokumentenvergleich.
-   **`requirements.txt`**: Listet alle benötigten Python-Bibliotheken auf.
-   **`test_audio_processing.py`**: Unit-Tests für die `audio_processing.py` Datei
-   **`test_chat_manager.py`**: Unit-Tests für die `chat_manager.py` Datei
-   **`test_gemini_functions.py`**: Unit-Tests für die `gemini_functions.py` Datei
-   **`test_mistral_functions.py`**: Unit-Tests für die `mistral_functions.py` Datei
-   **`test_ollama_functions.py`**: Unit-Tests für die `ollama_functions.py` Datei

## Danksagung

-   **Gradio:** Für das Erstellen der interaktiven Benutzeroberfläche.
-   **Mistral AI, Google AI, Ollama:** Für die Bereitstellung der leistungsstarken KI-Modelle.
-   **Hugging Face Transformers:** Für die Implementierung des Whisper-Modells zur Spracherkennung.

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz. Weitere Informationen finden Sie in der Datei [LICENSE](LICENSE).

## Kontakt

Für Fragen oder Feedback können Sie sich gerne an [Ralf Krümmel](https://github.com/kruemmel-python) wenden.


![image](https://github.com/user-attachments/assets/8efb3263-c088-4cf9-b149-33b74a0cfcd4)

![image](https://github.com/user-attachments/assets/e00dac56-ad51-4403-9bac-e4a848ebe491)

![image](https://github.com/user-attachments/assets/874f01a7-a795-4e66-acd3-797388dc39e2)

![image](https://github.com/user-attachments/assets/3bcb55c3-a7d7-413b-8e8f-4f0ce3958298)

![image](https://github.com/user-attachments/assets/49ec11ec-29ea-4a45-b788-14c6f208462f)






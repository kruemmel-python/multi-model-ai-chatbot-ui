# Multi-Modal AI Chatbot und Dateierstellungstool

Dieses Repository enthält ein Python-basiertes Tool mit einer Gradio-Benutzeroberfläche, das verschiedene KI-Modelle für Chat-Interaktionen, Bild- und Audioanalysen sowie die Erstellung von Dateien verwendet.
Besonderheit: Gemini Chatbot beinhaltet Websuche. Sofern man die Anweisung gibt "suche im web"
## Inhaltsverzeichnis

- [Funktionen](#funktionen)
- [Installation](#installation)
- [Verwendung](#verwendung)
    - [Mistral Chatbot](#mistral-chatbot)
    - [Gemini Chatbot](#gemini-chatbot)
    - [Ollama Chatbot](#ollama-chatbot)
    - [Dateierstellung](#dateierstellung)
- [Dateierstellung mit KI](#dateierstellung-mit-ki)
    - [Excel-Datei](#excel-datei)
    - [Word-Datei](#word-datei)
    - [PDF-Datei](#pdf-datei)
    - [PowerPoint-Datei](#powerpoint-datei)
    - [CSV-Datei](#csv-datei)
- [API-Schlüssel](#api-schlüssel)
- [Abhängigkeiten](#abhängigkeiten)
- [Beiträge](#beiträge)
- [Lizenz](#lizenz)

## Funktionen

Dieses Tool bietet folgende Funktionen:

- **Chatbots:**
    - Interaktive Chat-Schnittstelle mit verschiedenen KI-Modellen (Mistral, Gemini und Ollama).
    - Unterstützung für Text-, Bild- und Audioeingaben.
    - Speichern und Laden von Chatverläufen.
    - Löschen einzelner oder aller Chatverläufe.
- **Bildanalyse:**
    - Bildanalyse und -beschreibung mit Mistral und Gemini.
    - Bildvergleich mit Mistral.
    - Analyse von Diagrammen, Belegen und Dokumenten mit Mistral.
    - Durchführung von OCR (Optical Character Recognition) mit strukturiertem Output mit Mistral.
- **Audioanalyse:**
    - Transkription von Audio in Text mit dem Whisper-Modell.
- **Dateierstellung:**
    - Erstellung von Excel-, Word-, PDF-, PowerPoint- und CSV-Dateien basierend auf KI-generierten Inhalten.
    - Möglichkeit, die Anzahl der Tabellenblätter für Excel-Dateien anzugeben.

## Installation

1.  **Python-Umgebung einrichten:**
    - Stellen Sie sicher, dass Python 3.7 oder höher installiert ist.
    - Erstellen Sie eine virtuelle Umgebung (empfohlen):
      ```bash
      python -m venv venv
      source venv/bin/activate  # Unter Linux/Mac
      venv\Scripts\activate  # Unter Windows
      ```
2.  **Abhängigkeiten installieren:**
    - Installieren Sie die erforderlichen Python-Pakete:
      ```bash
      pip install -r requirements.txt
      ```
3.  **API-Schlüssel konfigurieren:**
    - Setzen Sie die Umgebungsvariablen `MISTRAL_API_KEY` und `GEMINI_API_KEY` mit Ihren jeweiligen API-Schlüsseln.
      - Unter Linux/Mac:
        ```bash
        export MISTRAL_API_KEY="YOUR_MISTRAL_API_KEY"
        export GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
        ```
      - Unter Windows:
        ```bash
        set MISTRAL_API_KEY="YOUR_MISTRAL_API_KEY"
        set GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
        ```
    - **Hinweis:** Wenn keine API-Schlüssel angegeben sind, werden die Standard-Schlüssel verwendet, die jedoch möglicherweise nicht zuverlässig funktionieren.

4. **Ollama installieren:**
   - Installieren und starten Sie Ollama gemäß der offiziellen Anleitung: https://ollama.com/download

5. **Ollama-Modelle herunterladen**
   - Stellen Sie sicher, dass die in `OLLAMA_MODELS` definierten Modelle heruntergeladen wurden, bevor das Script verwendet wird.
   - Beispiel: `ollama pull phi4`

## Verwendung

### Starten der Anwendung

Führen Sie das Skript aus:

```bash
python your_script_name.py
```

Eine Gradio-Oberfläche wird in Ihrem Standard-Webbrowser geöffnet.

### Mistral Chatbot

- **Chat-Verlauf:** Der Chat-Verlauf wird in einer interaktiven Chat-Schnittstelle angezeigt.
- **Nachrichten senden:** Geben Sie Ihre Nachricht in das Textfeld ein und klicken Sie auf "Senden".
- **Bilder hochladen:** Laden Sie ein Bild über den "Bild hochladen"-Bereich hoch, um das Bild zusammen mit einer Textnachricht zu senden.
- **Audio hochladen:** Laden Sie eine Audiodatei über den "Audio hochladen"-Bereich hoch, um den Text der Audio transkribieren zu lassen und zusammen mit der Nachricht zu senden.
- **Chat leeren:** Leert den aktuellen Chat-Verlauf.
- **Chat speichern:** Speichert den aktuellen Chat-Verlauf.
- **Neuen Chat starten:** Beginnt einen neuen Chat.
- **Gespeicherte Chats:** Zeigt eine Liste der gespeicherten Chats an, aus der Sie einen Chat laden oder löschen können.
- **Bildanalyse Tab:** Ermöglicht das Analysieren eines Bildes mit verschiedenen vordefinierten Anweisungen.
- **Bildvergleich Tab:** Ermöglicht den Vergleich von zwei Bildern.

### Gemini Chatbot

- **Chat-Verlauf:** Der Chat-Verlauf wird in einer interaktiven Chat-Schnittstelle angezeigt.
- **Nachrichten senden:** Geben Sie Ihre Nachricht in das Textfeld ein und klicken Sie auf "Senden".
- **Bilder hochladen:** Laden Sie ein Bild über den "Bild hochladen"-Bereich hoch, um das Bild zusammen mit einer Textnachricht zu senden.
- **Audio hochladen:** Laden Sie eine Audiodatei über den "Audio hochladen"-Bereich hoch, um den Text der Audio transkribieren zu lassen und zusammen mit der Nachricht zu senden.
- **Chat leeren:** Leert den aktuellen Chat-Verlauf.
- **Chat speichern:** Speichert den aktuellen Chat-Verlauf.
- **Neuen Chat starten:** Beginnt einen neuen Chat.
- **Gespeicherte Chats:** Zeigt eine Liste der gespeicherten Chats an, aus der Sie einen Chat laden oder löschen können.

### Ollama Chatbot

- **Eingabe:** Geben Sie Ihre Frage in das Textfeld ein oder laden Sie eine TXT- oder PDF-Datei hoch.
- **Modell auswählen:** Wählen Sie das gewünschte Ollama-Modell aus der Dropdown-Liste.
- **Datei hochladen (PDF oder TXT):** Laden Sie eine TXT- oder PDF-Datei hoch, um den Inhalt an das Modell zu übergeben.
- **Audio hochladen:** Laden Sie eine Audiodatei über den "Audio hochladen"-Bereich hoch, um den Text der Audio transkribieren zu lassen und an das Modell zu übergeben.
- **Antwort:** Die Antwort des Modells wird unter "Antwort" angezeigt.
- **Status:** Der Status der Anfrage (z.B. Generierung, Fehler) wird unter "Status" angezeigt.

### Dateierstellung

- **Dateiformat:** Wählen Sie das gewünschte Dateiformat (Excel, Word, PDF, PowerPoint oder CSV) aus der Dropdown-Liste.
- **Anzahl der Tabellenblätter (nur Excel):** Geben Sie die Anzahl der Tabellenblätter für Excel-Dateien an (Standard ist 1).
- **Inhalt der Datei:** Geben Sie den Inhalt der Datei im Textfeld an.
- **Datei erstellen:** Klicken Sie auf "Datei erstellen", um die Datei basierend auf den angegebenen Parametern zu erstellen. Die erstellte Datei wird automatisch geöffnet und kann heruntergeladen werden.

## Dateierstellung mit KI

Das Tool kann auch Dateien mit KI generierten Inhalten erstellen. Hier sind die Details für die einzelnen Dateiformate:

### Excel-Datei

- **Funktion:** Die `create_excel_with_ai` Funktion erstellt eine Excel-Datei (.xlsx) mit Inhalten, die von der Gemini-KI generiert wurden.
- **Inhalt:** Die KI generiert den Inhalt basierend auf der Eingabe des Benutzers. Die Funktion trennt die generierten Inhalte nach Zeilen (`\n`) und Spalten (`,`). Die erstellte Datei wird automatisch geöffnet.
- **Parameter:**
    - `user_prompt`: Die Eingabeaufforderung für die KI zur Inhaltsgenerierung.
    - `sheets` (optional): Die Anzahl der Tabellenblätter in der Excel-Datei (Standard ist 1).
- **Verwendung:**
    - Wählen Sie in der "Dateierstellung" den Dateityp "Excel" aus.
    - Geben Sie die Anzahl der Tabellenblätter an.
    - Geben Sie im Feld "Inhalt der Datei" den gewünschten Prompt ein.
    - Klicken Sie auf "Datei erstellen".

### Word-Datei

- **Funktion:** Die `create_word_with_ai` Funktion erstellt eine Word-Datei (.docx) mit von der Gemini-KI generierten Inhalten.
- **Inhalt:** Die KI generiert den Inhalt basierend auf der Eingabe des Benutzers. Der generierte Text wird als Absatz in das Dokument eingefügt. Die erstellte Datei wird automatisch geöffnet.
- **Parameter:**
    - `user_prompt`: Die Eingabeaufforderung für die KI zur Inhaltsgenerierung.
- **Verwendung:**
    - Wählen Sie in der "Dateierstellung" den Dateityp "Word" aus.
    - Geben Sie im Feld "Inhalt der Datei" den gewünschten Prompt ein.
    - Klicken Sie auf "Datei erstellen".

### PDF-Datei

- **Funktion:** Die `create_pdf_with_ai` Funktion erstellt eine PDF-Datei (.pdf) mit von der Gemini-KI generierten Inhalten.
- **Inhalt:** Die KI generiert den Inhalt basierend auf der Eingabe des Benutzers. Der generierte Text wird im Dokument angezeigt. Die erstellte Datei wird automatisch geöffnet.
- **Parameter:**
    - `user_prompt`: Die Eingabeaufforderung für die KI zur Inhaltsgenerierung.
- **Verwendung:**
    - Wählen Sie in der "Dateierstellung" den Dateityp "PDF" aus.
    - Geben Sie im Feld "Inhalt der Datei" den gewünschten Prompt ein.
    - Klicken Sie auf "Datei erstellen".

### PowerPoint-Datei

- **Funktion:** Die `create_ppt_with_ai` Funktion erstellt eine PowerPoint-Datei (.pptx) mit von der Gemini-KI generierten Inhalten.
- **Inhalt:** Die KI generiert den Inhalt basierend auf der Eingabe des Benutzers. Der generierte Text wird als Untertitel in einer Folie eingefügt. Die erstellte Datei wird automatisch geöffnet.
- **Parameter:**
    - `user_prompt`: Die Eingabeaufforderung für die KI zur Inhaltsgenerierung.
- **Verwendung:**
    - Wählen Sie in der "Dateierstellung" den Dateityp "PowerPoint" aus.
    - Geben Sie im Feld "Inhalt der Datei" den gewünschten Prompt ein.
    - Klicken Sie auf "Datei erstellen".

### CSV-Datei

- **Funktion:** Die `create_csv_with_ai` Funktion erstellt eine CSV-Datei (.csv) mit von der Gemini-KI generierten Inhalten.
- **Inhalt:** Die KI generiert den Inhalt basierend auf der Eingabe des Benutzers. Die Funktion trennt die generierten Inhalte nach Zeilen (`\n`) und Spalten (`,`). Die erstellte Datei wird automatisch geöffnet.
- **Parameter:**
    - `user_prompt`: Die Eingabeaufforderung für die KI zur Inhaltsgenerierung.
- **Verwendung:**
    - Wählen Sie in der "Dateierstellung" den Dateityp "CSV" aus.
    - Geben Sie im Feld "Inhalt der Datei" den gewünschten Prompt ein.
    - Klicken Sie auf "Datei erstellen".

## API-Schlüssel

Dieses Projekt verwendet die Mistral und Gemini APIs. Sie müssen sich für einen API-Schlüssel anmelden und die API-Schlüssel in Ihren Umgebungsvariablen konfigurieren.

- **Mistral API:** Besuchen Sie [Mistral AI](https://mistral.ai/) für API-Schlüssel.
- **Gemini API:** Besuchen Sie [Google AI Studio](https://ai.google.dev/) für API-Schlüssel.

## Abhängigkeiten

- `torch`: Für die Verwendung von PyTorch-Modellen.
- `openpyxl`: Für die Erstellung von Excel-Dateien.
- `docx`: Für die Erstellung von Word-Dateien.
- `fpdf`: Für die Erstellung von PDF-Dateien.
- `pptx`: Für die Erstellung von PowerPoint-Dateien.
- `csv`: Für die Erstellung von CSV-Dateien.
- `transformers`: Für die Verwendung von Transformer-Modellen.
- `datasets`: Für die Verwendung von Datensätzen.
- `gradio`: Für die Erstellung der Benutzeroberfläche.
- `Pillow`: Für die Bildverarbeitung.
- `requests`: Für HTTP-Anfragen an die API.
- `json`: Für JSON-Datenverarbeitung.
- `base64`: Für die Base64-Kodierung.
- `io`: Für die Verwendung von BytesIO.
- `mistralai`: Für die Mistral API.
- `google-generativeai`: Für die Gemini API.
- `subprocess`: Für die Ausführung von Befehlen im Terminal.
- `re`: Für die Verwendung von Regulären Ausdrücken.
- `PyPDF2`: Für die Verarbeitung von PDF-Dateien.
- `datetime`: Für die Verwaltung von Datumsangaben.
- `typing`: Für die Typisierung.
- `pydub`: Für die Bearbeitung von Audio-Dateien.

## Beiträge

Beiträge sind willkommen! Bitte forken Sie das Repository, nehmen Sie Ihre Änderungen vor und senden Sie einen Pull Request.

## Lizenz

Dieses Projekt ist unter der [MIT-Lizenz](LICENSE) lizenziert.
```

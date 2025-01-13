# Chatbots mit Bild- und Audioanalyse im Webinterface

Dieses Projekt implementiert eine leistungsstarke und vielseitige Chatbot-Plattform, die mehrere Modelle und KI-Dienste integriert, darunter **Mistral**, **Gemini** und **Ollama**. Die Plattform bietet eine intuitive Weboberfläche mit Funktionen für Text-, Bild- und Audioverarbeitung, unterstützt durch Gradio.

## Funktionen

### Allgemein
- **Mehrere KI-Modelle**: Unterstützung für Mistral, Gemini und Ollama.
- **Audioverarbeitung**: Automatische Sprach-zu-Text-Transkription mit OpenAI's Whisper-Modell.
- **Bildanalyse**: Bildverarbeitung und Analyse mit Mistral und Gemini.
- **OCR-Funktionalität**: Strukturierte Extraktion von Daten aus Dokumenten.
- **Chat-Speicherung**: Speichern, Anzeigen und Löschen von Chats.

### Spezifische Funktionen
1. **Mistral Chatbot**
   - Verarbeitung von Text-, Bild- und Audiodaten.
   - Unterstützung von Bildvergleichen und Diagrammverstehen.
   - Funktionen zur Umschreibung von Belegen und Dokumenten.
   - OCR mit JSON-Ausgabe.
2. **Gemini Chatbot**
   - Bildverarbeitung mit kreativen Beschreibungen.
   - Unterstützung für Audioverarbeitung.
3. **Ollama Chatbot**
   - Unterstützung für mehrere Modelle (z. B. phi4, llama2).
   - Verarbeitung von PDF- und TXT-Dateien.
   - Live-Ausgabe während der Verarbeitung.

## Anforderungen

- **Python 3.12**
- **CUDA** (optional für GPU-Unterstützung)
- Installierte Python-Bibliotheken:
  - `torch`
  - `transformers`
  - `gradio`
  - `datasets`
  - `requests`
  - `pydub`
  - `PyPDF2`

Installieren Sie alle erforderlichen Pakete mit:
```bash
pip install torch transformers gradio datasets requests pydub PyPDF2
```

## Installation

1. Klonen Sie das Repository:
   ```bash
   git clone https://github.com/kruemmel-python/multi-model-ai-chatbot-ui.git
   cd multi-model-ai-chatbot-ui
   ```

2. Installieren Sie die Python-Abhängigkeiten:
   ```bash
   pip install -r requirements.txt
   ```

3. Stellen Sie sicher, dass die Umgebungsvariablen für die API-Schlüssel gesetzt sind:
   ```bash
   export MISTRAL_API_KEY=<IhrMistralAPIKey>
   export GEMINI_API_KEY=<IhrGeminiAPIKey>
   ```

4. Starten Sie die Anwendung:
   ```bash
   python app.py
   ```

5. Rufen Sie die Weboberfläche unter `http://localhost:7779` auf.

## Verwendung

### Mistral Chatbot
- **Textnachrichten senden**: Geben Sie Ihre Nachricht in das Textfeld ein und klicken Sie auf "Senden".
- **Bildanalyse**: Laden Sie ein Bild hoch und klicken Sie auf "Bild Nachricht senden".
- **Audioverarbeitung**: Laden Sie eine Audiodatei hoch, um den Textinhalt zu extrahieren.
- **Bildvergleich**: Laden Sie zwei Bilder hoch, um Unterschiede zu analysieren.
- **OCR und Dokumentumschreibung**: Laden Sie ein Bild eines Dokuments hoch, um strukturierte Daten oder eine Umschrift zu erhalten.

### Gemini Chatbot
- Ähnlich wie Mistral, mit Fokus auf kreative Bildbeschreibungen.

### Ollama Chatbot
- Wählen Sie ein Modell aus der Dropdown-Liste.
- Geben Sie Text ein oder laden Sie eine Datei hoch (TXT oder PDF).
- Starten Sie die Verarbeitung und verfolgen Sie die Live-Ausgabe.

## Architektur

Das Projekt ist modular aufgebaut und nutzt die folgenden Hauptkomponenten:

1. **KI-Modelle**: 
   - Mistral: Bild- und Chat-Analyse.
   - Gemini: Generative KI für kreative Bild- und Textverarbeitung.
   - Ollama: Vielseitige Text- und Dateiunterstützung.

2. **Benutzeroberfläche**:
   - Basierend auf Gradio mit Tabs für verschiedene Chatbot-Dienste.
   - Unterstützung für Bild- und Dateiuploads.

3. **Datenverarbeitung**:
   - Audio: Konvertierung in WAV-Format und Transkription mit Whisper.
   - Bild: Kodierung in Base64 für API-Anfragen.
   - PDF/TXT: Textauszug und Verarbeitung.

## Screenshots

### Mistral
![image](https://github.com/user-attachments/assets/2b389454-5310-4cc3-85cf-34dafff1477c)


### Gemini
![image](https://github.com/user-attachments/assets/c6878394-7ce5-467f-adbf-51917b0e10c8)


### Ollama
![image](https://github.com/user-attachments/assets/8a6bb073-f209-4c04-afb7-21730703719b)

### Dateien (Inhalt wird an Mistral gesendet und in ausgewähltem Dokument gespeichert und geöffnet)
![image](https://github.com/user-attachments/assets/1970ed41-6986-49e8-b127-d39384735c16)



## Erweiterungen

- **Integration weiterer Modelle**: Neue KI-Dienste können leicht hinzugefügt werden.
- **Erweiterung der OCR-Funktionalität**: Unterstützung für mehrsprachige Dokumente.
- **Verbesserte Benutzeroberfläche**: Fortschrittsanzeigen und erweiterte Chat-Optionen.

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz. Weitere Informationen finden Sie in der [LICENSE](LICENSE)-Datei.

## Kontakt

Für Fragen oder Vorschläge wenden Sie sich bitte an [Ihre E-Mail-Adresse] oder erstellen Sie ein Issue auf GitHub.

---


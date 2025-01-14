# Benutzerhandbuch

Willkommen zum Benutzerhandbuch für Ihr Programm! Dieses Dokument bietet eine umfassende Anleitung für Entwickler und Endbenutzer. Es enthält Informationen zur Installation, Nutzung und Fehlerbehebung.

## Inhaltsverzeichnis
1. [Einführung](#einführung)
2. [Installation](#installation)
3. [Funktionen](#funktionen)
    - [Chat mit KI-Modellen](#chat-mit-ki-modellen)
    - [Bild- und Audioanalyse](#bild--und-audioanalyse)
    - [Dateierstellung](#dateierstellung)
4. [Erweiterte Nutzung](#erweiterte-nutzung)
5. [Datensicherheit](#datensicherheit)
6. [Fehlerbehebung](#fehlerbehebung)
7. [FAQ](#faq)
8. [Kontakt](#kontakt)

## Einführung

Dieses Programm nutzt KI-Modelle wie **Mistral**, **Gemini** und **Ollama**, um folgende Aufgaben zu erledigen:
- **Text-, Bild- und Audioanalyse**
- **Interaktive Chats mit KI**
- **Erstellung von Dateien (Excel, Word, PDF, usw.)**

## Installation

### Voraussetzungen
- **Python 3.12** oder höher
- **pip** (Python-Paketmanager)

### Installationsanleitung
1. Klonen Sie das Repository:
    ```bash
    git clone https://github.com/kruemmel-python/multi-model-ai-chatbot-ui.git
    cd multi-model-ai-chatbot-ui
    ```
2. Installieren Sie die Abhängigkeiten:
    ```bash
    pip install -r requirements.txt
    ```
3. Erstellen Sie eine `.env`-Datei und fügen Sie Ihre API-Schlüssel hinzu:
    ```env
    MISTRAL_API_KEY=IhrMistralAPIKey
    GEMINI_API_KEY=IhrGeminiAPIKey
    ```

4. Starten Sie das Programm:
    ```bash
    python main.py
    ```

## Funktionen

### Chat mit KI-Modellen

#### Nutzung
1. Öffnen Sie die Gradio-Benutzeroberfläche (wird automatisch gestartet).
2. Wählen Sie den gewünschten Chatbot (**Mistral**, **Gemini** oder **Ollama**) aus.
3. Geben Sie Ihre Nachricht in das Textfeld ein und klicken Sie auf **Senden**.

#### Beispielanwendung
- **Mistral Chatbot**: Ideal für längere Gespräche und Bildanalysen.
- **Gemini Chatbot**: Geeignet für kreative Textgenerierung.
- **Ollama Chatbot**: Perfekt für Dokumentenvergleiche.

### Bild- und Audioanalyse

#### Nutzung
1. Laden Sie ein Bild oder eine Audiodatei über die Benutzeroberfläche hoch.
2. Wählen Sie die gewünschte Analyseoption aus (z. B. **OCR**, **Diagramme verstehen**).
3. Das Ergebnis wird im Chatfenster angezeigt.

#### Beispielanwendung
- **OCR**: Extrahiert Texte aus Bildern.
- **Beleganalyse**: Analysiert Rechnungen und extrahiert relevante Informationen.

### Dateierstellung

#### Nutzung
1. Wählen Sie das gewünschte Dateiformat (Excel, Word, PDF, PowerPoint oder CSV).
2. Geben Sie den Inhalt und die benötigten Parameter ein (z. B. Anzahl der Tabellenblätter).
3. Klicken Sie auf **Datei erstellen** und laden Sie die Datei herunter.

#### Beispielanwendung
- **Excel**: Erstellen von tabellarischen Berichten.
- **PDF**: Generieren von Textdokumenten mit einfacher Formatierung.

## Erweiterte Nutzung

### Arbeiten mit API-Schlüsseln
- **Speicherung**: API-Schlüssel werden in einer `.env`-Datei gespeichert.
- **Sicherheit**: Teilen Sie Ihre API-Schlüssel niemals öffentlich.

### Anpassung der Modelle
- **Modellparameter**: Sie können die Parameter der Modelle (z. B. `temperature`, `top_p`) in den Konfigurationsdateien anpassen.

## Datensicherheit

### Umgang mit sensiblen Daten in Ollama
- **Lokalität der Verarbeitung**: Ollama führt alle Datenverarbeitungen lokal aus, sodass keine sensiblen Daten an externe Server gesendet werden.
- **Keine Speicherung**: Hochgeladene Dateien und eingegebene Inhalte werden nicht dauerhaft gespeichert.
- **Protokollierung deaktivieren**: Es wird keine Protokollierung von Benutzereingaben oder Ergebnissen vorgenommen.
- **Empfohlene Maßnahmen**:
  - Teilen Sie keine vertraulichen Informationen, die nicht notwendig sind.
  - Entfernen Sie sensible Daten aus Dokumenten, bevor Sie diese hochladen.

### Sicherheit bei anderen Modulen
- **Mistral und Gemini**:
  - API-Kommunikation erfolgt über verschlüsselte Verbindungen (HTTPS).
  - Vertrauliche Daten sollten nur verarbeitet werden, wenn dies notwendig ist.

## Fehlerbehebung

| Problem                           | Lösung                                                                 |
|-----------------------------------|------------------------------------------------------------------------|
| Gradio-Oberfläche lädt nicht      | Stellen Sie sicher, dass Python korrekt installiert ist.              |
| API-Schlüssel ungültig            | Überprüfen Sie Ihre `.env`-Datei.                                     |
| Dateien können nicht hochgeladen werden | Prüfen Sie das Dateiformat und die Dateigröße.                        |
| Programm stürzt ab                | Sehen Sie sich die Fehlermeldung im Terminal an und beheben Sie diese. |

## FAQ

**1. Kann ich mehrere Dateien gleichzeitig hochladen?**
- Ja, für einige Funktionen wie den Dokumentenvergleich.

**2. Welche Bildformate werden unterstützt?**
- JPEG und PNG.

**3. Welche Sprachen werden unterstützt?**
- Der Standard ist Deutsch, aber Modelle wie Ollama können auch andere Sprachen verwenden.

## Kontakt

Wenn Sie Unterstützung benötigen, wenden Sie sich an:
- **E-Mail**: ralf.kruemmel+python@outlook.de
- **GitHub Issues**: [https://github.com/kruemmel-python/multi-model-ai-chatbot-ui/issues](https://github.com/kruemmel-python/multi-model-ai-chatbot-ui/issues)

---
Vielen Dank, dass Sie mein Programm verwenden! Ich hoffe, dass es Ihre Anforderungen erfüllt.

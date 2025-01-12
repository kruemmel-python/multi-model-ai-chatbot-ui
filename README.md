# Chatbot mit Bildanalyse

## Inhaltsverzeichnis
- [Einleitung](#einleitung)
- [Funktionen](#funktionen)
- [Voraussetzungen](#voraussetzungen)
- [Installation](#installation)
- [Konfiguration](#konfiguration)
- [Verwendung](#verwendung)
- [Ollama Einrichtung](#ollama-einrichtung)
- [Fehlerbehebung](#fehlerbehebung)
- [Zusätzliche Informationen](#zus%C3%A4tzliche-informationen)
- [Beiträge](#beitr%C3%A4ge)

---

## Einleitung

Dieses Projekt bietet eine vielseitige Chatbot-Anwendung mit Unterstützung für verschiedene große Sprachmodelle (LLMs), einschließlich **Mistral**, **Gemini** und **Ollama**. Es ermöglicht Benutzern, Text- und Bildanfragen einzureichen, Chats zu speichern, zu verwalten und Bilder zu analysieren.

---

## Funktionen

| Funktion                | Unterstützt von    |
|-------------------------|--------------------|
| Chat mit Text           | Mistral, Gemini   |
| Bildanalyse            | Mistral, Gemini   |
| Bildvergleich          | Mistral           |
| OCR                    | Mistral           |
| Datei-Uploads          | Ollama            |
| Lokale Modellverarbeitung | Ollama            |

### Beispielanwendungen
- **Mistral Bildanalyse:** Laden Sie ein Bild hoch und geben Sie eine Beschreibung ein wie: *"Analysieren Sie dieses Diagramm und beschreiben Sie die Trends."*
- **Gemini Bildbeschreibung:** Laden Sie ein Bild hoch und fragen Sie: *"Beschreiben Sie dieses Bild in einer poetischen Weise."*
- **Ollama Textverarbeitung:** Laden Sie eine PDF-Datei hoch und lassen Sie deren Inhalt analysieren.

---

## Voraussetzungen

- **Python:** Version 3.12 oder höher
- **Erforderliche Bibliotheken:**
  - Gradio: Benutzeroberfläche
  - Mistral SDK: API-Integration
  - PIL: Bildverarbeitung
  - PyPDF2: PDF-Handling
  - Andere Pakete: Siehe `requirements.txt`
- **Mistral API-Schlüssel**: Registrierung unter [Mistral](https://mistral.ai).
- **Gemini API-Schlüssel**: Registrierung unter [Google AI Studio](https://ai.google/studio).
- **Ollama:** Installation erforderlich (siehe [Ollama Website](https://ollama.ai)).

---

## Installation

1. **Repository klonen:**
   ```bash
   git clone https://github.com/DeinUsername/Chatbot-mit-Bildanalyse.git
   cd Chatbot-mit-Bildanalyse
   ```

2. **Erforderliche Pakete installieren:**
   ```bash
   pip install -r requirements.txt
   ```

3. **API-Schlüssel konfigurieren:**
   - **Mistral:**
     ```bash
     export MISTRAL_API_KEY="Ihr_Mistral_API_Schlüssel"
     ```
   - **Gemini:**
     ```bash
     export GEMINI_API_KEY="Ihr_Gemini_API_Schlüssel"
     ```

4. **Anwendung starten:**
   ```bash
   python script.py
   ```
   Die Benutzeroberfläche ist nun unter [http://localhost:7479](http://localhost:7479) verfügbar.

---

## Konfiguration

### Ollama Einrichtung

1. **Ollama installieren:**
   Befolgen Sie die Installationsanweisungen auf der [Ollama Website](https://ollama.ai/search)).

2. **Modelle herunterladen:**
   Verwenden Sie die folgenden Befehle, um die benötigten Modelle herunterzuladen:
   ```bash
   ollama run mistral
   ollama run phi4
   ollama run llama3.3
   ollama run dolphin-mistral
   ```
   Laden Sie weitere Modelle entsprechend Ihren Anforderungen herunter.

3. **Ollama Chatbot verwenden:**
   - Wählen Sie ein Modell aus der Dropdown-Liste in der Registerkarte "Ollama Chatbot".
   - Geben Sie Ihre Anfrage ein oder laden Sie eine TXT-/PDF-Datei hoch.
   - Klicken Sie auf "Senden", um die Antwort zu generieren.

---

## Fehlerbehebung

### Typische Probleme und Lösungen

1. **Fehler:** `MISTRAL_API_KEY nicht gesetzt`
   - **Lösung:** Stellen Sie sicher, dass die Umgebungsvariable korrekt konfiguriert ist.
     ```bash
     export MISTRAL_API_KEY="Ihr_Mistral_API_Schlüssel"
     ```

2. **Problem:** `Ollama Modelle nicht gefunden`
   - **Lösung:** Laden Sie die Modelle mit dem Befehl `ollama pull` herunter.

3. **Fehler bei Bildanalyse:**
   - **Lösung:** Prüfen Sie, ob das hochgeladene Bild im unterstützten Format (JPEG/PNG) vorliegt.

---

## Zusätzliche Informationen

- **Sicherheit:**
  - Vermeiden Sie es, API-Schlüssel direkt im Code zu speichern.
  - Nutzen Sie Umgebungsvariablen oder sichere Speichermethoden.

- **Dateispeicher:**
  - Das Skript speichert Chatverläufe lokal im Verzeichnis `.gradio`.

- **Live-Ausgabe:**
  - Die Benutzeroberfläche zeigt live generierte Antworten für ein dynamisches Erlebnis an.

---

## Beiträge

Beiträge zu diesem Projekt sind willkommen! Bitte folgen Sie diesen Schritten:

1. **Repository forken** und einen neuen Branch erstellen:
   ```bash
   git checkout -b feature/neue-funktion
   ```

2. Änderungen vornehmen und testen.

3. Pull-Request erstellen mit einer Beschreibung der Änderungen.

---

Viel Spaß beim Chatten und Analysieren!


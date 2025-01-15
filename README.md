 # Modular AI Chatbot and Code Analyzer

## Überblick
Dieses Projekt ist eine modulare Anwendung, die verschiedene KI-Modelle (Mistral, Gemini, Ollama) integriert, um Chatbot-Funktionalitäten, Code-Analyse und Dateierstellung zu bieten. Die Anwendung verwendet Gradio für die Benutzeroberfläche und bietet Funktionen zur Verarbeitung von Audiodateien, Bildanalyse und Vergleich von Dokumenten.

## Installation

### Voraussetzungen
- Python 3.8 oder höher
- Pip (Python Paketmanager)

### Abhängigkeiten installieren
Installieren Sie die erforderlichen Abhängigkeiten mit dem folgenden Befehl:

pip install -r requirements.txt
Umgebungsvariablen setzen
Stellen Sie sicher, dass die erforderlichen Umgebungsvariablen gesetzt sind:


export MISTRAL_API_KEY="Ihr_Mistral_API_Schlüssel"
export GEMINI_API_KEY="Ihr_Gemini_API_Schlüssel"
Verwendung
Gradio-Benutzeroberfläche starten
Starten Sie die Gradio-Benutzeroberfläche mit dem folgenden Befehl:


python gradio_interface.py
Funktionalitäten
Chatbots: Interagieren Sie mit verschiedenen KI-Modellen (Mistral, Gemini, Ollama) über eine benutzerfreundliche Oberfläche.
Code-Analyse: Analysieren und verbessern Sie Python-Code mit Hilfe von KI-Modellen.
Dateierstellung: Erstellen Sie Excel-, Word-, PDF-, PowerPoint- und CSV-Dateien mit von KI generiertem Inhalt.
Bildanalyse: Analysieren und vergleichen Sie Bilder mit Hilfe von KI-Modellen.
Dokumentvergleich: Vergleichen Sie zwei hochgeladene Dokumente und erhalten Sie die Unterschiede.
Beispiele
Beispiel 1: Verwenden des Mistral Chatbots
Öffnen Sie die Gradio-Benutzeroberfläche.
Navigieren Sie zum Tab "Mistral Chatbot".
Geben Sie Ihre Nachricht ein und laden Sie optional ein Bild oder eine Audiodatei hoch.
Klicken Sie auf "Senden", um mit dem Chatbot zu interagieren.
Beispiel 2: Code-Analyse mit Gemini
Öffnen Sie die Gradio-Benutzeroberfläche.
Navigieren Sie zum Tab "Code Editor".
Geben Sie den zu analysierenden Python-Code ein.
Klicken Sie auf "Code analysieren", um eine Analyse des Codes zu erhalten.
Beispiel 3: Erstellen einer Excel-Datei
Öffnen Sie die Gradio-Benutzeroberfläche.
Navigieren Sie zum Tab "Dateierstellung".
Wählen Sie "Excel" als Dateiformat.
Geben Sie den gewünschten Inhalt der Datei ein.
Klicken Sie auf "Datei erstellen", um die Excel-Datei zu generieren und herunterzuladen.
Entwicklerhinweise
Projektstruktur
api_client.py: Verwaltet die API-Clients für Mistral und Gemini.
audio_processing.py: Verarbeitet Audiodateien und extrahiert Text.
chat_manager.py: Verwaltet Chat-Verläufe, einschließlich Speichern, Laden und Löschen.
codeeditor.py: Bietet Funktionen zur Analyse und Verbesserung von Python-Code.
config.py: Enthält Konfigurationsvariablen und API-Schlüssel.
file_creator.py: Erstellt Dateien mit von KI generiertem Inhalt.
gemini_functions.py: Bietet Funktionen zur Interaktion mit dem Gemini-Modell.
gradio_interface.py: Erstellt die Gradio-Benutzeroberfläche.
helpers.py: Bietet Hilfsfunktionen wie Bildkodierung und Nachrichtenformatierung.
logging_config.py: Konfiguriert das Logging für die Anwendung.
mistral_functions.py: Bietet Funktionen zur Interaktion mit dem Mistral-Modell.
model_pipeline.py: Initialisiert die Modell-Pipeline für die Spracherkennung.
ollama_functions.py: Bietet Funktionen zur Interaktion mit dem Ollama-Modell.
Testen
Um die Funktionalität der Anwendung zu testen, können Sie die folgenden Schritte ausführen:

Starten Sie die Gradio-Benutzeroberfläche.
Testen Sie die verschiedenen Funktionen, wie Chatbots, Code-Analyse, Dateierstellung, Bildanalyse und Dokumentvergleich.
Stellen Sie sicher, dass alle Funktionen wie erwartet arbeiten und dass die Ausgaben korrekt sind.
Fehlerbehebung
Falls Sie auf Probleme stoßen, überprüfen Sie die Logdateien auf Fehler und Hinweise. Die Logdateien befinden sich im Verzeichnis logs und bieten detaillierte Informationen zu den Vorgängen und Fehlern in der Anwendung.

Lizenz
Dieses Projekt ist unter der MIT-Lizenz lizenziert. Weitere Informationen finden Sie in der Datei LICENSE.

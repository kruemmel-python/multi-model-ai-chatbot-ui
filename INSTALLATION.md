# Installation

Diese Anleitung beschreibt die Schritte zur Installation und Konfiguration des Chatbot-Programms mit Bild- und Audioanalyse.

## Voraussetzungen

1. **Betriebssystem**:
   - Linux, macOS oder Windows (mit WSL2 für GPU-Unterstützung empfohlen).

2. **Python**:
   - Python 3.12 (oder höher).

3. **CUDA** (optional, für GPU-Beschleunigung):
   - NVIDIA-GPU mit aktuellen CUDA-Treibern.
   - [CUDA Toolkit installieren](https://developer.nvidia.com/cuda-downloads).

4. **Git**:
   - [Git installieren](https://git-scm.com/downloads).

5. **Ollama**:
   - Ollama ist für einige Funktionen des Programms erforderlich. Installieren Sie es nach der untenstehenden Anleitung.

---

## Schritt 1: Repository klonen

Klonen Sie das Repository in das gewünschte Verzeichnis:
```bash
git clone https://github.com/kruemmel-python/multi-model-ai-chatbot-ui.git
cd chatbots-image-audio-analysis
```

---

## Schritt 2: Python-Umgebung einrichten

Erstellen Sie eine virtuelle Python-Umgebung und aktivieren Sie diese:
```bash
python3.12 -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```

---

## Schritt 3: Abhängigkeiten installieren

Installieren Sie alle erforderlichen Bibliotheken mit pip:
```bash
pip install -r requirements.txt
```

### Alternativ: Manuelle Installation der Abhängigkeiten
Falls `requirements.txt` nicht verfügbar ist, können die Abhängigkeiten manuell installiert werden:
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118  # Für GPU-Beschleunigung
pip install transformers gradio datasets requests pydub PyPDF2 pillow google-generativeai
```

---

## Schritt 4: Ollama installieren

Ollama wird für spezifische Chat-Funktionen benötigt. Installieren Sie es wie folgt:

1. Besuchen Sie die [Ollama-Website](https://ollama.com) und laden Sie die Installationsdateien für Ihr Betriebssystem herunter.
2. Folgen Sie den Installationsanweisungen, um Ollama auf Ihrem System einzurichten.
3. Überprüfen Sie die Installation:
   ```bash
   ollama --version
   ```
4. Starten Sie Ollama:
   ```bash
   ollama run
   ```

---

## Schritt 5: Umgebungsvariablen konfigurieren

Setzen Sie die notwendigen API-Schlüssel für Mistral und Gemini:

1. Öffnen Sie die Konfigurationsdatei `.env` oder erstellen Sie sie im Hauptverzeichnis:
   ```plaintext
   MISTRAL_API_KEY=<IhrMistralAPIKey>
   GEMINI_API_KEY=<IhrGeminiAPIKey>
   ```

2. Alternativ können Sie die Variablen direkt im Terminal setzen:
   ```bash
   export MISTRAL_API_KEY=<IhrMistralAPIKey>
   export GEMINI_API_KEY=<IhrGeminiAPIKey>
   ```

   Hinweis: Unter Windows verwenden Sie `set` statt `export`.

---

## Schritt 6: Anwendung starten

Starten Sie das Programm, indem Sie die folgende Zeile ausführen:
```bash
python app.py
```

Das Gradio-Dashboard ist nun unter [http://localhost:7779](http://localhost:7779) verfügbar.

---

## GPU-Unterstützung

Falls eine NVIDIA-GPU verfügbar ist, wird das Programm automatisch auf CUDA zugreifen. Falls CUDA nicht aktiviert ist, stellen Sie sicher, dass folgende Voraussetzungen erfüllt sind:

1. Installieren Sie die NVIDIA-Treiber.
2. Installieren Sie das [CUDA Toolkit](https://developer.nvidia.com/cuda-downloads).
3. Verifizieren Sie die Installation mit:
   ```bash
   nvcc --version
   ```

---

## Problembehebung

### Fehler: "torch not compiled with CUDA enabled"
- Vergewissern Sie sich, dass die richtige Version von PyTorch installiert ist:
  ```bash
  pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
  ```

### Ollama ist nicht verfügbar
- Prüfen Sie, ob Ollama korrekt installiert und der Pfad zu den ausführbaren Dateien gesetzt ist.
- Stellen Sie sicher, dass Ollama läuft, indem Sie den folgenden Befehl ausführen:
  ```bash
  ollama run
  ```

---

## Zusätzliche Hinweise

- **Ports ändern**: Der Standardport ist `7779`. Falls dieser bereits verwendet wird, ändern Sie den Port im Code:
  ```python
  demo.launch(share=True, server_name="localhost", server_port=<NeuerPort>)
  ```

- **Erweiterung der Funktionalität**: Neue Modelle können einfach durch Hinzufügen von API-Schlüsseln und Modifikationen in der Codebasis integriert werden.

---

## Nach der Installation

Sobald die Installation abgeschlossen ist, können Sie das Programm nutzen, um:

- Chats mit Text-, Bild- und Audioeingaben durchzuführen.
- Bilder zu analysieren oder miteinander zu vergleichen.
- OCR für Belege und Dokumente durchzuführen.
- Kreative Textbeschreibungen für Bilder zu generieren.

Bei Fragen oder Problemen wenden Sie sich bitte an [Ihre E-Mail-Adresse] oder erstellen Sie ein Issue auf GitHub.

Viel Erfolg mit der Installation!

# Python-Modul-Dokumentation

## Inhaltsverzeichnis
- [api_client](#api_client)
- [audio_processing](#audio_processing)
- [chat_manager](#chat_manager)
- [codeeditor](#codeeditor)
- [config](#config)
- [file_creator](#file_creator)
- [gemini_functions](#gemini_functions)
- [gradio_interface](#gradio_interface)
- [helpers](#helpers)
- [logging_config](#logging_config)
- [mistral_functions](#mistral_functions)
- [model_pipeline](#model_pipeline)
- [ollama_functions](#ollama_functions)

## api_client
Dieses Modul verwaltet die API-Clients für Mistral und Gemini.

### Klassen
#### APIClient
Klasse zur Verwaltung der API-Clients für Mistral und Gemini.

##### Attribute
- **mistral_client** (Mistral): Der Mistral API-Client.
- **gemini_model** (genai.GenerativeModel): Das Gemini API-Modell.

##### Methoden
- **__init__**(mistral_api_key: str, gemini_api_key: str)
  Initialisiert die API-Clients für Mistral und Gemini.

### Globale Attribute
- **api_client** (APIClient): Instanz der APIClient-Klasse.

## audio_processing
Dieses Modul verarbeitet Audiodateien und extrahiert Text.

### Funktionen
#### process_audio
Verarbeitet eine Audiodatei und extrahiert den Text.

- **Parameter**:
  - **audio_file_path** (str): Der Pfad zur Audiodatei.
- **Rückgabewert**:
  - **str**: Der extrahierte Text.

## chat_manager
Dieses Modul verwaltet Chat-Verläufe.

### Klassen
#### ChatManager
Klasse zur Verwaltung von Chat-Verläufen.

##### Attribute
- **save_dir** (str): Der Speicherort für die Chat-Verläufe.
- **save_file** (str): Der Dateiname für die gespeicherten Chat-Verläufe.

##### Methoden
- **__init__**(save_dir: str, save_file: str)
  Initialisiert den ChatManager mit den angegebenen Speicherorten.
- **clear_chat**(chat_history: List[Tuple[str, str]]) -> List[Tuple[str, str]]
  Leert den Chatverlauf.
- **generate_chat_title**(chat_history: List[Tuple[str, str]]) -> str
  Generiert einen Titel basierend auf den ersten Chatnachrichten.
- **save_chat**(chat_history: List[Tuple[str, str]], saved_chats: List[Dict[str, Any]]) -> List[Dict[str, Any]]
  Speichert den aktuellen Chatverlauf.
- **_save_chats_to_file**(chats: List[Dict[str, Any]])
  Speichert Chatverläufe in einer JSON-Datei.
- **_load_chats_from_file**() -> List[Dict[str, Any]]
  Lädt Chatverläufe aus einer JSON-Datei.
- **format_saved_chat**(saved_chat: Dict[str, Any]) -> str
  Formatiert einen gespeicherten Chat für die Anzeige.
- **load_chat**(chat_title: str, saved_chats: List[Dict[str, Any]], chat_history: List[Tuple[str, str]]) -> Tuple[List[Tuple[str, str]], List[Tuple[str, str]], str]
  Lädt einen Chat in die Chat-Ausgabe.
- **new_chat**(saved_chats: List[Dict[str, Any]]) -> Tuple[List[Tuple[str, str]], List[Dict[str, Any]]]
  Startet einen neuen Chat.
- **delete_chat**(chat_title: str, saved_chats: List[Dict[str, Any]]) -> List[Dict[str, Any]]
  Löscht einen einzelnen Chat.
- **delete_all_chats**() -> List[Dict[str, Any]]
  Löscht alle gespeicherten Chats.

### Globale Attribute
- **chat_manager** (ChatManager): Instanz der ChatManager-Klasse.

## codeeditor
Dieses Modul bietet Funktionen zur Verwaltung eines Code-Editors.

### Funktionen
#### setup_api
Konfiguriert die Gemini API mit dem bereitgestellten API-Schlüssel.

- **Parameter**:
  - **gemini_api_key** (str): Der Gemini API-Schlüssel.
- **Rückgabewert**:
  - **Optional[genai.GenerativeModel]**: Das konfigurierte Gemini-Modell.

#### format_code
Formatiert den gegebenen Python-Code mit Pygments.

- **Parameter**:
  - **code_input** (str): Der Eingabe-Code.
- **Rückgabewert**:
  - **str**: Der formatierte Code.

#### save_code
Speichert den gegebenen Code in einer Datei.

- **Parameter**:
  - **code_input** (str): Der Eingabe-Code.
  - **filename** (str): Der Dateiname.

#### load_code
Lädt den Code aus einer Datei.

- **Parameter**:
  - **filename** (str): Der Dateiname.
- **Rückgabewert**:
  - **str**: Der geladene Code.

#### format_code_with_black
Formatiert den gegebenen Code mit Black.

- **Parameter**:
  - **code_input** (str): Der Eingabe-Code.
- **Rückgabewert**:
  - **str**: Der formatierte Code.

### Klassen
#### GeminiFunctions
Klasse zur Verwaltung der Gemini API-Funktionalitäten.

##### Attribute
- **model** (genai.GenerativeModel): Das Gemini API-Modell.

##### Methoden
- **__init__**(model: genai.GenerativeModel)
  Initialisiert die GeminiFunctions mit dem angegebenen Modell.
- **_speak_text**(text: str, config: dict)
  Konvertiert Text in Sprache und spielt diese ab.
- **_async_speak_text**(text: str, config: dict)
  Asynchrone Funktion zum Sprechen von Text.
- **upload_to_gemini**(image: Image.Image)
  Lädt ein Bild zur Gemini API hoch.
- **chat_with_gemini**(user_input: str, chat_history: List[Tuple[str, str]], image: Optional[Image.Image] = None, audio_file: Optional[str] = None, enable_tts: bool = False)
  Chattet mit dem Gemini-Modell.
- **analyze_image_gemini**(image: Optional[Image.Image], chat_history: List[Tuple[str, str]], user_input: str) -> List[Tuple[str, str]]
  Analysiert ein Bild mit Gemini.
- **format_code**(code_input: str) -> str
  Formatiert den gegebenen Python-Code mit Pygments.
- **save_code**(code_input: str, filename: str)
  Speichert den gegebenen Code in einer Datei.
- **load_code**(filename: str) -> str
  Lädt den Code aus einer Datei.
- **format_code_with_black**(code_input: str) -> str
  Formatiert den gegebenen Code mit Black.
- **analyze_code**(code_input: str) -> str
  Analysiert den gegebenen Python-Code und gibt Feedback.
- **suggest_code_improvements**(code_input: str) -> str
  Schlägt Verbesserungen für den gegebenen Python-Code vor.
- **update_model**(model_name: str)
  Aktualisiert das Gemini-Modell basierend auf der Auswahl.

### Globale Attribute
- **gemini_functions** (GeminiFunctions): Instanz der GeminiFunctions-Klasse.

## config
Dieses Modul enthält Konfigurationen und Umgebungsvariablen.

### Funktionen
#### load_config
Lädt die Konfiguration aus einer JSON-Datei.

- **Rückgabewert**:
  - **dict**: Die geladene Konfiguration.

#### save_config
Speichert die Konfiguration in einer JSON-Datei.

- **Parameter**:
  - **config** (dict): Die zu speichernde Konfiguration.

### Globale Attribute
- **device** (str): Das Gerät (CPU oder GPU).
- **torch_dtype** (torch.dtype): Der Datentyp für die Berechnungen.
- **model_id** (str): Die ID des Modells.
- **mistral_api_key** (str): Der Mistral API-Schlüssel.
- **gemini_api_key** (str): Der Gemini API-Schlüssel.
- **MISTRAL_CHAT_MODEL** (str): Das Mistral Chat-Modell.
- **MISTRAL_IMAGE_MODEL** (str): Das Mistral Bild-Modell.
- **MISTRAL_API_URL** (str): Die Mistral API-URL.
- **OLLAMA_MODELS** (List[str]): Die verfügbaren Ollama-Modelle.
- **DEFAULT_OLLAMA_MODEL** (str): Das Standard-Ollama-Modell.
- **STATUS_MESSAGE_GENERATING** (str): Die Statusnachricht für die Generierung.
- **STATUS_MESSAGE_COMPLETE** (str): Die Statusnachricht für die Vollendung.
- **STATUS_MESSAGE_ERROR** (str): Die Statusnachricht für Fehler.
- **SAVE_DIR** (str): Der Speicherort für die gespeicherten Dateien.
- **SAVE_FILE** (str): Der Dateiname für die gespeicherten Dateien.
- **CONFIG_FILE** (str): Der Dateiname für die Konfigurationsdatei.
- **DEFAULT_CONFIG** (dict): Die Standardkonfiguration.
- **config** (dict): Die geladene Konfiguration.

## file_creator
Dieses Modul erstellt Dateien mit von KI generiertem Inhalt.

### Klassen
#### FileCreator
Klasse zur Erstellung von Dateien mit von KI generiertem Inhalt.

##### Methoden
- **__init__**()
  Initialisiert den FileCreator.
- **generate_content_with_model**(model_name: str, user_prompt: str) -> str
  Generiert den Inhalt basierend auf dem ausgewählten Modell.
- **clean_output**(output: str) -> str
  Entfernt Steuerzeichen aus der Ollama-Ausgabe.
- **create_excel_with_ai**(user_prompt: str, sheets: int = 1) -> str
  Erstellt eine Excel-Datei mit von KI generiertem Inhalt.
- **create_word_with_ai**(user_prompt: str) -> str
  Erstellt eine Word-Datei mit von KI generiertem Inhalt.
- **create_pdf_with_ai**(user_prompt: str) -> str
  Erstellt eine PDF-Datei mit von KI generiertem Inhalt.
- **create_ppt_with_ai**(user_prompt: str) -> str
  Erstellt eine PowerPoint-Datei mit von KI generiertem Inhalt.
- **create_csv_with_ai**(user_prompt: str) -> str
  Erstellt eine CSV-Datei mit von KI generiertem Inhalt.

### Globale Attribute
- **file_creator** (FileCreator): Instanz der FileCreator-Klasse.

## gemini_functions
Dieses Modul bietet Funktionen zur Verwaltung der Gemini API-Funktionalitäten.

### Klassen
#### GeminiFunctions
Klasse zur Verwaltung der Gemini API-Funktionalitäten.

##### Methoden
- **__init__**()
  Initialisiert die GeminiFunctions.
- **_speak_text**(text: str, config: dict)
  Konvertiert Text in Sprache und spielt diese ab.
- **_async_speak_text**(text: str, config: dict)
  Asynchrone Funktion zum Sprechen von Text.
- **upload_to_gemini**(image: Image.Image)
  Lädt ein Bild zur Gemini API hoch.
- **chat_with_gemini**(user_input: str, chat_history: List[Tuple[str, str]], image: Optional[Image.Image] = None, audio_file: Optional[str] = None, enable_tts: bool = False)
  Chattet mit dem Gemini-Modell.
- **analyze_image_gemini**(image: Optional[Image.Image], chat_history: List[Tuple[str, str]], user_input: str) -> List[Tuple[str, str]]
  Analysiert ein Bild mit Gemini.
- **format_code**(code_input: str) -> str
  Formatiert den gegebenen Python-Code mit Pygments.
- **save_code**(code_input: str, filename: str)
  Speichert den gegebenen Code in einer Datei.
- **load_code**(filename: str) -> str
  Lädt den Code aus einer Datei.
- **format_code_with_black**(code_input: str) -> str
  Formatiert den gegebenen Code mit Black.
- **analyze_code**(code_input: str) -> str
  Analysiert den gegebenen Python-Code und gibt Feedback.
- **suggest_code_improvements**(code_input: str) -> str
  Schlägt Verbesserungen für den gegebenen Python-Code vor.
- **update_model**(model_name: str)
  Aktualisiert das Gemini-Modell basierend auf der Auswahl.

### Globale Attribute
- **gemini_functions** (GeminiFunctions): Instanz der GeminiFunctions-Klasse.

## gradio_interface
Dieses Modul erstellt die Gradio-Benutzeroberfläche.

### Funktionen
#### create_gradio_interface
Erstellt die Gradio-Benutzeroberfläche.

- **Rückgabewert**:
  - **gr.Blocks**: Die erstellte Gradio-Benutzeroberfläche.

## helpers
Dieses Modul bietet Hilfsfunktionen.

### Funktionen
#### encode_image
Kodiert ein Bild in Base64.

- **Parameter**:
  - **image** (Image.Image): Das zu kodierende Bild.
- **Rückgabewert**:
  - **str**: Das Base64-kodierte Bild.

#### format_chat_message
Formatiert eine Chatnachricht mit benutzerdefiniertem Stil.

- **Parameter**:
  - **text** (str): Der Text der Chatnachricht.
- **Rückgabewert**:
  - **str**: Die formatierte Chatnachricht.

## logging_config
Dieses Modul konfiguriert das Logging für die Anwendung.

### Funktionen
#### setup_logging
Konfiguriert das Logging für die Anwendung.

- **Parameter**:
  - **log_level** (str): Das Logging-Level.

## mistral_functions
Dieses Modul bietet Funktionen zur Verwaltung der Mistral-Funktionalitäten.

### Klassen
#### MistralFunctions
Klasse zur Verwaltung der Mistral-Funktionalitäten.

##### Methoden
- **__init__**()
  Initialisiert die MistralFunctions.
- **chat_with_mistral**(user_input: str, chat_history: List[Tuple[str, str]], image: Optional[Image.Image] = None, audio_file: Optional[str] = None)
  Chattet mit dem Mistral-Modell.
- **analyze_image_mistral**(image: Optional[Image.Image], chat_history: List[Tuple[str, str]], user_input: str, prompt: str) -> List[Tuple[str, str]]
  Analysiert ein Bild mit Mistral.
- **compare_images_mistral**(image1: Optional[Image.Image], image2: Optional[Image.Image], chat_history: List[Tuple[str, str]]) -> List[Tuple[str, str]]
  Vergleicht zwei Bilder mit Mistral.

### Globale Attribute
- **mistral_functions** (MistralFunctions): Instanz der MistralFunctions-Klasse.

## model_pipeline
Dieses Modul verwaltet die Modell-Pipeline für die Spracherkennung.

### Klassen
#### ModelPipeline
Klasse zur Verwaltung der Modell-Pipeline.

##### Attribute
- **model** (AutoModelForSpeechSeq2Seq): Das Modell für die Spracherkennung.
- **processor** (AutoProcessor): Der Prozessor für die Spracherkennung.
- **pipe** (pipeline): Die Pipeline für die Spracherkennung.

##### Methoden
- **__init__**(model_id: str, device: str, torch_dtype: torch.dtype)
  Initialisiert die Modell-Pipeline.

### Globale Attribute
- **model_pipeline** (ModelPipeline): Instanz der ModelPipeline-Klasse.

## ollama_functions
Dieses Modul bietet Funktionen zur Verwaltung der Ollama-Funktionalitäten.

### Klassen
#### OllamaFunctions
Klasse zur Verwaltung der Ollama-Funktionalitäten.

##### Methoden
- **__init__**()
  Initialisiert die OllamaFunctions.
- **clean_output**(output: str) -> str
  Entfernt Steuerzeichen aus der Ollama-Ausgabe.
- **format_as_codeblock**(output: str) -> str
  Formatiert die Ausgabe als Markdown-Codeblock.
- **format_output**(output: str) -> str
  Formatiert die Ausgabe mit Zeilenumbrüchen und Code-Blöcken.
- **run_ollama_live**(prompt: str, model: str)
  Führt Ollama aus und gibt die Ausgabe live zurück.
- **process_uploaded_file**(file: gr.File) -> str
  Verarbeitet hochgeladene TXT- und PDF-Dateien.
- **compare_documents**(file1: gr.File, file2: gr.File) -> str
  Vergleicht zwei hochgeladene Dokumente und gibt die Unterschiede zurück.
- **chatbot_interface**(input_text: str, model: str, file1: Optional[gr.File] = None, file2: Optional[gr.File] = None, audio_file: Optional[gr.File] = None)
  Schnittstelle für die Ollama-Chatbot-Funktion.

### Globale Attribute
- **ollama_functions** (OllamaFunctions): Instanz der OllamaFunctions-Klasse.

## Lizenzinformationen
Diese Dokumentation ist unter der MIT-Lizenz verfügbar.

## Erstellt am
16. Januar 2025

## Zurück nach oben
[Zurück nach oben](#python-modul-dokumentation)

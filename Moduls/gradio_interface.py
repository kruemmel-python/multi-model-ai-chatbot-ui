import gradio as gr
from mistral_functions import mistral_functions
from gemini_functions import gemini_functions
from chat_manager import chat_manager
from ollama_functions import ollama_functions
from file_creator import file_creator
from api_client import api_client
from config import OLLAMA_MODELS, DEFAULT_OLLAMA_MODEL, STATUS_MESSAGE_GENERATING, STATUS_MESSAGE_COMPLETE, STATUS_MESSAGE_ERROR, config
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def create_gradio_interface():
    """
    Erstellt die Gradio-Benutzeroberfläche.

    Returns:
        gr.Blocks: Die erstellte Gradio-Benutzeroberfläche.
    """
    with gr.Blocks() as demo:
        gr.Markdown("## Chatbots mit Bild- und Audioanalyse")

        with gr.Tabs():
            # --- Mistral Chatbot ---
            with gr.TabItem("Mistral Chatbot"):
                mistral_chatbot = gr.Chatbot(label="Chat-Verlauf", height=400)
                mistral_state = gr.State([])
                mistral_saved_chats = gr.State(chat_manager._load_chats_from_file())

                with gr.Row():
                    with gr.Column(scale=5):
                        mistral_user_input = gr.Textbox(label="Nachricht", placeholder="Geben Sie hier Ihre Nachricht ein...")
                    with gr.Column(scale=1, min_width=100):
                        mistral_submit_btn = gr.Button("Senden")
                with gr.Row():
                    with gr.Column(scale=1):
                        mistral_image_upload = gr.Image(type="pil", label="Bild hochladen", height=200)
                    with gr.Column(scale=1):
                        mistral_audio_upload = gr.Audio(type="filepath", label="Audio hochladen")
                    with gr.Column(scale=1):
                        mistral_analyze_btn = gr.Button("Bild mit Nachricht senden")

                with gr.Row():
                    mistral_clear_chat_button = gr.Button("Chat leeren")
                    mistral_save_chat_button = gr.Button("Chat speichern")
                    mistral_new_chat_button = gr.Button("Neuen Chat starten")

                with gr.Accordion("Gespeicherte Chats", open=False):
                    mistral_saved_chat_display = gr.Radio(label="Gespeicherte Chats", interactive=True)
                    with gr.Row():
                        mistral_delete_chat_button = gr.Button("Ausgewählten Chat löschen")
                        mistral_delete_all_chats_button = gr.Button("Alle Chats löschen")

                with gr.Tabs():
                    with gr.TabItem("Bildanalyse"):
                        with gr.Row():
                            with gr.Column(scale=1):
                                mistral_image_upload_analysis = gr.Image(type="pil", label="Bild hochladen", height=200)
                            with gr.Column(scale=1):
                                mistral_analyze_btn_analysis = gr.Button("Nur Bild analysieren")

                        with gr.Row():
                            with gr.Column(scale=1):
                                mistral_analyze_btn_charts = gr.Button("Diagramme verstehen")
                            with gr.Column(scale=1):
                                mistral_analyze_btn_compare = gr.Button("Bilder vergleichen")
                            with gr.Column(scale=1):
                                mistral_analyze_btn_receipts = gr.Button("Belege umschreiben")
                            with gr.Column(scale=1):
                                mistral_analyze_btn_documents = gr.Button("Alte Dokumente umschreiben")
                            with gr.Column(scale=1):
                                mistral_analyze_btn_ocr = gr.Button("OCR mit strukturiertem Output")

                    with gr.TabItem("Bildvergleich"):
                        with gr.Row():
                            with gr.Column(scale=1):
                                mistral_image_upload_compare1 = gr.Image(type="pil", label="Bild 1 hochladen", height=200)
                            with gr.Column(scale=1):
                                mistral_image_upload_compare2 = gr.Image(type="pil", label="Bild 2 hochladen", height=200)
                        with gr.Row():
                            mistral_compare_btn = gr.Button("Bilder vergleichen")

                mistral_submit_btn.click(
                    mistral_functions.chat_with_mistral,
                    inputs=[mistral_user_input, mistral_state, mistral_image_upload, mistral_audio_upload],
                    outputs=[mistral_chatbot, mistral_user_input]
                )

                mistral_analyze_btn.click(
                    lambda image, chat_history, user_input: mistral_functions.analyze_image_mistral(image, chat_history, user_input, "Beschreiben Sie das Bild mit einer kreativen Beschreibung. Bitte in Deutsch antworten."),
                    inputs=[mistral_image_upload, mistral_state, mistral_user_input],
                    outputs=[mistral_chatbot]
                )
                mistral_clear_chat_button.click(chat_manager.clear_chat, inputs=[mistral_state], outputs=[mistral_chatbot])
                mistral_save_chat_button.click(chat_manager.save_chat, inputs=[mistral_state, mistral_saved_chats], outputs=[mistral_saved_chats])
                mistral_new_chat_button.click(chat_manager.new_chat, inputs=[mistral_saved_chats], outputs=[mistral_chatbot, mistral_saved_chats])

                def update_mistral_radio(chats):
                    formatted_chats = [chat_manager.format_saved_chat(chat) for chat in chats]
                    return gr.update(choices=formatted_chats)

                mistral_saved_chats.change(update_mistral_radio, inputs=[mistral_saved_chats], outputs=[mistral_saved_chat_display])
                mistral_saved_chat_display.change(chat_manager.load_chat, inputs=[mistral_saved_chat_display, mistral_saved_chats, mistral_state], outputs=[mistral_chatbot, mistral_state, mistral_saved_chat_display])

                mistral_delete_chat_button.click(chat_manager.delete_chat, inputs=[mistral_saved_chat_display, mistral_saved_chats], outputs=[mistral_saved_chats])
                mistral_delete_all_chats_button.click(chat_manager.delete_all_chats, outputs=[mistral_saved_chats])
                demo.load(update_mistral_radio, inputs=[mistral_saved_chats], outputs=[mistral_saved_chat_display])

                mistral_analyze_btn_analysis.click(
                    lambda image, chat_history, user_input: mistral_functions.analyze_image_mistral(image, chat_history, user_input, "Was ist auf diesem Bild? Bitte in Deutsch antworten."),
                    inputs=[mistral_image_upload_analysis, mistral_state, mistral_user_input],
                    outputs=[mistral_chatbot]
                )
                mistral_analyze_btn_charts.click(
                    lambda image, chat_history, user_input: mistral_functions.analyze_image_mistral(image, chat_history, user_input, "Was ist auf diesem Bild? Bitte in Deutsch antworten."),
                    inputs=[mistral_image_upload_analysis, mistral_state, mistral_user_input],
                    outputs=[mistral_chatbot]
                )
                mistral_analyze_btn_compare.click(
                    lambda image, chat_history, user_input: mistral_functions.analyze_image_mistral(image, chat_history, user_input, "Was sind die Unterschiede zwischen den beiden Bildern? Bitte in Deutsch antworten."),
                    inputs=[mistral_image_upload_analysis, mistral_state, mistral_user_input],
                    outputs=[mistral_chatbot]
                )
                mistral_analyze_btn_receipts.click(
                    lambda image, chat_history, user_input: mistral_functions.analyze_image_mistral(image, chat_history, user_input, "Transkribieren Sie diesen Beleg. Bitte in Deutsch antworten."),
                    inputs=[mistral_image_upload_analysis, mistral_state, mistral_user_input],
                    outputs=[mistral_chatbot]
                )
                mistral_analyze_btn_documents.click(
                    lambda image, chat_history, user_input: mistral_functions.analyze_image_mistral(image, chat_history, user_input, "Transkribieren Sie dieses Dokument. Bitte in Deutsch antworten."),
                    inputs=[mistral_image_upload_analysis, mistral_state, mistral_user_input],
                    outputs=[mistral_chatbot]
                )
                mistral_analyze_btn_ocr.click(
                    lambda image, chat_history, user_input: mistral_functions.analyze_image_mistral(image, chat_history, user_input, "Extrahieren Sie aus dieser Rechnung die Rechnungsnummer, die Artikelnamen und zugehörigen Preise sowie den Gesamtpreis und geben Sie sie als Zeichenfolge in einem JSON-Objekt zurück. Bitte in Deutsch antworten."),
                    inputs=[mistral_image_upload_analysis, mistral_state, mistral_user_input],
                    outputs=[mistral_chatbot]
                )

                mistral_compare_btn.click(mistral_functions.compare_images_mistral, inputs=[mistral_image_upload_compare1, mistral_image_upload_compare2, mistral_state], outputs=[mistral_chatbot])

            # --- Gemini Chatbot ---
            with gr.TabItem("Gemini Chatbot"):
                gemini_chatbot = gr.Chatbot(label="Chat-Verlauf", height=400)
                gemini_state = gr.State([])
                gemini_saved_chats = gr.State(chat_manager._load_chats_from_file())

                with gr.Row():
                    with gr.Column(scale=5):
                        gemini_user_input = gr.Textbox(label="Nachricht", placeholder="Geben Sie hier Ihre Nachricht ein...")
                    with gr.Column(scale=1, min_width=100):
                        gemini_submit_btn = gr.Button("Senden")
                with gr.Row():
                    with gr.Column(scale=1):
                        gemini_image_upload = gr.Image(type="pil", label="Bild hochladen", height=200)
                    with gr.Column(scale=1):
                        gemini_audio_upload = gr.Audio(type="filepath", label="Audio hochladen")
                    with gr.Column(scale=1):
                        gemini_analyze_btn = gr.Button("Bild mit Nachricht senden")

                with gr.Row():
                    gemini_clear_chat_button = gr.Button("Chat leeren")
                    gemini_save_chat_button = gr.Button("Chat speichern")
                    gemini_new_chat_button = gr.Button("Neuen Chat starten")

                with gr.Accordion("Gespeicherte Chats", open=False):
                    gemini_saved_chat_display = gr.Radio(label="Gespeicherte Chats", interactive=True)
                    with gr.Row():
                        gemini_delete_chat_button = gr.Button("Ausgewählten Chat löschen")
                        gemini_delete_all_chats_button = gr.Button("Alle Chats löschen")

                gemini_enable_tts = gr.Checkbox(label="TTS aktivieren", value=config.get("enable_tts", False))

                gemini_submit_btn.click(
                    gemini_functions.chat_with_gemini,
                    inputs=[gemini_user_input, gemini_state, gemini_image_upload, gemini_audio_upload, gemini_enable_tts],
                    outputs=[gemini_chatbot, gemini_user_input]
                )

                gemini_analyze_btn.click(
                    lambda image, chat_history, user_input, tts_enabled: gemini_functions.analyze_image_gemini(image, chat_history, user_input, tts_enabled),
                    inputs=[gemini_image_upload, gemini_state, gemini_user_input, gemini_enable_tts],
                    outputs=[gemini_chatbot]
                )
                gemini_clear_chat_button.click(chat_manager.clear_chat, inputs=[gemini_state], outputs=[gemini_chatbot])
                gemini_save_chat_button.click(chat_manager.save_chat, inputs=[gemini_state, gemini_saved_chats], outputs=[gemini_saved_chats])
                gemini_new_chat_button.click(chat_manager.new_chat, inputs=[gemini_saved_chats], outputs=[gemini_chatbot, gemini_saved_chats])

                def update_gemini_radio(chats):
                    formatted_chats = [chat_manager.format_saved_chat(chat) for chat in chats]
                    return gr.update(choices=formatted_chats)

                gemini_saved_chats.change(update_gemini_radio, inputs=[gemini_saved_chats], outputs=[gemini_saved_chat_display])
                gemini_saved_chat_display.change(chat_manager.load_chat, inputs=[gemini_saved_chat_display, gemini_saved_chats, gemini_state], outputs=[gemini_chatbot, gemini_state, gemini_saved_chat_display])

                gemini_delete_chat_button.click(chat_manager.delete_chat, inputs=[gemini_saved_chat_display, gemini_saved_chats], outputs=[gemini_saved_chats])
                gemini_delete_all_chats_button.click(chat_manager.delete_all_chats, outputs=[gemini_saved_chats])
                demo.load(update_gemini_radio, inputs=[gemini_saved_chats], outputs=[gemini_saved_chat_display])

            # --- Ollama Chatbot ---
            with gr.TabItem("Ollama Chatbot"):
                ollama_input_text = gr.Textbox(lines=2, placeholder="Geben Sie Ihre Frage an Ollama ein", label="Eingabe (oder Datei hochladen)")
                ollama_model_selector = gr.Dropdown(choices=OLLAMA_MODELS, value=DEFAULT_OLLAMA_MODEL, label="Modell auswählen")
                ollama_file_upload1 = gr.File(label="Datei 1 hochladen (PDF oder TXT)", file_types=[".txt", ".pdf"])
                ollama_file_upload2 = gr.File(label="Datei 2 hochladen (PDF oder TXT)", file_types=[".txt", ".pdf"])
                ollama_audio_upload = gr.Audio(type="filepath", label="Audio hochladen")
                ollama_output = gr.Markdown(label="Antwort")
                ollama_status = gr.Label(label="Status")

                ollama_submit_btn = gr.Button("Senden")
                ollama_submit_btn.click(ollama_functions.chatbot_interface, inputs=[ollama_input_text, ollama_model_selector, ollama_file_upload1, ollama_file_upload2, ollama_audio_upload], outputs=[ollama_output, ollama_status])

            # --- Dateierstellung ---
            with gr.TabItem("Dateierstellung"):
                gr.Markdown("## Dateierstellung")
                with gr.Row():
                    with gr.Column(scale=1):
                        file_type = gr.Radio(choices=["Excel", "Word", "PDF", "PowerPoint", "CSV"], label="Dateiformat", value="Excel")
                    with gr.Column(scale=1):
                        sheets = gr.Slider(minimum=1, maximum=5, step=1, label="Anzahl der Tabellenblätter (nur Excel)", value=1)
                    with gr.Column(scale=2):
                        file_content = gr.Textbox(label="Inhalt der Datei", placeholder="Geben Sie den Inhalt der Datei ein...")
                    with gr.Column(scale=1):
                        create_file_btn = gr.Button("Datei erstellen")
                        download_file = gr.File(label="Herunterladen")

                create_file_btn.click(
                    lambda content, file_format, sheets: (
                        file_creator.create_excel_with_ai(content, sheets) if file_format == "Excel" else
                        file_creator.create_word_with_ai(content) if file_format == "Word" else
                        file_creator.create_pdf_with_ai(content) if file_format == "PDF" else
                        file_creator.create_ppt_with_ai(content) if file_format == "PowerPoint" else
                        file_creator.create_csv_with_ai(content)
                    ),
                    inputs=[file_content, file_type, sheets],
                    outputs=[download_file]
                )

            # --- Code Editor ---
            with gr.TabItem("Code Editor"):
                gr.Markdown("""
                <h1>Code Analyzer & Generator mit Gemini AI</h1>
                """, elem_classes="markdown-text")

                # Input Code Editor
                code_input = gr.Code(label="Code Eingabe", language="python", lines=10, elem_classes="code-output")

                # Buttons
                with gr.Row():
                    analyze_button = gr.Button("Code analysieren", variant="primary", elem_classes="button-font")
                    suggest_button = gr.Button("Vorschläge generieren", variant="secondary", elem_classes="button-font")

                # Outputs
                analysis_output = gr.Code(label="Analyse", language="python", lines=10, elem_classes="code-output")
                suggestions_output = gr.Code(label="Vorschläge", language="python", lines=10, elem_classes="code-output")

                # Button Click Events
                analyze_button.click(fn=gemini_functions.analyze_code, inputs=code_input, outputs=analysis_output)
                suggest_button.click(fn=gemini_functions.suggest_code_improvements, inputs=code_input, outputs=suggestions_output)

                # Save and Load Code
                save_button = gr.Button("Code speichern", variant="primary", elem_classes="button-font")
                load_button = gr.Button("Code laden", variant="secondary", elem_classes="button-font")
                filename_input = gr.Textbox(label="Dateiname", placeholder="Geben Sie den Dateinamen ein", elem_classes="code-output")

                save_button.click(fn=gemini_functions.save_code, inputs=[code_input, filename_input])
                load_button.click(fn=gemini_functions.load_code, inputs=filename_input, outputs=code_input)

                # Model Selection
                model_selection = gr.Dropdown(choices=["gemini-pro", "gemini-lite"], label="Gemini Modell", value="gemini-pro", elem_classes="code-output")
                model_selection.change(fn=gemini_functions.update_model, inputs=model_selection)

                # Format Code with Black
                format_button = gr.Button("Code mit black formatieren", variant="secondary", elem_classes="button-font")
                format_button.click(fn=gemini_functions.format_code_with_black, inputs=code_input, outputs=code_input)

    return demo

if __name__ == '__main__':
    demo = create_gradio_interface()
    demo.launch(share=True, server_name="localhost", server_port=2379)
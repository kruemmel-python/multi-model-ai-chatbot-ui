import gradio as gr
from mistral_functions import mistral_functions
from gemini_functions import gemini_functions
from chat_manager import chat_manager
from ollama_functions import ollama_functions
from file_creator import file_creator
from config import OLLAMA_MODELS, DEFAULT_OLLAMA_MODEL, STATUS_MESSAGE_GENERATING, STATUS_MESSAGE_COMPLETE, STATUS_MESSAGE_ERROR

def create_gradio_interface():
    """
    Erstellt die Gradio-Benutzeroberfläche mit mehreren Tabs für Chatbots, Bild- und Audioanalyse
    sowie die Erstellung von Dateien in verschiedenen Formaten.
    
    Returns:
        gr.Blocks: Die konfigurierte Gradio-Oberfläche.
    """
    with gr.Blocks() as demo:
        gr.Markdown("## Chatbots mit Bild- und Audioanalyse")

        with gr.Tabs():
            # --- Mistral Chatbot ---
            with gr.TabItem("Mistral Chatbot"):
                mistral_chatbot = gr.Chatbot(label="Chat-Verlauf", height=400)
                mistral_state = gr.State([])  # Zustandsverwaltung für den Chatverlauf.
                mistral_saved_chats = gr.State(chat_manager._load_chats_from_file())  # Geladene Chats aus der Datei.

                with gr.Row():
                    with gr.Column(scale=5):
                        mistral_user_input = gr.Textbox(
                            label="Nachricht", 
                            placeholder="Geben Sie hier Ihre Nachricht ein..."
                        )
                    with gr.Column(scale=1, min_width=100):
                        mistral_submit_btn = gr.Button("Senden")  # Schaltfläche für die Eingabe.

                with gr.Row():
                    mistral_image_upload = gr.Image(type="pil", label="Bild hochladen", height=200)
                    mistral_audio_upload = gr.Audio(type="filepath", label="Audio hochladen")  # Audio-Upload.
                    mistral_analyze_btn = gr.Button("Bild Nachricht senden")  # Schaltfläche zur Bildanalyse.

                with gr.Row():
                    mistral_clear_chat_button = gr.Button("Chat leeren")
                    mistral_save_chat_button = gr.Button("Chat speichern")
                    mistral_new_chat_button = gr.Button("Neuen Chat starten")

                # Gespeicherte Chats verwalten.
                with gr.Accordion("Gespeicherte Chats", open=False):
                    mistral_saved_chat_display = gr.Radio(label="Gespeicherte Chats", interactive=True)
                    with gr.Row():
                        mistral_delete_chat_button = gr.Button("Ausgewählten Chat löschen")
                        mistral_delete_all_chats_button = gr.Button("Alle Chats löschen")

                # Bildanalyse spezifisch.
                with gr.Tabs():
                    with gr.TabItem("Bildanalyse"):
                        mistral_image_upload_analysis = gr.Image(type="pil", label="Bild hochladen", height=200)
                        mistral_analyze_btn_analysis = gr.Button("Nur Bild analysieren")

                        mistral_analyze_btn_charts = gr.Button("Diagramme verstehen")
                        mistral_analyze_btn_compare = gr.Button("Bilder vergleichen")
                        mistral_analyze_btn_receipts = gr.Button("Belege umschreiben")
                        mistral_analyze_btn_documents = gr.Button("Alte Dokumente umschreiben")
                        mistral_analyze_btn_ocr = gr.Button("OCR mit strukturiertem Output")

                    with gr.TabItem("Bildvergleich"):
                        mistral_image_upload_compare1 = gr.Image(type="pil", label="Bild 1 hochladen", height=200)
                        mistral_image_upload_compare2 = gr.Image(type="pil", label="Bild 2 hochladen", height=200)
                        mistral_compare_btn = gr.Button("Bilder vergleichen")

                # --- Button-Funktionalität ---
                mistral_submit_btn.click(
                    mistral_functions.chat_with_mistral,
                    inputs=[mistral_user_input, mistral_state, mistral_image_upload, mistral_audio_upload],
                    outputs=[mistral_chatbot, mistral_user_input]
                )

                mistral_analyze_btn.click(
                    lambda image, chat_history, user_input: mistral_functions.analyze_image_mistral(
                        image, chat_history, user_input, "Beschreiben Sie das Bild mit einer kreativen Beschreibung. Bitte in Deutsch antworten."
                    ),
                    inputs=[mistral_image_upload, mistral_state, mistral_user_input],
                    outputs=[mistral_chatbot]
                )

                mistral_clear_chat_button.click(chat_manager.clear_chat, inputs=[mistral_state], outputs=[mistral_chatbot])
                mistral_save_chat_button.click(chat_manager.save_chat, inputs=[mistral_state, mistral_saved_chats], outputs=[mistral_saved_chats])
                mistral_new_chat_button.click(chat_manager.new_chat, inputs=[mistral_saved_chats], outputs=[mistral_chatbot, mistral_saved_chats])

                def update_mistral_radio(chats):
                    """Aktualisiert die Anzeige der gespeicherten Chats."""
                    formatted_chats = [chat_manager.format_saved_chat(chat) for chat in chats]
                    return gr.update(choices=formatted_chats)

                mistral_saved_chats.change(update_mistral_radio, inputs=[mistral_saved_chats], outputs=[mistral_saved_chat_display])
                mistral_saved_chat_display.change(
                    chat_manager.load_chat, 
                    inputs=[mistral_saved_chat_display, mistral_saved_chats, mistral_state], 
                    outputs=[mistral_chatbot, mistral_state, mistral_saved_chat_display]
                )

                mistral_delete_chat_button.click(chat_manager.delete_chat, inputs=[mistral_saved_chat_display, mistral_saved_chats], outputs=[mistral_saved_chats])
                mistral_delete_all_chats_button.click(chat_manager.delete_all_chats, outputs=[mistral_saved_chats])

                mistral_analyze_btn_analysis.click(
                    lambda image, chat_history, user_input: mistral_functions.analyze_image_mistral(
                        image, chat_history, user_input, "Was ist auf diesem Bild? Bitte in Deutsch antworten."
                    ),
                    inputs=[mistral_image_upload_analysis, mistral_state, mistral_user_input],
                    outputs=[mistral_chatbot]
                )

                mistral_compare_btn.click(
                    mistral_functions.compare_images_mistral,
                    inputs=[mistral_image_upload_compare1, mistral_image_upload_compare2, mistral_state],
                    outputs=[mistral_chatbot]
                )

            # --- Weitere Tabs wie Gemini, Ollama, Dateierstellung ---
            # Für jedes Tab analog dem Mistral-Tab eine vollständige Funktionsbeschreibung und Struktur.

    return demo

if __name__ == '__main__':
    # Starten der Gradio-Oberfläche.
    demo = create_gradio_interface()
    demo.launch(share=True, server_name="localhost", server_port=3379)

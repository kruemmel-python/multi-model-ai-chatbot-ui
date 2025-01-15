import json
from datetime import datetime
from typing import List, Dict, Any, Tuple
import os
from config import SAVE_DIR, SAVE_FILE
import logging

logger = logging.getLogger(__name__)

class ChatManager:
    """
    Klasse zur Verwaltung von Chat-Verläufen.
    """

    def __init__(self, save_dir: str, save_file: str):
        """
        Initialisiert den ChatManager mit den angegebenen Speicherorten.
        """
        self.save_dir = save_dir
        self.save_file = save_file

    def clear_chat(self, chat_history: List[Tuple[str, str]]) -> List[Tuple[str, str]]:
        """
        Leert den Chatverlauf.
        """
        chat_history.clear()
        logger.info("Chat history cleared.")
        return chat_history

    def generate_chat_title(self, chat_history: List[Tuple[str, str]]) -> str:
        """
        Generiert einen Titel basierend auf den ersten Chatnachrichten.
        """
        if not chat_history:
            return "Neuer Chat"
        first_messages = [msg[0] for msg in chat_history if msg[0] is not None][:2]
        if not first_messages:
            return "Neuer Chat"
        title = " ".join(first_messages)
        title = title[:50] + "..." if len(title) > 50 else title
        logger.info(f"Generated chat title: {title}")
        return title

    def save_chat(self, chat_history: List[Tuple[str, str]], saved_chats: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Speichert den aktuellen Chatverlauf.
        """
        if not chat_history:
            return saved_chats

        title = self.generate_chat_title(chat_history)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        saved_chat = {
            "title": title,
            "date": timestamp,
            "chat": chat_history,
        }
        saved_chats.append(saved_chat)
        self._save_chats_to_file(saved_chats)
        logger.info(f"Saved chat with title: {title}")
        return saved_chats

    def _save_chats_to_file(self, chats: List[Dict[str, Any]]):
        """
        Speichert Chatverläufe in einer JSON-Datei.
        """
        try:
            os.makedirs(self.save_dir, exist_ok=True)
            with open(self.save_file, 'w', encoding='utf-8') as f:
                json.dump(chats, f, ensure_ascii=False, indent=4)
            logger.info(f"Chats saved to file: {self.save_file}")
        except Exception as e:
            logger.error(f"Error saving chats: {e}")
            raise

    def _load_chats_from_file(self) -> List[Dict[str, Any]]:
        """
        Lädt Chatverläufe aus einer JSON-Datei.
        """
        if os.path.exists(self.save_file):
            try:
                with open(self.save_file, 'r', encoding='utf-8') as f:
                    logger.info(f"Chats loaded from file: {self.save_file}")
                    return json.load(f)
            except json.JSONDecodeError as e:
                logger.error(f"Error loading chats: {e}")
                return []
        return []

    def format_saved_chat(self, saved_chat: Dict[str, Any]) -> str:
        """
        Formatiert einen gespeicherten Chat für die Anzeige.
        """
        return f"**{saved_chat['title']}** ({saved_chat['date']})"

    def load_chat(self, chat_title: str, saved_chats: List[Dict[str, Any]], chat_history: List[Tuple[str, str]]) -> Tuple[List[Tuple[str, str]], List[Tuple[str, str]], str]:
        """
        Lädt einen Chat in die Chat-Ausgabe.
        """
        selected_chat = next((chat for chat in saved_chats if self.format_saved_chat(chat) == chat_title), None)
        if selected_chat:
            logger.info(f"Loaded chat with title: {chat_title}")
            return selected_chat['chat'], selected_chat['chat'], chat_title
        return chat_history, chat_history, None

    def new_chat(self, saved_chats: List[Dict[str, Any]]) -> Tuple[List[Tuple[str, str]], List[Dict[str, Any]]]:
        """
        Startet einen neuen Chat.
        """
        logger.info("Started new chat.")
        return [], saved_chats

    def delete_chat(self, chat_title: str, saved_chats: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Löscht einen einzelnen Chat.
        """
        updated_chats = [chat for chat in saved_chats if self.format_saved_chat(chat) != chat_title]
        self._save_chats_to_file(updated_chats)
        logger.info(f"Deleted chat with title: {chat_title}")
        return updated_chats

    def delete_all_chats(self) -> List[Dict[str, Any]]:
        """
        Löscht alle gespeicherten Chats.
        """
        self._save_chats_to_file([])
        logger.info("Deleted all chats.")
        return []

chat_manager = ChatManager(SAVE_DIR, SAVE_FILE)
import json
from datetime import datetime
from typing import List, Dict, Any, Tuple
import os
from config import SAVE_DIR, SAVE_FILE

class ChatManager:
    """
    Eine Klasse zur Verwaltung von Chatverläufen, einschließlich Speichern, Laden, 
    Löschen und Bearbeiten von Chats.

    Attributes:
        save_dir (str): Das Verzeichnis, in dem die Chats gespeichert werden.
        save_file (str): Der Dateiname der Datei, in der die Chats gespeichert werden.
    """

    def __init__(self, save_dir: str, save_file: str):
        """
        Initialisiert den ChatManager mit Speicherverzeichnis und Datei.

        Args:
            save_dir (str): Das Verzeichnis für die Speicherung.
            save_file (str): Der Dateiname für die Speicherung.
        """
        self.save_dir = save_dir
        self.save_file = save_file

    def clear_chat(self, chat_history: List[Tuple[str, str]]) -> List[Tuple[str, str]]:
        """
        Leert den aktuellen Chatverlauf.

        Args:
            chat_history (List[Tuple[str, str]]): Der aktuelle Chatverlauf.

        Returns:
            List[Tuple[str, str]]: Ein leerer Chatverlauf.
        """
        chat_history.clear()  # Entfernt alle Nachrichten aus der Liste.
        return chat_history

    def generate_chat_title(self, chat_history: List[Tuple[str, str]]) -> str:
        """
        Generiert einen Titel basierend auf den ersten Nachrichten des Chats.

        Args:
            chat_history (List[Tuple[str, str]]): Der aktuelle Chatverlauf.

        Returns:
            str: Ein Titel, der aus den ersten Nachrichten generiert wird.
        """
        if not chat_history:  # Überprüfen, ob der Verlauf leer ist.
            return "Neuer Chat"
        # Extrahiert die ersten zwei Nachrichten aus dem Verlauf.
        first_messages = [msg[0] for msg in chat_history if msg[0] is not None][:2]
        if not first_messages:  # Wenn keine Nachrichten verfügbar sind.
            return "Neuer Chat"
        # Generiert einen Titel aus den ersten Nachrichten, begrenzt auf 50 Zeichen.
        title = " ".join(first_messages)
        return title[:50] + "..." if len(title) > 50 else title

    def save_chat(self, chat_history: List[Tuple[str, str]], saved_chats: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Speichert den aktuellen Chatverlauf.

        Args:
            chat_history (List[Tuple[str, str]]): Der aktuelle Chatverlauf.
            saved_chats (List[Dict[str, Any]]): Die Liste der gespeicherten Chats.

        Returns:
            List[Dict[str, Any]]: Die aktualisierte Liste der gespeicherten Chats.
        """
        if not chat_history:  # Überprüfen, ob der Verlauf leer ist.
            return saved_chats

        # Generiere einen Titel und einen Zeitstempel für den Chat.
        title = self.generate_chat_title(chat_history)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        saved_chat = {
            "title": title,
            "date": timestamp,
            "chat": chat_history,
        }
        # Fügt den neuen Chat zur gespeicherten Liste hinzu und speichert diese.
        saved_chats.append(saved_chat)
        self._save_chats_to_file(saved_chats)
        return saved_chats

    def _save_chats_to_file(self, chats: List[Dict[str, Any]]):
        """
        Speichert die Chats in einer JSON-Datei.

        Args:
            chats (List[Dict[str, Any]]): Die Liste der Chats, die gespeichert werden sollen.
        """
        os.makedirs(self.save_dir, exist_ok=True)  # Erstellen des Verzeichnisses, falls nicht vorhanden.
        with open(self.save_file, 'w', encoding='utf-8') as f:
            json.dump(chats, f, ensure_ascii=False, indent=4)  # Speichern im JSON-Format.

    def _load_chats_from_file(self) -> List[Dict[str, Any]]:
        """
        Lädt die gespeicherten Chats aus einer JSON-Datei.

        Returns:
            List[Dict[str, Any]]: Die Liste der geladenen Chats.
        """
        if os.path.exists(self.save_file):  # Überprüfen, ob die Datei existiert.
            try:
                with open(self.save_file, 'r', encoding='utf-8') as f:
                    return json.load(f)  # Laden der JSON-Daten.
            except json.JSONDecodeError:  # Fehlerbehandlung für fehlerhafte Dateien.
                return []
        return []

    def format_saved_chat(self, saved_chat: Dict[str, Any]) -> str:
        """
        Formatiert einen gespeicherten Chat für die Anzeige.

        Args:
            saved_chat (Dict[str, Any]): Der gespeicherte Chat.

        Returns:
            str: Der formatierte Titel und Zeitstempel des Chats.
        """
        return f"**{saved_chat['title']}** ({saved_chat['date']})"

    def load_chat(self, chat_title: str, saved_chats: List[Dict[str, Any]], chat_history: List[Tuple[str, str]]) -> Tuple[List[Tuple[str, str]], List[Tuple[str, str]], str]:
        """
        Lädt einen gespeicherten Chat basierend auf dem Titel.

        Args:
            chat_title (str): Der Titel des zu ladenden Chats.
            saved_chats (List[Dict[str, Any]]): Die Liste der gespeicherten Chats.
            chat_history (List[Tuple[str, str]]): Der aktuelle Chatverlauf.

        Returns:
            Tuple[List[Tuple[str, str]], List[Tuple[str, str]], str]: 
                Der geladene Chatverlauf, der Chatverlauf zur Anzeige und der Titel.
        """
        selected_chat = next((chat for chat in saved_chats if self.format_saved_chat(chat) == chat_title), None)
        if selected_chat:  # Wenn ein Chat mit dem Titel gefunden wurde.
            return selected_chat['chat'], selected_chat['chat'], chat_title
        return chat_history, chat_history, None  # Fallback, wenn kein Titel gefunden wurde.

    def new_chat(self, saved_chats: List[Dict[str, Any]]) -> Tuple[List[Tuple[str, str]], List[Dict[str, Any]]]:
        """
        Startet einen neuen Chat.

        Args:
            saved_chats (List[Dict[str, Any]]): Die Liste der gespeicherten Chats.

        Returns:
            Tuple[List[Tuple[str, str]], List[Dict[str, Any]]]: Ein leerer Chatverlauf und die gespeicherten Chats.
        """
        return [], saved_chats

    def delete_chat(self, chat_title: str, saved_chats: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Löscht einen gespeicherten Chat basierend auf dem Titel.

        Args:
            chat_title (str): Der Titel des zu löschenden Chats.
            saved_chats (List[Dict[str, Any]]): Die Liste der gespeicherten Chats.

        Returns:
            List[Dict[str, Any]]: Die aktualisierte Liste der gespeicherten Chats.
        """
        updated_chats = [chat for chat in saved_chats if self.format_saved_chat(chat) != chat_title]
        self._save_chats_to_file(updated_chats)  # Speichert die aktualisierte Liste.
        return updated_chats

    def delete_all_chats(self) -> List[Dict[str, Any]]:
        """
        Löscht alle gespeicherten Chats.

        Returns:
            List[Dict[str, Any]]: Eine leere Liste der Chats.
        """
        self._save_chats_to_file([])  # Löscht alle Daten aus der Datei.
        return []

# Instanziierung eines ChatManager-Objekts mit den konfigurierten Speicherpfaden.
chat_manager = ChatManager(SAVE_DIR, SAVE_FILE)

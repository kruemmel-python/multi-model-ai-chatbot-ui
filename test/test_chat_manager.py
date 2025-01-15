import unittest
from chat_manager import ChatManager, SAVE_DIR, SAVE_FILE
import os

class TestChatManager(unittest.TestCase):
    def setUp(self):
        self.chat_manager = ChatManager(SAVE_DIR, SAVE_FILE)

    def test_clear_chat(self):
        chat_history = [("message1", "response1"), ("message2", "response2")]
        cleared_chat = self.chat_manager.clear_chat(chat_history)
        self.assertEqual(cleared_chat, [])

    def test_generate_chat_title(self):
        chat_history = [("message1", "response1"), ("message2", "response2")]
        title = self.chat_manager.generate_chat_title(chat_history)
        self.assertIn("message1", title)

    def test_save_chat(self):
        chat_history = [("message1", "response1"), ("message2", "response2")]
        saved_chats = []
        self.chat_manager.save_chat(chat_history, saved_chats)
        self.assertEqual(len(saved_chats), 1)
        self.assertIn("message1", saved_chats[0]["chat"])

    def test_load_chat(self):
        chat_history = [("message1", "response1"), ("message2", "response2")]
        saved_chats = []
        self.chat_manager.save_chat(chat_history, saved_chats)
        loaded_chat = self.chat_manager.load_chat("Neuer Chat", saved_chats, [])
        self.assertEqual(loaded_chat[0], chat_history)

    def test_new_chat(self):
        saved_chats = [{"title": "Chat 1", "chat": [("message1", "response1")]}]
        new_chat = self.chat_manager.new_chat(saved_chats)
        self.assertEqual(new_chat[0], [])
        self.assertEqual(len(new_chat[1]), 1)

    def test_delete_chat(self):
        saved_chats = [{"title": "Chat 1", "chat": [("message1", "response1")]}]
        self.chat_manager.delete_chat("Chat 1", saved_chats)
        self.assertEqual(len(saved_chats), 0)

    def test_delete_all_chats(self):
        saved_chats = [{"title": "Chat 1", "chat": [("message1", "response1")]}]
        self.chat_manager.delete_all_chats()
        self.assertEqual(len(self.chat_manager._load_chats_from_file()), 0)

    def tearDown(self):
        if os.path.exists(SAVE_FILE):
            os.remove(SAVE_FILE)

if __name__ == "__main__":
    unittest.main()

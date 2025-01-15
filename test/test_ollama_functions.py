
import unittest
from unittest.mock import MagicMock
from ollama_functions import OllamaFunctions

class TestOllamaFunctions(unittest.TestCase):
    def setUp(self):
        self.ollama_functions = OllamaFunctions()

    def test_clean_output(self):
        output = "\x1B[1mThis is bold text\x1B[0m"
        result = self.ollama_functions.clean_output(output)
        self.assertNotIn("\x1B", result)

    def test_format_as_codeblock(self):
        output = "This is a code block"
        result = self.ollama_functions.format_as_codeblock(output)
        self.assertIn("```", result)

    def test_format_output(self):
        output = "This is a long text that needs to be formatted with line breaks and code blocks."
        result = self.ollama_functions.format_output(output)
        self.assertIn("\n", result)

    def test_run_ollama_live(self):
        prompt = "Generate a response"
        model = "ollama-model"
        self.ollama_functions.run_ollama_live = MagicMock(return_value=iter(["Response part 1", "Response part 2"]))

        result = list(self.ollama_functions.run_ollama_live(prompt, model))
        self.assertIn("Response part 1", result[0])
        self.assertIn("Response part 2", result[1])

    def test_process_uploaded_file(self):
        file = MagicMock()
        file.name = "test.txt"
        file.read = MagicMock(return_value="File content")

        result = self.ollama_functions.process_uploaded_file(file)
        self.assertEqual(result, "File content")

    def test_compare_documents(self):
        file1 = MagicMock()
        file2 = MagicMock()
        file1.name = "test1.txt"
        file2.name = "test2.txt"
        file1.read = MagicMock(return_value="File 1 content")
        file2.read = MagicMock(return_value="File 2 content")

        result = self.ollama_functions.compare_documents(file1, file2)
        self.assertIn("File 1 content", result)
        self.assertIn("File 2 content", result)

    def test_chatbot_interface(self):
        input_text = "Generate a response"
        model = "ollama-model"
        self.ollama_functions.run_ollama_live = MagicMock(return_value=iter(["Response part 1", "Response part 2"]))

        result = list(self.ollama_functions.chatbot_interface(input_text, model))
        self.assertIn("Response part 1", result[0][1])
        self.assertIn("Response part 2", result[1][1])

if __name__ == "__main__":
    unittest.main()

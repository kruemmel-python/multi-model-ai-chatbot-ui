import unittest
from audio_processing import process_audio

class TestAudioProcessing(unittest.TestCase):
    def test_process_audio(self):
        # Test mit einer gültigen Audiodatei
        result = process_audio("path/to/valid/audio/file.wav")
        self.assertIsNotNone(result)
        self.assertIn("transcribed text", result)

        # Test mit einer ungültigen Audiodatei
        with self.assertRaises(ValueError):
            process_audio("path/to/invalid/audio/file.mp3")

if __name__ == "__main__":
    unittest.main()
import unittest
import os
from moviepy.editor import VideoFileClip

from video_processing import VideoLoadAndMakeSubclip

class TestVideoLoadAndMakeSubclip(unittest.TestCase):
    def setUp(self):
        # Set up a temporary file path for testing
        self.test_file_path = "test_video.mp4"

    def tearDown(self):
        # Clean up the temporary file created during testing
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)

    def test_run_method(self):
        # Create a VideoLoadAndMakeSubclip instance with a test file and output string
        video_processor = VideoLoadAndMakeSubclip(self.test_file_path, "output_test.mp4")

        # Create a dummy video file for testing
        clip = VideoFileClip("path/to/your/input/video.mp4")
        clip.write_videofile(self.test_file_path, codec='libx264', audio_codec='aac')

        # Run the method under test
        result_file_path = video_processor.run()

        # Assert that the result file path is the same as the expected output string
        self.assertEqual(result_file_path, "output_test.mp4")

        # You can add more assertions based on your specific requirements and expected behavior

if __name__ == "__main__":
    unittest.main()

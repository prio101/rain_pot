"""Import Movie Py"""
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

class TextOverVideo:
    """Class for writing text over a video."""
    def __init__(self, text, video_input_path, video_output_path):
        self.text = text
        self.video_input_path = video_input_path
        self.video_output_path = video_output_path


    def run(self):
        """Main Function for the class."""
        # get the video clip
        # get the text string
        # set the text size and color
        # set the text position

        # create new video clip with text
        # write the video clip to the output path

        try:

            video_clip = VideoFileClip(self.video_input_path)

            text_clip = TextClip(self.text, fontsize=30, color='white', font='Amiri-Bold', stroke_width=10)

            text_clip = text_clip.set_pos('center').set_duration(video_clip.duration)

            final_clip = CompositeVideoClip([video_clip, text_clip])

            final_clip.write_videofile(self.video_output_path, codec='libx264', audio_codec='mp3')

            return self.video_output_path

        except FileNotFoundError as e:
            print(f"File not found: {e}")
            return None
        except IOError as e:
            print(f"IO error occurred: {e}")
            return None
        except ImportError as e:
            print(f"An error occurred: {e}")
            return None

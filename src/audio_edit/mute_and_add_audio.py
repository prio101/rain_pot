"""Module providing the MuteAndAddAudio class."""
from moviepy.editor import VideoFileClip, AudioFileClip


class MuteAndAddAudio:
    """This class will deal with adding new sound to the clip"""
    def __init__(self, input_video_path, input_audio_path, output_video_path):
        self.input_video_path = input_video_path
        self.input_audio_path = input_audio_path
        self.output_video_path = output_video_path

    def run(self, input_video_path, input_audio_path, output_video_path):
        """Will convert the video to a muted video and then add the audio to it."""
        try:
            # 1. Mute the video
            muted_video = VideoFileClip(input_video_path).set_audio(None)
            # 2. Add the latest audio to the muted video
            latest_video_with_new_audio = muted_video.set_audio(AudioFileClip(input_audio_path))
            # 3. Write the video with the new audio
            latest_video_with_new_audio.write_videofile(output_video_path,
                codec='libx264', audio_codec='aac')
            # 4. Return the output video path
            return output_video_path
        except FileNotFoundError as e:
            print(f"File not found: {e}")
            return None
        except IOError as e:
            print(f"IO error occurred: {e}")
            return None
        except ImportError as e:
            print(f"An error occurred: {e}")
            return None
        except EOFError as e:
            print(f"An error occurred: {e}")
            return None

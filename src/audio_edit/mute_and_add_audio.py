"""Module providing the MuteAndAddAudio class."""
from moviepy.editor import VideoFileClip, AudioFileClip


class MuteAndAddAudio:
    """This class will deal with adding new sound to the clip"""
    def __init__(self, input_video_path, input_audio_path, output_video_path):
        self.input_video_path = input_video_path
        self.input_audio_path = input_audio_path
        self.output_video_path = output_video_path

    def run(self):
        """Will convert the video to a muted video and then add the audio to it."""
        try:
            # 1. Mute the video
            muted_video = VideoFileClip(self.input_video_path).set_audio(None)
            # 2. Add the latest audio to the muted video
            latest_video_with_new_audio = muted_video.set_audio(
                AudioFileClip(self.input_audio_path))


            # - Get the duration of the total clip
            # - Get the Audio File Duration
            # - Try to put the audio into the video with adhering the video file duration
            # - If the audio file duration is less than the video file duration,
            #   then repeat the audio file until the video file duration

            muted_video_duration = muted_video.duration

            audio_file_duration = AudioFileClip(self.input_audio_path).duration

            if audio_file_duration < muted_video_duration:
                # - Repeat the audio file until the video file duration
                latest_video_with_new_audio = latest_video_with_new_audio.set_audio(
                    AudioFileClip(self.input_audio_path).fx(
                        lambda a: a.audio_loop(duration=muted_video_duration)))
            elif audio_file_duration > muted_video_duration:
                # - Trim the audio file until the video file duration
                latest_video_with_new_audio = latest_video_with_new_audio.set_audio(
                    AudioFileClip(self.input_audio_path).fx(
                        lambda a: a.subclip(t_end=muted_video_duration)))
            else:
                # - Add the audio file to the video file
                latest_video_with_new_audio = latest_video_with_new_audio.set_audio(
                    AudioFileClip(self.input_audio_path))

            # 3. Write the video with the new audio
            latest_video_with_new_audio.write_videofile(self.output_video_path,
                codec='libx264', audio_codec='mp3')
            # 4. Return the output video path
            return self.output_video_path
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

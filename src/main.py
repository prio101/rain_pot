"""Import all classes from audio_edit module."""
from audio_edit.mute_and_add_audio import MuteAndAddAudio
from video_edit.graffiti.text_over_video import TextOverVideo
from video_edit.load_and_subclip import LoadAndSubclip


BASE_PATH = "/home/prio/work/mahabub_llc/python_scripts/video_edit/assets/"

# file_path, file_output_path
FILE_PATH = BASE_PATH+"videos/test2.mp4"
FILE_OUTPUT_PATH = BASE_PATH+"clips/test2-subclip.mp4"

clipper = LoadAndSubclip(FILE_PATH, FILE_OUTPUT_PATH)
clipper.run()


INPUT_VIDEO_PATH = BASE_PATH+"clips/test2-subclip.mp4"
INPUT_AUDIO_PATH = BASE_PATH+"sound/sound-track.mp3"
OUTPUT_VIDEO_PATH = BASE_PATH+"clips/test2-subclip-with-sound.mp4"

# input_video_path, input_audio_path, output_video_path
clip = MuteAndAddAudio(INPUT_VIDEO_PATH, INPUT_AUDIO_PATH, OUTPUT_VIDEO_PATH)

clip.run()

# text, video_input_path, video_output_path
TEXT = "Every next level of \n your life will demand \n a different you."

VIDEO_INPUT_PATH = BASE_PATH+"clips/test2-subclip-with-sound.mp4"
VIDEO_OUTPUT_PATH = BASE_PATH+"clips/test2-subclip-with-sound-and-text.mp4"

clip_with_text = TextOverVideo(TEXT, VIDEO_INPUT_PATH, VIDEO_OUTPUT_PATH)

clip_with_text.run()

"""Import all classes from audio_edit module."""
from src.audio_edit.mute_and_add_audio import MuteAndAddAudio

base_path = "/home/prio/work/mahabub_llc/python_projects/video_editor"

input_video_path = base_path+"/assets/clips/test2-subclip.mp4"
input_audio_path = base_path+"/assets/sound/sound-track.mp3"

# input_video_path, input_audio_path, output_video_path
clip = MuteAndAddAudio()

"""Importing the videoclip"""
from moviepy.editor import *

class LoadAndSubclip:
    """Video Loader and Subclipper"""
    def __init__(self, file_path, file_output_path):
        self.file_path = file_path
        self.file_output_path = file_output_path


    # open the file and write the string to it
    # 1. Create a clip from the origin file.
    # 2. Return the File Path.

    def run(self):
        """Run the main function of the class."""
        movie = VideoFileClip(self.file_path)
        # Set the desired aspect ratio (9:16)
        target_aspect_ratio = 9 / 16
        new_width = int(movie.size[1] * target_aspect_ratio)
        # check if the file is a video file
        # check if the file duration is less than 15 seconds
        # check if file duration is greater than 15 seconds
        movie_duration = movie.duration
        
        if movie_duration < 15:
            print("The video is less than 15 seconds")
            # get a subclip from the origin file but in less and full size
            subclip = movie.subclip(0, movie_duration)
            resized_sub_clip = subclip.resize(width=new_width)
        elif movie_duration > 15:
            # start the normal process
            # get a subclip from the origin file
            subclip = movie.subclip(0, 15)
            resized_sub_clip = subclip.resize(width=new_width)
            # save the subclip into a file
            resized_sub_clip.write_videofile(self.file_output_path,
                codec='libx264', audio_codec='aac')

        # return the file path
        return self.file_output_path

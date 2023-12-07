"""Importing the videoclip"""
from moviepy.editor import VideoFileClip

class LoadAndSubclip:
    """Video Loader and Subclipper"""
    def __init__(self, file_path, str):
        self.file_path = file_path
        self.str = str


    # open the file and write the string to it
    # 1. Create a clip from the origin file.
    # 2. Return the File Path.

    def run(self):
        """Run the main function of the class."""
        movie = VideoFileClip(self.file_path)

        # check if the file is a video file
        # check if the file duration is less than 15 seconds
        # check if file duration is greater than 15 seconds
        movie_duration = movie.duration

        if movie_duration < 15:
        print("The video is less than 15 seconds")
        # get a subclip from the origin file but in less and full size
        subclip = movie.subclip(0, movie_duration)
        elif movie_duration > 15:
        # start the normal process
        # get a subclip from the origin file
        subclip = movie.subclip(0, 15)

        # save the subclip into a file
        subclip.write_videofile(self.str, codec='libx264', audio_codec='aac')

        # return the file path
        return self.str



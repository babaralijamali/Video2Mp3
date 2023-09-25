#pip install moviepy
import os
import moviepy.editor as mp

def convert_video_to_audio(video_path):
    video = mp.VideoFileClip(video_path)
    audio_file = os.path.splitext(video_path)[0] + ".mp3"
    video.audio.write_audiofile(audio_file)

# Get user input
video_file = input("Enter the path to the video file: ")

convert_video_to_audio(video_file)

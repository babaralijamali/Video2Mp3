import os
import moviepy.editor as mp

def convert_video_to_audio(video_path, output_folder):
    video = mp.VideoFileClip(video_path)
    audio_file = os.path.splitext(os.path.basename(video_path))[0] + ".mp3"
    output_path = os.path.join(output_folder, audio_file)
    video.audio.write_audiofile(output_path)

# Get folder paths
video_folder = "video"
output_folder = "converted_mp3_by_bjamali"

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Convert all video files in the folder
for filename in os.listdir(video_folder):
    if filename.endswith(".mp4") or filename.endswith(".avi") or filename.endswith(".mkv"):
        video_path = os.path.join(video_folder, filename)
        convert_video_to_audio(video_path, output_folder)

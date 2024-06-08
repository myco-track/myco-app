'''
# Let the user choose which parts to delete
delete_indices = input(
    "Enter the numbers of the utterances you want to delete, separated by commas: ")
delete_indices = list(map(int, delete_indices.split(',')))

# Calculate the segments to keep
keep_segments = []
current_start = 0
updated_transcript = []

for i, utterance in enumerate(transcript.utterances):
    if i + 1 not in delete_indices:
        keep_segments.append((current_start, utterance.end / 1000))
        updated_transcript.append(
            f"{i + 1}: Speaker {utterance.speaker}: {utterance.text}")
    current_start = utterance.end / 1000

# Update the transcript file to reflect the deletions
with open(transcript_file_path, "w") as file:
    for line in updated_transcript:
        file.write(line + "\n")

# Create the new video by concatenating the kept segments
clips = [video.subclip(start, end) for start, end in keep_segments]
audio_clips = [audio.subclip(start, end) for start, end in keep_segments]
final_video_clip = concatenate_videoclips(clips)
final_audio_clip = concatenate_audioclips(audio_clips)
final_clip = final_video_clip.set_audio(final_audio_clip)

output_file_path = "edited_video.mp4"
final_clip.write_videofile(
    output_file_path, codec="libx264", audio_codec="aac")

print(f"Edited video saved as: {output_file_path}")

# Function to add subtitles to a video using ffmpeg
'''
import os
import assemblyai as aai
from moviepy.editor import VideoFileClip, concatenate_videoclips, concatenate_audioclips
import subprocess


output_file_path = "123.mp4"
transcript="transcript.txt"
def add_subtitles(video_path, subtitles_path, output_path):
    command = [
        "ffmpeg",
        "-i", video_path,
        "-vf", f"subtitles={subtitles_path}",
        "-c:a", "aac",
        output_path
    ]
    subprocess.run(command, check=True)


# Create the SRT content
srt_content = ""
subtitle_counter = 1

for i, utterance in enumerate(transcript.utterances):
    if i + 1 not in delete_indices:
        start_time = utterance.start // 1000
        end_time = utterance.end // 1000
        srt_content += f"{subtitle_counter}\n{start_time // 3600:02}:{(start_time % 3600) // 60:02}:{start_time % 60:02},{utterance.start % 1000:03} --> {end_time // 3600:02}:{(end_time % 3600) // 60:02}:{end_time % 60:02},{utterance.end % 1000:03}\n{utterance.text}\n\n"
        subtitle_counter += 1

srt_file_path = "subtitles.srt"

# Save the SRT content to a file
with open(srt_file_path, "w") as file:
    file.write(srt_content)

print("SRT file created:", srt_file_path)

# Paths to input and output files for adding subtitles
final_output_with_subs = "final_video_with_subtitles.mp4"

# Add subtitles to the video
add_subtitles(output_file_path, srt_file_path, final_output_with_subs)

print("Video with subtitles saved as:", final_output_with_subs)

# Clean up temporary files
os.remove(mp3_file_path)
os.remove(output_file_path)

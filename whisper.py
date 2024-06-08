#python3 -m pip install assemblyai
#python3 -m pip install moviepy

import os
import assemblyai as aai
from moviepy.editor import VideoFileClip, concatenate_videoclips, concatenate_audioclips
import subprocess
import streamlit as st

# Set your AssemblyAI API key
aai.settings.api_key = "d9238deca7624c1cb974b4f0c5aa1b1c"
transcriber = aai.Transcriber()

# Path to the MP4 file
mp4_file_path = "123.mp4"

# Convert MP4 to MP3
mp3_file_path = mp4_file_path.replace(".mp4", ".mp3")
video = VideoFileClip(mp4_file_path)
audio = video.audio
audio.write_audiofile(mp3_file_path)

# Transcribe the audio
config = aai.TranscriptionConfig(speaker_labels=True)
transcript = transcriber.transcribe(mp3_file_path, config)

# Display the transcript and save it to a file
transcript_file_path = "transcript.txt"
with open(transcript_file_path, "w") as file:
    for i, utterance in enumerate(transcript.utterances, start=1):
        file.write(f"{i}: Speaker {utterance.speaker}: {utterance.text}\n")
        print(f"{i}: Speaker {utterance.speaker}: {utterance.text}")
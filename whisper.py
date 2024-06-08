import assemblyai as aai
from moviepy.editor import VideoFileClip

aai.settings.api_key = "d9238deca7624c1cb974b4f0c5aa1b1c"

transcriber = aai.Transcriber()

'''audio_url = (
    "A beautiful mind-John Nash teaches mathematics scene (1080p HD).mp3"
)'''
# Path to the MP4 file
mp4_file_path = "20131015_184626.mp4"

# Convert MP4 to MP3
mp3_file_path = mp4_file_path.replace(".mp4", ".mp3")
video = VideoFileClip(mp4_file_path)
audio = video.audio
audio.write_audiofile(mp3_file_path)

config = aai.TranscriptionConfig(speaker_labels=True)

transcript = transcriber.transcribe(mp3_file_path, config)

print(transcript.text)
transcript_file_path = "transcript.txt"

# Save the transcript to a file
with open(transcript_file_path, "w") as file:
    file.write(transcript.text)

for utterance in transcript.utterances:
    print(f"Speaker {utterance.speaker}: {utterance.text}")



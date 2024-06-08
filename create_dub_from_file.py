import moviepy.editor as mp
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
from pydub import AudioSegment
import os

def extract_audio(video_path, audio_path):
    video = mp.VideoFileClip(video_path)
    video.audio.write_audiofile(audio_path)

def transcribe_audio(audio_path):
    recognizer = sr.Recognizer()
    audio_file = sr.AudioFile(audio_path)
    with audio_file as source:
        audio = recognizer.record(source)
    return recognizer.recognize_google(audio)

def translate_text(text, dest_language):
    translator = Translator()
    return translator.translate(text, dest=dest_language).text

def synthesize_speech(text, dest_audio_path, lang='en'):
    tts = gTTS(text=text, lang=lang)
    tts.save(dest_audio_path)

def merge_audio_with_video(video_path, audio_path, output_path):
    video = mp.VideoFileClip(video_path)
    audio = AudioSegment.from_file(audio_path)
    audio.export(audio_path, format="mp3")
    new_audio = mp.AudioFileClip(audio_path)
    final_video = video.set_audio(new_audio)
    final_video.write_videofile(output_path)

def dub_video(input_video_path, output_video_path, target_language):
    # Step 1: Extract audio from video
    audio_path = "extracted_audio.wav"
    extract_audio(input_video_path, audio_path)
    
    # Step 2: Transcribe the audio
    text = transcribe_audio(audio_path)
    print(f"Transcribed Text: {text}")
    
    # Step 3: Translate the text
    translated_text = translate_text(text, target_language)
    print(f"Translated Text: {translated_text}")
    
    # Step 4: Synthesize speech
    synthesized_audio_path = "synthesized_audio.mp3"
    synthesize_speech(translated_text, synthesized_audio_path, lang=target_language)
    
    # Step 5: Merge new audio with original video
    merge_audio_with_video(input_video_path, synthesized_audio_path, output_video_path)

    # Clean up temporary files
    os.remove(audio_path)
    os.remove(synthesized_audio_path)

# Example usage
input_video = "123.mp4"
output_video = "output_video.mp4"
target_language = "es"  # Spanish
dub_video(input_video, output_video, target_language)

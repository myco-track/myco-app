import os
import uuid
import tkinter as tk
from tkinter import messagebox
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs

# Fetch the ElevenLabs API key from environment variables
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

# Initialize the ElevenLabs client
client = ElevenLabs(api_key=ELEVENLABS_API_KEY)

def list_voices():
    """Mock function to fetch available voices from ElevenLabs."""
    # Replace with actual API call to list voices if available
    return {
        "Adam": "pNInz6obpgDQGcFmaJgB",
        "Alice": "Xb7hH8MSUJpSbSDYk0k2",
        "Sam": "EXAVITQu4vr4xnSDxMaL",
        "Emily": "LcfcDJNUP1GQjkzn1xUU",
        "Charlotte": "XB0fDUnXU5powFXDhCwa",
        "James": "ZQe5CZNOzWyzPSCn5a3c",
        "Charlie": "IKne3meq5aSn9XLyUdCD",
    }

def text_to_speech_file(text: str, voice_id: str) -> str:
    """Convert text to speech and save it to a file using the specified voice ID."""
    response = client.text_to_speech.convert(
        voice_id=voice_id,
        optimize_streaming_latency="0",
        output_format="mp3_22050_32",
        text=text,
        model_id="eleven_multilingual_v2",
        voice_settings=VoiceSettings(
            stability=0.0,
            similarity_boost=1.0,
            style=0.0,
            use_speaker_boost=True,
        ),
    )

    save_file_path = f"{uuid.uuid4()}.mp3"

    with open(save_file_path, "wb") as f:
        for chunk in response:
            if chunk:
                f.write(chunk)

    print(f"{save_file_path}: A new audio file was saved successfully!")
    return save_file_path

def generate_audio():
    """Generate audio based on user input and selected voice."""
    text = text_entry.get("1.0", tk.END).strip()
    if not text:
        messagebox.showerror("Error", "Please enter text to convert to speech.")
        return

    voice_name = voice_var.get()
    voice_id = voices[voice_name]

    try:
        output_file = text_to_speech_file(text, voice_id)
        messagebox.showinfo("Success", f"Audio saved to {output_file}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to generate audio: {e}")

# Fetch available voices
voices = list_voices()

# Create the main application window
root = tk.Tk()
root.title("Text-to-Speech Converter")

# Create a dropdown menu for selecting voices
voice_var = tk.StringVar(root)
voice_var.set("Select a voice")

voice_menu = tk.OptionMenu(root, voice_var, *voices.keys())
voice_menu.pack(pady=10)

# Create a text area for inputting the text
text_entry = tk.Text(root, wrap=tk.WORD, width=50, height=10)
text_entry.pack(pady=10)

# Create a button to generate audio
generate_button = tk.Button(root, text="Generate Audio", command=generate_audio)
generate_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()

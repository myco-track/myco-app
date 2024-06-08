import streamlit as st
import streamlit.components.v1 as components
import subprocess
import time
import os

# Custom CSS for the navigation bar
st.markdown(
    """
    <style>
    .navbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background-color: rgb(46 56 70/var(--tw-bg-opacity));
        padding: 10px 20px;
        border-radius: 8px;
    }
    .navbar img {
        height: 40px;
    }
    .navbar .nav-links {
        display: flex;
        align-items: center;
    }
    .navbar .nav-links a, .navbar .nav-links button {
        color: rgb(46 56 70/var(--tw-bg-opacity));
        margin-left: 20px;
        text-align: center;
        text-decoration: none;
        font-size: 18px;
        font-family: Arial, sans-serif;
        background: none;
        border: none;
        cursor: pointer;
    }
    .navbar .nav-links a:hover, .navbar .nav-links button :hover {
        background-color: rgb(46 56 70/var(--tw-bg-opacity));
        color: black;
        border-radius: 4px;
    }
    .upload-btn-wrapper {
        position: relative;
        overflow: hidden;
        display: inline-block;
        cursor: pointer;
    }
    .upload-btn-wrapper:hover {
        cursor: pointer;
    }
    .upload-btn-wrapper button {
        border: 2px solid #4CAF50;
        color: white;
        background-color: #4CAF50;
        padding: 8px 20px;
        border-radius: 8px;
        font-size: 16px;
        font-weight: bold;
         cursor: pointer;
    }
    .upload-btn-wrapper input[type=file] {
        font-size: 100px;
        position: absolute;
        left: 0;
        top: 0;
        opacity: 0;
         cursor: pointer;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Navbar HTML
st.markdown("""
    <div class="navbar">
        <img src="https://about.myco.io/wp-content/uploads/2022/11/myco-logo-variation-4-500px-300x124.png" alt="Logo" width="100" height="100">
        <div class="nav-links">
            <a href="#search"><img src="https://img.icons8.com/ios-filled/50/ffffff/search.png" ></a>
            <div class="upload-btn-wrapper">
                <button>Upload</button>
                <input type="file" name="upload"/>
            </div>
            <button><img src="https://img.icons8.com/ios-filled/50/ffffff/user.png" height="24"></button>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Title
st.title("Profile")

# State to manage the popup visibility
if "show_popup" not in st.session_state:
    st.session_state.show_popup = False

# Function to toggle popup visibility
def toggle_popup():
    st.session_state.show_popup = not st.session_state.show_popup

# Create a row with four columns for the user image, user name, upload button, and generate button
col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

with col1:
    st.image("https://img.icons8.com/ios-filled/50/ffffff/user.png", width=50)

with col2:
    # Style the username with CSS
    st.markdown("<h2 style='font-weight: bold; font-size: larger; color: white;'>User Name</h2>", unsafe_allow_html=True)

with col4:
    # Upload button with transparent background
   uploade_video_button=st.button("Upload Video", key="upload_video")

with col5:
    # Upload button with transparent background
    create_voiceover_button = st.button("Create Voiceover", key="create_voiceover")

with col6:
    # Upload button with transparent background
    speech_to_text_button = st.button("Create transcript", key="create_transcript")

with col7:
    # Upload button with transparent background
    text_to_speech_button = st.button("Create AI audio", key="create_audio")

# Display the popup HTML conditionally based on the state
if st.session_state.show_popup:
    components.html(
        """
        <div class="popup-overlay"></div>
        <div class="popup">
            <div id="text_input_container">
                <input id="popup_input" type="text" placeholder="Enter text to convert to video" style="border: 1px solid #ccc; padding: 8px; border-radius: 8px; margin-bottom: 10px; width: 70%;">
                <button id="submit_button" style="border: 2px solid teal; color: white; background-color: teal; padding: 10px 20px; border-radius: 8px; font-size: 16px; cursor: pointer;">Submit</button>
            </div>
        </div>
        """,
        height=300
    )

    # Inject the JavaScript to handle the submit button click
    st.markdown(
        """
        <script>
        // Show the popup and overlay when the "Generate Video" button is clicked
        document.querySelector('button[data-testid="stButton"]').addEventListener("click", function() {
            document.querySelector('.popup-overlay').style.display = 'block';
            document.querySelector('.popup').style.display = 'block';
        });

        // Hide the popup and overlay when the close button is clicked
        document.getElementById("submit_button").addEventListener("click", function() {
            document.querySelector('.popup-overlay').style.display = 'none';
            document.querySelector('.popup').style.display = 'none';
        });
        </script>
        """,
        unsafe_allow_html=True
    )

if create_voiceover_button:
    with st.spinner('Generating video...'):
        process = subprocess.Popen(['python3', 'create_dub_from_file.py'])
        while process.poll() is None:
            # Poll the process every second to check if it has finished
            time.sleep(1)

    # Check if the video file exists before trying to display it
    if os.path.exists("/home/sibila/myco-app/output_video.mp4"):
        st.video("/home/sibila/myco-app/output_video.mp4")
    else:
        st.error("Video generation failed.")

if speech_to_text_button:
    with st.spinner('Generating transcript'):
        process = subprocess.Popen(['python3', 'whisper.py'])
        while process.poll() is None:
            # Poll the process every second to check if it has finished
            time.sleep(1)
    with open("/home/sibila/myco-app/transcript.txt", "r") as file:
        content = file.read()
        sentences = content.split('.')
        modified = '.\n'.join(sentences)
    st.text(modified)
    edit_button = st.button("Edit Video")
    caption_button = st.button("Add Caption to Video")
    if edit_button:
        with st.spinner('Generating transcript'):
            process = subprocess.Popen(['python3', 'delete.py'])
            while process.poll() is None:
                    # Poll the process every second to check if it has finished
                    time.sleep(1)
        if os.path.exists("/home/sibila/myco-app/final_video_with_edit.mp4"):
            st.video("/home/sibila/myco-app/final_video_with_edit.mp4")
        else:
            st.error("Video generation failed.")
    if caption_button:
        with st.spinner('Generating transcript'):
            process = subprocess.Popen(['python3', 'CC.py'])
            while process.poll() is None:
                    # Poll the process every second to check if it has finished
                    time.sleep(1)
        if os.path.exists("/home/sibila/myco-app/final_video_with_subtitles.mp4"):
            st.video("/home/sibila/myco-app/final_video_with_subtitles.mp4")
        else:
            st.error("Video generation failed.")
        

if text_to_speech_button:
    with st.spinner('Generating audio'):
        process = subprocess.Popen(['python3', 'text_to_speech_file.py'])
        while process.poll() is None:
            # Poll the process every second to check if it has finished
            time.sleep(1)

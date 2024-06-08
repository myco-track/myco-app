import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="myco", page_icon="https://about.myco.io/wp-content/uploads/2022/11/myco-logo-variation-4-500px-300x124.png", layout="wide")

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
            <div class="upload-btn-wrapper" id="upload-btn-wrapper">
                <button onclick="showPopup()">Upload</button>
                <input type="file" name="upload"/>
            </div>
            <button><img src="https://img.icons8.com/ios-filled/50/ffffff/user.png" height="24"></button>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Custom JavaScript to show the popup
popup_js = """
<script>
function showPopup() {
    document.getElementById("overlay").style.display = "block";
}
</script>
"""

# Display the overlay for the popup
st.markdown('<div id="overlay" class="overlay" style="display: none;"></div>', unsafe_allow_html=True)

# Inject the JavaScript for the popup
st.markdown(popup_js, unsafe_allow_html=True)

# Display the image banner
st.image("/home/sibila/myco-app/banner.png", use_column_width=True)
st.title("New Releases")

# Create a row with three columns for the video images
col1, col2, col3 = st.columns(3)

# Display the video images in the columns
with col1:
    st.image("/home/sibila/myco-app/video.png", use_column_width=True)

with col2:
    st.image("/home/sibila/myco-app/video.png", use_column_width=True)

with col3:
    st.image("/home/sibila/myco-app/video.png", use_column_width=True)
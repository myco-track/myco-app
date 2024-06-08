import streamlit as st

#navbar
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

# Title
st.title("Profile")

# Create a row with three columns for the user image, user name, and upload button
col1, col2, col3 = st.columns(3)

with col1:
    st.image("https://img.icons8.com/ios-filled/50/ffffff/user.png", width=50)

with col2:
    # Style the username with CSS
    st.markdown("<h2 style='font-weight: bold; font-size: larger;'>User Name</h2>", unsafe_allow_html=True)

with col3:
    # Change the color of the button to teal and make the background transparent
    st.markdown(
        "<button style='border-color: teal; background-color: transparent; color: teal; padding: 8px 20px; border-radius: 8px;'>Upload Video</button>",
        unsafe_allow_html=True
    )

import streamlit as st

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

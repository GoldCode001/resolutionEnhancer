import streamlit as st
import requests

# --- PAGE CONFIG ---
st.set_page_config(
    page_title='Media Resolution Enhancer',
    page_icon=":cinema:",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Streamlit UI
st.title('Media Resolution Enhancer')

# File uploader
uploaded_file = st.file_uploader("Upload image or video")

# Processing button
if st.button("Enhance Resolution"):
    if uploaded_file is not None:
        # Send file to backend for processing
        files = {'file': uploaded_file.getvalue()}
        response = requests.post('http://localhost:5000/process', files=files)

        # Display processed media
        if response.status_code == 200:
            st.video(response.content)
            st.markdown("[Download Enhanced Media](http://localhost:5000/download/<filename>)")
        else:
            st.error("Error processing media")

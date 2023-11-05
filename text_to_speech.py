import streamlit as st
from gtts import gTTS
from io import BytesIO
from IPython.display import Audio

# Streamlit app title
st.title("Text-to-Speech with Streamlit")

# Text input area
text = st.text_area("Enter text to convert to speech")

# Language selection (optional, default is English)
language = st.selectbox("Select Language", ["en", "fr", "es", "de","my"])

# Generate and play audio
if st.button("Convert to Speech"):
    if text:
        # Create a gTTS object
        tts = gTTS(text, lang=language)

        # Stream audio without saving to a file
        with BytesIO() as audio_buffer:
            tts.write_to_fp(audio_buffer)
            audio_data = audio_buffer.getvalue()

        # Display the audio using IPython's Audio widget
        st.audio(audio_data, format="audio/ogg", start_time=0)
    else:
        st.warning("Please enter some text before converting to speech.")

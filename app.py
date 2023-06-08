import streamlit as st

from gtts import gTTS

from io import BytesIO

import IPython.display as ipd

st.title("Text-to-Audio Converter")

text = st.text_area("Enter your text here", "")

language = st.selectbox("Select Language", ("en", "es", "fr", "de", "it"))

if st.button("Convert to Audio"):

    if text.strip() != "":

        try:

            tts = gTTS(text, lang=language)

            audio = BytesIO()

            tts.save(audio, format='mp3')

            audio.seek(0)

            st.audio(audio, format='audio/mp3')

        except:

            st.error("Error: Failed to convert text to audio.")

    else:

        st.warning("Please enter some text.")


            

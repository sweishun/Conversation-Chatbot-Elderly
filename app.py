import streamlit as st
import os
from stt import speech_to_text
from text_gen import get_answer
from tts import generate_speech
from audio_recorder_streamlit import audio_recorder
from streamlit_float import *
from gtts import gTTS
import time
import tempfile
# from pydub import AudioSegment


float_init()

def initialize_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Hi! How may I assist you today?"}
        ]
initialize_session_state()

st.title("AyuAI")
# count = 0

footer_container = st.container()
with footer_container:
    audio_bytes = audio_recorder()

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if audio_bytes:
    with st.spinner("Transcribing..."):
        # webm_file_path = "temp_audio.mp3"
        # with open(webm_file_path, "wb") as f:
        #     f.write(audio_bytes)

        transcript = speech_to_text(audio_bytes)
        # if transcript:
        st.session_state.messages.append({"role": "user", "content": transcript})
        final_response = get_answer(st.session_state.messages)
        with st.chat_message("user"):
            st.write(transcript)
            # os.remove(webm_file_path)

# if st.session_state.messages[-1]["role"] != "assistant":
    
    with st.chat_message("assistant"):
        # with st.spinner("Thinking..."):
        
            # time.sleep(2)
        # with st.spinner("Generating audio response..."):
        generate_speech(final_response)
        st.write(final_response)
        st.session_state.messages.append({"role": "assistant", "content": final_response})
    
    
        

    
    os.remove("tmp.mp3")
footer_container.float("bottom: 0rem;")

            # Using Pydub
            # audio = AudioSegment.from_wav(tts)
            # audio.export("reply_audio.mp3", format="mp3")
            # time.sleep(2)
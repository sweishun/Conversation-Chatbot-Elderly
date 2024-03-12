import streamlit as st
import base64
from gtts import gTTS

audio_file_path = "tmp.mp3"

def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f: 
        data = f.read()
    b64 = base64.b64encode(data).decode("utf-8")
    md = f"""
    <audio autoplay>
    <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
    </audio>
    """
    st.markdown(md, unsafe_allow_html=True)

def generate_speech(response_msg):
    try:
        tts = gTTS(response_msg, lang='en', slow=False)
        tts.save(audio_file_path)
        print("Audio file saved.")

        # Assuming this function plays the audio file
        autoplay_audio(audio_file_path)
        print("Playback initiated.")
        
    except Exception as e:
        print(f"Error during audio generation or playback: {e}")




# API_URL = "https://api-inference.huggingface.co/models/microsoft/speecht5_tts"
# headers = {"Authorization": f"Bearer {os.getenv('HUGGINGFACE_TOKEN')}"}

# def query(payload):
# 	response = requests.post(API_URL, headers=headers, json=payload)
# 	return response.content

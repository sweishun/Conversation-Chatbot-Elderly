from transformers import pipeline

pipe = pipeline("automatic-speech-recognition", model="openai/whisper-base")

def speech_to_text(audio_data):
    transcript = pipe(audio_data)['text']
    return transcript
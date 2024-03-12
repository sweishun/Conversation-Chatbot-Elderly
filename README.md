# Conversation-Chatbot-Elderly
A conversational chatbot designed to target social isolation and loneliness for the elderly.

There are three main segments to the conversational chatbot. 

First, a Speech-To-Text LLM to convert the user's speech to the input text. 
Second, the input text wil be fed into a text-generation model (Mistral-7b) using the HuggingFace Inference API.
Third, the generated text will be converted into speech using Google's Python package gTTS for quicker inference times. 

This prototype is hosted on streamlit. 

import streamlit as st
import requests

# --- CONFIG ---
API_KEY = "AIzaSyCmz5zNxmQC-wjTREXNLZmfFMeH4zBsgAQ"
# جربنا v1 بدل v1beta لأنها أكثر استقراراً
URL = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={API_KEY}"

st.set_page_config(page_title="MedResearch AI", page_icon="🔬")
st.title("🔬 MedResearch AI Assistant")

user_input = st.text_input("Enter your research topic:")

if st.button("Analyze ✨"):
    if user_input:
        payload = {
            "contents": [{"parts": [{"text": user_input}]}]
        }
        try:
            response = requests.post(URL, json=payload)
            result = response.json()
            
            if response.status_code == 200:
                answer = result["candidates"][0]["content"]["parts"][0]["text"]
                st.markdown(answer)
                st.success("Success!")
            else:
                st.error(f"Error {response.status_code}: {result.get('error', {}).get('message', 'Unknown error')}")
        except Exception as e:
            st.error(f"Connection Error: {e}")

import streamlit as st
import requests

# --- الإعدادات ---
API_KEY = "AIzaSyCmz5zNxmQC-wjTREXNLZmfFMeH4zBsgAQ"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

st.set_page_config(page_title="MedResearch AI", page_icon="🔬")
st.title("🔬 MedResearch AI Assistant")

user_input = st.text_input("Enter your medical research topic:")

if st.button("Analyze"):
    if user_input:
        # تجهيز البيانات للإرسال
        payload = {
            "contents": [{
                "parts": [{"text": f"You are a medical researcher. Analyze: {user_input}"}]
            }]
        }
        
        try:
            response = requests.post(URL, json=payload)
            result = response.json()
            
            # عرض النتيجة
            if "candidates" in result:
                answer = result["candidates"][0]["content"]["parts"][0]["text"]
                st.markdown(answer)
                st.success("Done!")
            else:
                st.error(f"API Error: {result}")
        except Exception as e:
            st.error(f"Connection Error: {e}")

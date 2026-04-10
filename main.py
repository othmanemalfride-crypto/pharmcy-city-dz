import streamlit as st
import google.generativeai as genai

# حط المفتاح تاعك هنا
API_KEY = "AIzaSyCmz5zNxmQC-wjTREXNLZmfFMeH4zBsgAQ" 

genai.configure(api_key=API_KEY)

# طريقة ذكية لتفادي خطأ 404
try:
    model = genai.GenerativeModel('gemini-1.5-flash')
except:
    model = genai.GenerativeModel('gemini-pro') # نسخة احتياطية

st.set_page_config(page_title="MedResearch AI", page_icon="🔬")

st.title("🔬 MedResearch AI")
user_input = st.text_input("Ask about medical research:")

if st.button("Analyze"):
    if user_input:
        try:
            # نحدد الإصدار v1beta يدوياً في الطلب
            response = model.generate_content(user_input)
            st.write(response.text)
        except Exception as e:
            st.error(f"Error details: {e}")

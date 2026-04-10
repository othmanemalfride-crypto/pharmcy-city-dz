import streamlit as st
import google.generativeai as genai

# --- CONFIGURATION ---
API_KEY = "AIzaSyCmz5zNxmQC-wjTREXNLZmfFMeH4zBsgAQ" 

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('models/gemini-1.5-flash')

# --- UI SETTINGS ---
st.set_page_config(page_title="MedResearch AI", page_icon="🔬", layout="wide")

# القائمة الجانبية (Sidebar) - هادي تزيد الاحترافية
with st.sidebar:
    st.title("👨‍💻 Developer Info")
    st.write("Project: AI Medical Analyst")
    st.write("Goal: Global Research Support")
    st.divider()
    st.info("هذا النظام مخصص لتحليل الأبحاث الطبية وتلخيص الدراسات العالمية.")

# الواجهة الرئيسية
st.title("🔬 MedResearch AI Assistant")
st.subheader("Your Gateway to Global Medical Insights")

# خانة البحث
user_input = st.text_area("Enter a drug name, symptoms, or a link to a medical paper:", 
                         placeholder="e.g., Clinical trials of Metformin in 2024...")

col1, col2 = st.columns([1, 5])
with col1:
    analyze_btn = st.button("Analyze ✨")

if analyze_btn:
    if user_input:
        with st.spinner("Analyzing global database..."):
            try:
                # الـ Prompt الجديد: نخبر الـ AI يتصرف كخبير عالمي
                prompt = f"""
                You are a world-class Medical Research Assistant. 
                Analyze the following request with academic precision:
                Request: {user_input}
                
                Please provide:
                1. Executive Summary (Brief).
                2. Key Scientific Findings.
                3. Safety & Clinical Considerations.
                
                Answer in English and provide a brief Arabic summary at the end.
                """
                
                response = model.generate_content(prompt)
                
                # عرض النتيجة في إطار جميل
                st.markdown("### 📊 Research Analysis")
                st.write(response.text)
                st.success("Analysis Completed Successfully!")
                
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter some text to analyze.")



import streamlit as st
import google.generativeai as genai


API_KEY ="AIzaSyCmz5zNxmQC-wjTREXNLZmfFMeH4zBsgAQ"

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# إعدادات واجهة المستخدم
st.set_page_config(page_title="فارماسي سيتي-دي زد", page_icon="💊")
st.title("🤖 مساعد الصيدلي الذكي - فارماسي سيتي")
st.markdown("---")

# خانة إدخال السؤال
user_question = st.text_input("اسأل أي سؤال عن الأدوية أو التفاعلات الدوائية:", placeholder="مثلاً: ما هي دواعي استعمال Gaviscon؟")

if st.button("تحليل الآن"):
    if user_question:
        with st.spinner('جاري جلب أدق المعلومات...'):
            try:
                # توجيه الـ AI
                prompt = f"أنت خبير صيدلاني في الجزائر. أجب بدقة علمية وباللغة التي سأل بها المستخدم عن: {user_question}"
                response = model.generate_content(prompt)
                
                st.subheader("النتيجة:")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"حدث خطأ في الاتصال: {e}")
    else:
        st.warning("يرجى كتابة سؤالك أولاً!")

st.sidebar.markdown("### عن التطبيق")
st.sidebar.info("هذا التطبيق يستعمل الذكاء الاصطناعي (Gemini) لمساعدة الصيادلة في الجزائر.")

import streamlit as st
import google.generativeai as genai

# This pulls your API key safely from the cloud settings
# Change the long string to "GEMINI_API_KEY"
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("🚀 AI Skill Gap Analyzer")
role = st.text_input("Target Job Role")
resume = st.text_area("Paste Resume Text")

if st.button("Analyze"):
    if role and resume:
        with st.spinner("Analyzing..."):
            prompt = f"Identify skill gaps for {role} based on: {resume}. Give a 4-week roadmap."
            response = model.generate_content(prompt)
            st.markdown(response.text)

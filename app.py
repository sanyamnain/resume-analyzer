import streamlit as st
from utils import extract_text, get_similarity, get_missing_skills

st.title("📄 Resume Analyzer")

uploaded_file = st.file_uploader("Upload your resume (PDF)", type="pdf")
job_description = st.text_area("Paste Job Description")

if uploaded_file is not None and job_description.strip() != "":
    
    try:
        resume_text = extract_text(uploaded_file)

        if resume_text.strip() == "":
            st.error("Could not extract text from PDF")
        else:
            score = get_similarity(resume_text, job_description)
            missing_skills = get_missing_skills(resume_text)

            st.subheader("📊 Results")
            st.write(f"Match Score: {score:.2f}%")

            st.write("⚠️ Missing Skills:")
            st.write(missing_skills)

    except Exception as e:
        st.error(f"Error: {e}")

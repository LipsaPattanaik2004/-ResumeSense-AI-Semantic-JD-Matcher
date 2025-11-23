import streamlit as st
from src.resume_matcher import match_resume_to_jd

st.title("ResumeSense AI – Semantic JD Matcher")

resume_text = st.text_area("Paste Resume Text")
jd_text = st.text_area("Paste Job Description")

if st.button("Match"):
    if resume_text.strip() and jd_text.strip():
        score, matched_skills = match_resume_to_jd(resume_text, jd_text)
        st.subheader(f"Match Score: {score:.2f}%")
        st.write("Matched Skills:", matched_skills)
    else:
        st.warning("Please paste both Resume and Job Description.")

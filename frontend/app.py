import streamlit as st
import requests
import os

BACKEND_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:8000")


st.title(
"AI Resume Analyzer"
)

uploaded_file=st.file_uploader(

"Upload Resume",
type=["pdf"]

)

jd=st.text_area(

"Paste Job Description"

)


if st.button("Analyze"):
    if not uploaded_file or not jd:
        st.error("Please upload a resume and paste a job description.")
    else:
        files={
            "file": (uploaded_file.name, uploaded_file.getvalue(), "application/pdf")
        }

        data={
            "jd":jd
        }

        with st.spinner("Analyzing..."):
            response=requests.post(
                f"{BACKEND_URL}/analyze",
                files=files,
                data=data
            )
            
            if response.status_code == 200:
                result=response.json()
                
                st.metric(
                    "ATS Score",
                    result["ATS Score"]
                )

                st.subheader("ATS Breakdown")

                st.write(
                    f"Skill Score: {result['Skill Score']:.2f}"
                )

                st.write(
                    f"Semantic Score: {result['Semantic Score']:.2f}"
                )

                st.write(
                    f"Experience Score: {result['Experience Score']:.2f}"
                )

                st.write(
                    f"Education Score: {result['Education Score']:.2f}"
                )

                st.write(
                    f"Structure Score: {result['Structure Score']:.2f}"
                )

                st.write(
                    f"Achievement Score: {result['Achievement Score']:.2f}"
                )
                

                st.subheader("Skills")
                st.write(result["Resume Skills"])

                st.subheader("Missing Skills")
                st.write(result["Missing Skills"])

                st.subheader("AI Feedback")
                st.write(result["AI Feedback"])
            else:
                st.error(f"Error {response.status_code}: {response.text}")
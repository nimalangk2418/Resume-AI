from pdf  import read_pdf
import streamlit as st
import os 
import google.generativeai as genai
genai.configure(api_key = os.getenv("Google_api"))

model = genai.GenerativeModel("gemini-2.0-flash")

# Read the pdf 

def profile(resume,job_desc):
    if resume is not None:
        resume_doc = read_pdf(resume)
        st.markdown("Resume is uploaded")
    else:
        st.warning("Resume not uploaded")
    response = model.generate_content(f'''Act as a Data Analyst or Business Analyst role in any domain and compare {resume} with {job_desc}
and suggest - What are the Chances of getting selected?''')
    # return Resume insights 
    return(st.write(response.text))
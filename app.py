from dotenv import load_dotenv
load_dotenv() # Activate the local environment variables
# 
import streamlit as st # for html codes 
import google.generativeai as genai
from pdf import read_pdf
from analysis import profile

# Create the front end page 
st.header(":blue[Resume Analysis] Using AI", divider = "green")
st.subheader("Tips for using the Application")
st.sidebar.subheader("Upload the Resume 👇")
resume = st.sidebar.file_uploader(label = "Upload your Resume 📝",type = ["pdf"])

notes = f'''
* **Upload the Resume:** This ia GenAI Powered APP to extract insights.
* **Job Description:** Copy Paste the Job Description from Job Boards 
* **Unleash The Power of Gen AI Model:** Click on the Button to get Insights.
'''
st.write(notes)

# Job Desc 
st.subheader("Enter Job Description 🔡",divider = True)

job_desc = st.text_area(label = "Copy Paste Job Desc", max_chars = 10000)

button = st.button(label = "Get AI Powered Insights")
if button:
    st.markdown(profile(resume=resume,job_desc=job_desc))

import streamlit as st
import google.generativeai as genai
import os
import pdfplumber 

from dotenv import load_dotenv

load_dotenv() ## load all the enviornment varables

#api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key='')

## Gemini pro response
def get_gemini_response(input):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input)
    return response.text



def input_pdf_text(uploaded_file):
    text = ""
    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

#def input_pdf_text(uploaded_file):
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page_num in reader(len(reader.pages)):
        page = reader.pages[page_num]
        text+=str(page.extract_text())
    return text


## Prompt template

input_prompt = """ Hey act like a skilled or very experience ATD(Application Tracking System) with a deep understanding of tech field, software engineering, data science, 
data analyst and bidg data engineer. Your task is to evaluate the resume based on the given job description. You must consider the job market is very competitive and you 
should provide best assitance for improving the resume. Assign the percentage MAtching based on jd(Job description) and the missing keywords with high accuracy. 
resume:{text} 
description: {jd}
I want the response in one single string having the stucture {{"JD Match":"%", MissingKeywords:[]","ProfileSummary":""}}
"""

## streamlit app

st.title("Smart ATS")
st.text("Improve Your Resume ATS")
jd=st.text_area("PAste the Job description")
uploaded_file=st.file_uploader("Upload Your Resume",type="pdf",help="Please upload the pdf")

submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        text=input_pdf_text(uploaded_file)
        response=get_gemini_response(input_prompt)
        st.subheader(response)

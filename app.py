
import streamlit as st
from openai import OpenAI
from PyPDF2 import PdfReader
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="centered"
)

st.title("📄 AI Resume Analyzer")
st.write("Upload your resume PDF and extract important details using AI.")

# API key
api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    st.error("API key not found. Please configure your .env file.")
    st.stop()

# OpenRouter client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key
)

# File uploader
uploaded_file = st.file_uploader(
    "Upload your Resume (PDF)",
    type=["pdf"]
)

if uploaded_file is not None:

    st.success("Resume uploaded successfully!")

    if st.button("🔍 Analyze Resume"):

        with st.spinner("Extracting resume text..."):

            try:
                # Read PDF
                reader = PdfReader(uploaded_file)

                text = ""

                for page in reader.pages:
                    extracted_text = page.extract_text()

                    if extracted_text:
                        text += extracted_text + "\n"

                if not text.strip():
                    st.error("Could not extract text from this PDF.")
                    st.stop()

                # System prompt
                system_prompt = {
                    "role": "system",
                    "content": """
You are a resume information extraction assistant.

Extract the following details from the resume:

1. Name
2. Education
3. Skills
4. Experience
5. Email
6. Phone Number

Return the result in a well-structured format using Markdown.

Do not invent information.
If a field is missing, write "Not Mentioned".
"""
                }

                # User prompt
                user_prompt = {
                    "role": "user",
                    "content": text
                }

                # AI response
                response = client.chat.completions.create(
                    model="openrouter/free",
                    messages=[
                        system_prompt,
                        user_prompt
                    ]
                )

                result = response.choices[0].message.content

                # Display result
                st.subheader("📋 Extracted Resume Details")
                st.markdown(result)

                # Download result
                st.download_button(
                    label="📥 Download Analysis",
                    data=result,
                    file_name="resume_analysis.md",
                    mime="text/markdown"
                )

            except Exception as e:
                st.error(f"An error occurred: {e}")

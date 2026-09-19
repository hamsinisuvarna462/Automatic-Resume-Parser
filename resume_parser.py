

# !pip install PyPDF2

from openai import OpenAI

from google.colab import userdata
api_key = userdata.get('openrouter-api')

model = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=api_key)

from PyPDF2 import PdfReader

reader = PdfReader("Aditya_Gunge_resume_2026.pdf")
page = reader.pages[0]
text = page.extract_text()

system_prompt = {"role":"system","content":"""
Extract name, education, skills, experience, email, and phone number from resume text given by user. output should be well structured."""}

user_prompt = {"role":"user", "content":text}

responce = model.chat.completions.create(model="openrouter/free",messages=[system_prompt,user_prompt])

from IPython.display import display,Markdown

display(Markdown(responce.choices[0].message.content))


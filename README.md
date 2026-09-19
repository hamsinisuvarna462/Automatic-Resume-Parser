
# 📄 AI Resume Analyzer

An AI-powered Resume Analyzer built using **Python, Streamlit, PyPDF2, and OpenRouter API**.

This application allows users to upload a PDF resume and automatically extract important information such as Name, Education, Skills, Experience, Email, and Phone Number using AI.

---

## 🚀 Features

- 📄 Upload resume in PDF format
- 🔍 Extract text from PDF using PyPDF2
- 🤖 AI-powered resume analysis
- 🧑‍💻 Extract Name and Education
- 🛠️ Extract Skills
- 💼 Extract Experience
- 📧 Extract Email Address
- 📞 Extract Phone Number
- 📋 Display structured resume details
- 📥 Download analysis as a Markdown file
- 🔐 Secure API key handling using environment variables

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Streamlit | Web Application Framework |
| PyPDF2 | PDF Text Extraction |
| OpenAI SDK | API Client |
| OpenRouter | AI Model API |
| python-dotenv | Environment Variables |

---

## 📁 Project Structure

```text
resume_analyzer/
│
├── app.py
├── requirements.txt
├── .env
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/hamsinisuvarna462/Automatic-Resume-Parser.git
```

### 2. Navigate to Project Folder

```bash
cd Automatic-Resume-Parser
```

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

---

## 🔑 API Key Configuration

This project uses the OpenRouter API.

### Step 1: Get API Key

Visit:

https://openrouter.ai/

Create an account and generate an API key.

### Step 2: Create `.env` File

Inside the project folder, create a file named:

```text
.env
```

Add the following:

```env
OPENROUTER_API_KEY=your_openrouter_api_key
```

**Important:** Never share your API key publicly or upload `.env` to GitHub.

---

## ▶️ Run the Application

Run the following command in the terminal:

```bash
streamlit run app.py
```

The application will open in your browser.

Default URL:

```text
http://localhost:8501
```

---

## 🔄 Working Methodology

1. User uploads a resume in PDF format.
2. Streamlit receives the uploaded file.
3. PyPDF2 extracts text from the PDF.
4. Extracted text is sent to the OpenRouter AI model.
5. AI analyzes the resume information.
6. Extracted details are displayed in a structured format.
7. User can download the analysis.

---

## 📊 Information Extracted

The application extracts:

- **Name**
- **Education**
- **Skills**
- **Experience**
- **Email**
- **Phone Number**

If any information is missing, the AI returns "Not Mentioned".

---

## 🧪 Testing

The application can be tested using different PDF resumes.

| Test Case | Expected Result |
|-----------|-----------------|
| Upload valid PDF | Resume uploaded successfully |
| Upload non-PDF file | File upload rejected |
| Upload empty PDF | Text extraction error |
| Upload resume with details | Information extracted |
| Missing resume information | Displays "Not Mentioned" |
| Missing API key | Configuration error |

---

## 🔮 Future Enhancements

- 📈 ATS Score Calculation
- 🎨 Improved User Interface
- 📊 Resume Skill Analysis
- 📄 Download Results as PDF
- 🧠 Resume Improvement Suggestions
- 🗂️ Multiple Resume Comparison
- ☁️ Deployment on Streamlit Cloud

---

## 👨‍💻 Author

**Hamsini Suvarna**

B.Tech Computer Science Engineering (AI & ML)

Rai Technology University, Bangalore

---

## 📜 License

This project is created for educational and academic purposes.

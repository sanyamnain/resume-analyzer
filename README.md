# 📄 Resume Analyzer

A simple NLP-based Resume Analyzer that compares a candidate's resume with a job description and provides a match score, missing skills, and improvement suggestions.

---

## 🚀 Features

- 📥 Upload resume (PDF)
- 📊 Match score using TF-IDF & Cosine Similarity
- 🧠 Identify missing skills
- 🔍 Keyword matching analysis
- 📧 Extract email from resume
- 📏 Resume length analysis
- 💡 Suggestions to improve resume

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Scikit-learn
- PyPDF2
- Regex (re)

---

## ⚙️ How It Works

1. Upload a resume in PDF format  
2. Paste a job description  
3. The system:
   - Extracts text from resume  
   - Converts text into vectors using TF-IDF  
   - Computes similarity using cosine similarity  
   - Identifies missing skills  
   - Generates suggestions  

---

## 📊 Example Output

- Match Score: 75%  
- Missing Skills: SQL, Machine Learning  
- Resume Length: 320 words  
- Suggestions:
  - Add missing skills  
  - Improve resume content  

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py

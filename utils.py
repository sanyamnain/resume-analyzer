import PyPDF2
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# -------- Resume Text Extraction --------
def extract_text(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    
    for page in reader.pages:
        text += page.extract_text()
        
    return text


# -------- Similarity Function --------
def get_similarity(resume, jd):
    tfidf = TfidfVectorizer()
    vectors = tfidf.fit_transform([resume, jd])
    score = cosine_similarity(vectors[0:1], vectors[1:2])
    
    return score[0][0] * 100


# -------- Skills Matching --------
skills_list = ["python", "sql", "machine learning", "excel"]

def get_missing_skills(resume_text):
    resume_text = resume_text.lower()
    missing = []
    
    for skill in skills_list:
        if skill not in resume_text:
            missing.append(skill)
            
    return missing
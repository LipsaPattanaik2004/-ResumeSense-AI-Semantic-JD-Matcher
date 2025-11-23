from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

def embed(text):
    return model.encode([text])[0]

def match_resume_to_jd(resume_text, jd_text):
    emb_resume = embed(resume_text)
    emb_jd = embed(jd_text)

    score = cosine_similarity([emb_resume], [emb_jd])[0][0]
    score = (score + 1) / 2 * 100  # scale 0–100%

    matched_skills = extract_keywords(resume_text, jd_text)

    return score, matched_skills

def extract_keywords(resume, jd):
    resume_words = set(resume.lower().split())
    jd_words = set(jd.lower().split())

    matched = resume_words.intersection(jd_words)
    return list(matched)

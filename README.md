# ResumeSense AI – Semantic Job Description Matcher
ResumeSense AI is an NLP-powered project that analyzes resumes and job descriptions, computes semantic similarity, and provides intelligent match scoring using transformer embeddings.

## Features
Semantic similarity using Sentence-BERT / Transformer models
Resume parsing for skills, experience, education
Job description keyword extraction & gap analysis
Clean modular code in /src
Jupyter notebooks for experiments
Ready for extension into ATS or dashboard

## Project Structure
ResumeSense-AI/
│
├── app/                 # App-level runnable scripts
├── assets/              # Icons, images, diagrams
├── data/                # Sample resume & JD text files
├── docs/                # Documentation, PDFs
├── notebooks/           # Jupyter notebooks
├── src/                 # Core NLP & model logic
└── README.md

## Tech Stack
Python 3.10+
Transformers (BERT, SBERT)
scikit-learn
Pandas / NumPy
NLTK / SpaCy
Jupyter Notebook

## How It Works
Load resume and job description
Preprocess text
Generate embeddings using transformer model
Compute cosine similarity
Output match score, strengths, missing skills

## How to Run
git clone https://github.com/<your-username>/ResumeSense-AI.git
cd ResumeSense-AI
pip install -r requirements.txt


## Run notebooks & app:
jupyter notebook
python app/main.py
Example OutputMatch Score: 82.6%
Matched Skills: Python, NLP, PandasMissing Skills: Docker, Airflow

## Future Enhancements
Flask/FastAPI deployment
Skill-gap recommendation system
Batch processing for multiple resumes
Recruiter-friendly dashboard

# LIPSA || ITER SOA UNIVERSITY || AI • ML • NLP 

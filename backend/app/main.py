from fastapi import FastAPI
from fastapi import UploadFile,File,Form
import shutil
import os
from dotenv import load_dotenv

load_dotenv("../../.env")

from services.parser import parse_pdf
from services.extractor import extract_skills
from services.extractor import extract_experience
from services.embeddings import semantic_similarity
from services.ats import calculate_skill_score
from services.skill_gap import skill_gap_analysis
from services.feedback import generate_feedback

from services.extractor import extract_education

from services.quality import (
    structure_score,
    achievement_score
)

from services.ats import (
    calculate_skill_score,
    calculate_experience_score,
    calculate_education_score,
    calculate_ats_score
)


app=FastAPI()

UPLOAD_FOLDER="../../uploads"

os.makedirs(
UPLOAD_FOLDER,
exist_ok=True
)


@app.post("/analyze")

async def analyze(

file:UploadFile=File(...),
jd:str=Form(...)

):

    filepath=os.path.join(

UPLOAD_FOLDER,
file.filename

)

    with open(
        filepath,
        "wb"
    ) as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    resume_text=parse_pdf(
        filepath
    )

    resume_skills=extract_skills(
        resume_text
    )

    jd_skills=extract_skills(
        jd
    )

    experience=extract_experience(
        resume_text
    )

    education = extract_education(
    resume_text
    )

    jd_experience = extract_experience(
    jd
    )

    jd_education = extract_education(
    jd
    )

    skill_score=calculate_skill_score(

        resume_skills,
        jd_skills

    )

    semantic_score=semantic_similarity(

        resume_text,
        jd

    )

    education_score = (
    calculate_education_score(
        education,
        jd_education
    )
    )

    structure = structure_score(
    resume_text
    )

    achievement = achievement_score(
    resume_text
    )

    experience_score = (
    calculate_experience_score(
        experience,
        jd_experience
    )
    )

    ats = calculate_ats_score(

    skill_score,
    semantic_score,
    experience_score,
    education_score,
    structure,
    achievement

    )

    missing=skill_gap_analysis(

        resume_skills,
        jd_skills

    )

    feedback=generate_feedback(

        resume_text,
        jd

    )

    return {

    "ATS Score": ats,

    "Skill Score": skill_score,

    "Semantic Score": semantic_score,

    "Experience Score": experience_score,

    "Education Score": education_score,

    "Structure Score": structure,

    "Achievement Score": achievement,

    "Resume Skills": resume_skills,

    "Missing Skills": missing,

    "AI Feedback": feedback

}
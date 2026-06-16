def calculate_skill_score(
    resume_skills,
    jd_skills
):

    if len(jd_skills) == 0:
        return 0

    matched = set(
        resume_skills
    ).intersection(
        set(jd_skills)
    )

    return (
        len(matched)
        /
        len(jd_skills)
    ) * 100


def calculate_experience_score(
    resume_exp,
    jd_exp
):

    if jd_exp == 0:
        return 100

    return min(
        resume_exp / jd_exp,
        1
    ) * 100


def calculate_education_score(
    resume_edu,
    jd_edu
):

    if jd_edu == 0:
        return 100

    return min(
        resume_edu / jd_edu,
        1
    ) * 100


def calculate_ats_score(

    skill_score,
    semantic_score,
    experience_score,
    education_score,
    structure_score,
    achievement_score

):

    ats = (

        skill_score * 0.30 +

        semantic_score * 0.20 +

        experience_score * 0.20 +

        education_score * 0.10 +

        structure_score * 0.10 +

        achievement_score * 0.10

    )

    return round(ats, 2)
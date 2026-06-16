def skill_gap_analysis(

resume_skills,
jd_skills

):

    missing=list(

        set(jd_skills)-set(
            resume_skills
        )
    )

    return missing
import re


SKILLS_DB=[

"python",
"machine learning",
"deep learning",
"tensorflow",
"pytorch",
"sql",
"docker",
"kubernetes",
"fastapi",
"streamlit",
"nlp",
"aws",
"azure",
"java",
"c++",
"pandas",
"numpy"
]


def extract_skills(text):

    text=text.lower()

    found=[]

    for skill in SKILLS_DB:

        if skill in text:

            found.append(skill)

    return list(set(found))


def extract_experience(text):

    pattern=r'(\d+)\+?\s*(years|year)'

    matches=re.findall(pattern,text.lower())

    if matches:

        years=max([int(x[0]) for x in matches])

        return years

    return 0


def extract_education(text):

    text = text.lower()

    education_map = {
        "phd": 4,
        "doctorate": 4,
        "m.tech": 3,
        "mtech": 3,
        "master": 3,
        "ms": 3,
        "b.tech": 2,
        "btech": 2,
        "bachelor": 2,
        "bsc": 1
    }

    highest = 0

    for degree, rank in education_map.items():

        if degree in text:

            highest = max(highest, rank)

    return highest
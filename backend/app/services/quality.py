def structure_score(text):

    sections = [
        "skills",
        "education",
        "experience",
        "projects",
        "certifications",
        "summary"
    ]

    found = 0

    text = text.lower()

    for section in sections:

        if section in text:
            found += 1

    return (found / len(sections)) * 100

import re

def achievement_score(text):

    achievements = re.findall(
        r'\d+%|\d+\s*(million|thousand|k)',
        text.lower()
    )

    count = len(achievements)

    if count == 0:
        return 20

    elif count <= 2:
        return 50

    elif count <= 5:
        return 80

    else:
        return 100
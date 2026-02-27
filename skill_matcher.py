skills_list = [
    "python", "machine learning", "data analysis",
    "html", "css", "java", "c++", "sql",
    "deep learning", "nlp", "flask", "javascript"
]

required_skills = [
    "python", "machine learning", "data analysis", "nlp"
]

roles = {
    "AI Engineer": ["python", "machine learning", "deep learning", "nlp"],
    "Web Developer": ["html", "css", "javascript", "flask"],
    "Data Analyst": ["python", "data analysis", "sql"],
    "Software Developer": ["java", "c++", "python"]
}

def detect_skills(resume_text):
    resume_text = resume_text.lower()
    detected = []

    for skill in skills_list:
        if skill in resume_text:
            detected.append(skill)

    return detected


def suggest_missing(detected):
    missing = []

    for skill in required_skills:
        if skill not in detected:
            missing.append(skill)

    return missing


def calculate_score(detected):
    total_skills = len(required_skills)
    score = (len(detected) / total_skills) * 100
    return int(score)


def detect_role(detected):
    role_scores = {}

    for role, role_skills in roles.items():
        match = len(set(detected) & set(role_skills))
        role_scores[role] = match

    best_role = max(role_scores, key=role_scores.get)
    return best_role
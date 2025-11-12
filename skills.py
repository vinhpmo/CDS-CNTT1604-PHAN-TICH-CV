import re

def extract_skills(text, technical_skills, soft_skills):
    """
    """
    text_lower = text.lower()
    technical = set(skill for skill in technical_skills if re.search(r'\b' + re.escape(skill) + r'\b', text_lower))
    soft = set(skill for skill in soft_skills if re.search(r'\b' + re.escape(skill) + r'\b', text_lower))
    return list(technical), list(soft)
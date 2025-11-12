def analyze_education_and_experience(text, education_keywords, experience_keywords):
    """
    Phân tích học vấn và kinh nghiệm dựa trên từ khóa.
    - Duyệt qua từng dòng, chuyển section khi gặp từ khóa.
    - Lọc bỏ dòng trống và tiêu đề.
    """
    lines = text.split('\n')
    education = []
    experience = []
    in_education = False
    in_experience = False

    for line in lines:
        line_lower = line.lower().strip()
        if not line_lower:
            continue  

        if any(kw in line_lower for kw in education_keywords):
            in_education = True
            in_experience = False
            continue  
        elif any(kw in line_lower for kw in experience_keywords):
            in_experience = True
            in_education = False
            continue  

        if in_education:
            education.append(line.strip())
        if in_experience:
            experience.append(line.strip())

    return education, experience
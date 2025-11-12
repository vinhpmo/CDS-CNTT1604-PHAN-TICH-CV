import re

def calculate_score(personal_found, education_found, experience_found, skills_count, text):
    score = 0

    if personal_found:
        score += 20

    if education_found:
        score += 20
        if len(re.findall(r'\b(năm|số năm|bằng cấp)\b', text.lower())) > 0:
            score += 5

    if experience_found:
        score += 20
        exp_text = ' '.join(re.findall(r'kinh nghiệm.*?(?=học vấn|kỹ năng|$)', text.lower(), re.DOTALL))
        if len(exp_text.split()) > 50:
            score += 5

    skills_bonus = min(skills_count * 4, 40)
    if re.search(r'(kỹ năng|skills):.*?\.', text, re.DOTALL):
        skills_bonus += 5
    score += min(skills_bonus, 40)

    return min(score, 100)

def get_improvements(personal_found, education_found, experience_found, skills_count, text):
    suggestions = []

    if not personal_found:
        suggestions.append(
            "Thiếu thông tin cá nhân đầy đủ (tên, email, số điện thoại). Hãy đặt ở đầu CV với format rõ ràng.")

    if not education_found or len(text.split()) < 100:
        suggestions.append(
            "Phần học vấn chưa chi tiết. Thêm năm học, bằng cấp, điểm số hoặc thành tích.")

    if not experience_found or len(re.findall(r'\d+ năm', text.lower())) == 0:
        suggestions.append(
            "Kinh nghiệm làm việc thiếu hoặc không cụ thể. Mô tả vai trò, thành tựu với số liệu (ví dụ: 'Tăng doanh thu 20%').")

    if skills_count < 5:
        suggestions.append(
            f"Chỉ có {skills_count} kỹ năng. Thêm kỹ năng liên quan đến vị trí, phân loại rõ kỹ thuật và mềm.")

    if len(text.split()) < 300:
        suggestions.append(
            "CV quá ngắn. Mở rộng mô tả để đạt ít nhất 300 từ.")

    if not re.search(r'\n\s{2,}', text) and not re.search(r'^\s*-\s', text, re.MULTILINE):
        suggestions.append(
            "Format chưa chuẩn. Sử dụng bullet points (-), khoảng trắng, hoặc bold cho tiêu đề.")

    return suggestions

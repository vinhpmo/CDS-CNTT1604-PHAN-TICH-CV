import streamlit as st
import json
import tempfile
from utils.extract_text import extract_text_from_file
from utils.personal_info import extract_personal_info
from utils.analyze_sections import analyze_education_and_experience
from utils.skills import extract_skills
from utils.evaluation import calculate_score, get_improvements
from utils.visualization import (
    display_personal_info,
    display_sections,
    display_skills,
    display_evaluation,
    display_suggestions,
    display_charts
)

# Đọc dữ liệu keywords
with open('data/keywords.json', 'r', encoding='utf-8') as f:
    keywords = json.load(f)

# ------------------------
# Giao diện Streamlit
# ------------------------
st.set_page_config(page_title="Đánh Giá CV Tự Động", layout="wide")

with st.sidebar:
    st.title("👤 Thông tin & Hướng dẫn")
    st.info("""
    1️⃣ Tải lên CV của bạn (định dạng `.txt`, `.docx`, `.pdf`, `.jpg`, `.png`).  
    2️⃣ Hệ thống sẽ tự động trích xuất nội dung.  
    3️⃣ Phân tích các phần: **Thông tin cá nhân, Học vấn, Kinh nghiệm, Kỹ năng.**  
    4️⃣ Hiển thị điểm đánh giá và gợi ý cải thiện CV.  
    5️⃣ Xem biểu đồ trực quan và nội dung CV gốc.
    """)
    st.markdown("---")
    st.markdown("### 👨‍💼 Nguyễn Thế Vinh – 1671020355")

st.title("🤖 Hệ thống Đánh Giá CV Tự Động")
st.write("Tải lên CV của bạn để hệ thống tiến hành phân tích chi tiết!")

# ------------------------
# Upload file CV
# ------------------------
uploaded_file = st.file_uploader(
    "📂 Chọn file CV (.docx, .txt, .pdf, .jpg, .png)",
    type=['docx', 'txt', 'pdf', 'jpg', 'jpeg', 'png']
)

if uploaded_file is not None:
    try:
        # ⚙️ Lưu file tạm để đảm bảo các thư viện (pdf, ảnh) đọc được
        with tempfile.NamedTemporaryFile(delete=False, suffix=f"_{uploaded_file.name}") as tmp_file:
            tmp_file.write(uploaded_file.getbuffer())
            temp_path = tmp_file.name

        # ✅ Trích xuất văn bản từ file tạm
        text = extract_text_from_file(temp_path)

        if text:
            st.success("✅ Đã tải lên và trích xuất văn bản thành công!")

            # ------------------------
            # PHÂN TÍCH THÔNG TIN
            # ------------------------
            name, email, phone = extract_personal_info(text)
            personal_found = all([
                name != "Không tìm thấy",
                email != "Không tìm thấy",
                phone != "Không tìm thấy"
            ])

            education, experience = analyze_education_and_experience(
                text,
                keywords['education_keywords'],
                keywords['experience_keywords']
            )
            education_found = len(education) > 0
            experience_found = len(experience) > 0

            technical, soft = extract_skills(
                text,
                keywords['technical_skills'],
                keywords['soft_skills']
            )
            skills_count = len(technical) + len(soft)

            score = calculate_score(
                personal_found, education_found, experience_found, skills_count, text
            )
            suggestions = get_improvements(
                personal_found, education_found, experience_found, skills_count, text
            )

            # ------------------------
            # HIỂN THỊ KẾT QUẢ
            # ------------------------
            st.subheader("📌 Kết quả phân tích")
            display_personal_info(name, email, phone)
            display_sections(education, experience)
            display_skills(technical, soft)
            display_evaluation(score, personal_found, education_found, experience_found, skills_count)
            display_suggestions(suggestions)
            display_charts(technical, soft, education, experience)

            with st.expander("📄 Xem nội dung CV gốc"):
                st.text_area("Nội dung CV:", text, height=300)

    except Exception as e:
        st.error(f"❌ Lỗi xử lý file: {str(e)}")

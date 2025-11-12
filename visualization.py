import streamlit as st
import plotly.express as px


def display_personal_info(name, email, phone):
    """Hiển thị thông tin cá nhân với metric."""
    st.subheader("📋 Thông tin cá nhân")
    col1, col2, col3 = st.columns(3)
    col1.metric("Tên", name)
    col2.metric("Email", email)
    col3.metric("Số điện thoại", phone)


def display_sections(education, experience):
    """Hiển thị học vấn và kinh nghiệm với list."""
    st.subheader("🎓 Học vấn")
    if education:
        for item in education[:10]:  
            st.write(f"- {item}")
    else:
        st.info("Không tìm thấy phần học vấn.")

    st.subheader("💼 Kinh nghiệm làm việc")
    if experience:
        for item in experience[:10]:
            st.write(f"- {item}")
    else:
        st.info("Không tìm thấy phần kinh nghiệm.")


def display_skills(technical, soft):
    """Hiển thị kỹ năng với columns."""
    st.subheader("🛠️ Kỹ năng")
    col_t, col_s = st.columns(2)
    with col_t:
        st.write("**Kỹ năng kỹ thuật:**")
        if technical:
            for skill in technical:
                st.write(f"- {skill.capitalize()}")
        else:
            st.info("Không tìm thấy kỹ năng kỹ thuật.")
    with col_s:
        st.write("**Kỹ năng mềm:**")
        if soft:
            for skill in soft:
                st.write(f"- {skill.capitalize()}")
        else:
            st.info("Không tìm thấy kỹ năng mềm.")


def display_evaluation(score, personal_found, education_found, experience_found, skills_count):
    """Hiển thị đánh giá với metric và table."""
    st.subheader("📊 Đánh giá tổng quan")
    st.metric("Điểm CV (0-100)", score)

    st.subheader("Bảng điểm chi tiết")
    data = {
        "Tiêu chí": ["Thông tin cá nhân", "Học vấn", "Kinh nghiệm", "Kỹ năng"],
        "Điểm": [20 if personal_found else 0, 20 if education_found else 0, 20 if experience_found else 0,
                 min(skills_count * 4, 40)],
        "Trạng thái": ["✅" if personal_found else "❌", "✅" if education_found else "❌",
                       "✅" if experience_found else "❌", f"✅ ({skills_count} kỹ năng)"]
    }
    st.table(data)


def display_suggestions(suggestions):
    """Hiển thị gợi ý với warning."""
    st.subheader("💡 Gợi ý cải thiện")
    if suggestions:
        for sug in suggestions:
            st.warning(sug)
    else:
        st.success("CV khá hoàn chỉnh! Không có gợi ý lớn.")


def display_charts(technical, soft, education, experience):
    """Vẽ biểu đồ với Plotly (tương tác)."""
    st.subheader("📈 Biểu đồ phân tích")
    col1, col2 = st.columns(2)

    # Biểu đồ tròn tỷ lệ kỹ năng
    with col1:
        skills_data = {'Kỹ năng': ['Kỹ thuật', 'Mềm'], 'Số lượng': [len(technical), len(soft)]}
        fig_pie = px.pie(skills_data, values='Số lượng', names='Kỹ năng', title='Tỷ lệ kỹ năng')
        st.plotly_chart(fig_pie, use_container_width=True)

    # Biểu đồ cột phân bố nội dung (dựa trên số từ)
    with col2:
        edu_words = len(' '.join(education).split())
        exp_words = len(' '.join(experience).split())
        skills_words = len(' '.join(technical + soft).split())
        total = edu_words + exp_words + skills_words
        if total > 0:
            distribution = {
                'Phần': ['Học vấn', 'Kinh nghiệm', 'Kỹ năng'],
                '%': [(edu_words / total) * 100, (exp_words / total) * 100, (skills_words / total) * 100]
            }
            fig_bar = px.bar(distribution, x='Phần', y='%', title='Phân bố nội dung CV')
            st.plotly_chart(fig_bar, use_container_width=True)
        else:
            st.info("Không đủ dữ liệu để vẽ biểu đồ phân bố.")
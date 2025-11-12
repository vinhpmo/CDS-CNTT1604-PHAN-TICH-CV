<h2 align="center">
    <a href="https://dainam.edu.vn/vi/khoa-cong-nghe-thong-tin">
        🎓 Faculty of Information Technology (DaiNam University)
    </a>
</h2>

<h2 align="center">
    ỨNG DỤNG TRA CỨU THỜI TIẾT ONLINE 
</h2>

<div align="center">
    <p align="center">
        <img src="dosc/aiotlab_logo.png" alt="AIoTLab Logo" width="170"/>
        <img src="dosc/fitdnu_logo.png" alt="FIT Logo" width="180"/>
        <img src="dosc/dnu_logo.png" alt="DaiNam University Logo" width="200"/>
    </p>

[![AIoTLab](https://img.shields.io/badge/AIoTLab-green?style=for-the-badge)](https://www.facebook.com/DNUAIoTLab)
[![Faculty of Information Technology](https://img.shields.io/badge/Faculty%20of%20Information%20Technology-blue?style=for-the-badge)](https://dainam.edu.vn/vi/khoa-cong-nghe-thong-tin)
[![DaiNam University](https://img.shields.io/badge/DaiNam%20University-orange?style=for-the-badge)](https://dainam.edu.vn)

</div>

## 1. Giới thiệu hệ thống

**CVAnalyzer** là một hệ thống mã nguồn mở giúp tự động phân tích hồ sơ ứng tuyển (CV/Resume). Hệ thống:
- Trích xuất thông tin chính: tên, liên hệ, học vấn, kinh nghiệm, kỹ năng.
- Chuẩn hóa và nhận diện kỹ năng.
- So sánh kỹ năng với mô tả công việc (job description) bằng embeddings để đưa ra **điểm phù hợp** (suitability score).
- Giao diện web đơn giản được xây bằng Streamlit để người dùng upload file và xem kết quả.
👉 **Điểm nổi bật**:
-- Hỗ trợ PDF, DOCX, TXT input.
- Kết hợp rule-based và embeddings (SentenceTransformers).
- Giao diện Streamlit thân thiện, export kết quả CSV.
- Dễ cài đặt, dễ mở rộng.
- 
## 🔧 2. Công nghệ & Ngôn ngữ sử dụng
- Python 3.9+
- Streamlit
- pdfminer.six / python-docx / textract
- spaCy / transformers
- sentence-transformers
- rapidfuzz

## 🚀 3. Một số hình ảnh

### Giao diện chính 
![Client Interface](dosc/ui_home.png)

### Kết quả tra của phân tích

** Thông tin phân tích

![Weather Result](dosc/charts.png)

** Biểu đồ phân tích

![Weather Result](dosc/chart_skills.png)

**Sơ đồ luồng

![Weather Result](dosc/architecture.png)

** Yêu thích

![Weather Result](docs/giaodienyeutich.png)


## 📝 4. Các bước cài đặt

### 1) Clone project
```bash
git clone https://github.com/yourusername/CVAnalyzer.git
cd CVAnalyzer
```

### 2) Tạo virtual environment và cài dependencies
```bash
python -m venv venv
source venv/bin/activate  # Unix / macOS
venv\Scripts\activate     # Windows

pip install -r requirements.txt
```

### 3) Chạy Streamlit app
```bash
streamlit run app.py
```

Giao diện sẽ mở ở `http://localhost:8501`. Upload CV (PDF/DOCX/TXT) và nhập (tùy chọn) job description để xem điểm phù hợp.

## 📞 5. Liên hệ

Nếu có thắc mắc hoặc cần hỗ trợ, vui lòng liên hệ:
```bash
📍 Địa chỉ: Hà Đông, Hà Nội

📧 Email: vinhvh010204@gmail.com

📞 Điện thoại: 098567****

© 2025 - Khoa Công nghệ thông tin - Trường Đại học Đại Nam
 ```



















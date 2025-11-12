import os
from docx import Document

def extract_text_from_file(file_path):
    """
    Hàm trích xuất nội dung văn bản từ các định dạng file:
    - .docx
    - .txt
    - .pdf
    - .jpg / .jpeg / .png

    Giữ nguyên logic cũ, mở rộng thêm khả năng đọc PDF và ảnh.
    """

    ext = os.path.splitext(file_path)[1].lower().strip()

    # -------- DOCX --------
    if ext == ".docx":
        try:
            doc = Document(file_path)
            text = "\n".join([p.text for p in doc.paragraphs if p.text.strip() != ""])
            return text
        except Exception as e:
            return f"Lỗi khi đọc file DOCX: {e}"

    # -------- TXT --------
    elif ext == ".txt":
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return f.read()
        except Exception:
            # fallback nếu file không phải UTF-8
            with open(file_path, "r", encoding="latin-1") as f:
                return f.read()

    # -------- PDF --------
    elif ext == ".pdf":
        try:
            import fitz  # PyMuPDF
            text = ""
            with fitz.open(file_path) as pdf:
                for page in pdf:
                    text += page.get_text()
            return text if text.strip() else "Không tìm thấy nội dung văn bản trong PDF."
        except Exception as e:
            return f"Lỗi khi đọc file PDF: {e}\n(Hãy cài: pip install PyMuPDF)"

    # -------- ẢNH (JPG, PNG) --------
    elif ext in [".jpg", ".jpeg", ".png"]:
        try:
            from PIL import Image
            import pytesseract

            # Mở ảnh và nhận dạng văn bản
            img = Image.open(file_path)
            text = pytesseract.image_to_string(img, lang="vie+eng")
            return text if text.strip() else "Không nhận dạng được chữ trong ảnh."
        except Exception as e:
            return f"Lỗi khi đọc ảnh: {e}\n(Hãy cài: pip install pytesseract Pillow)"

    # -------- KHÔNG HỖ TRỢ --------
    else:
        return "Định dạng file này chưa được hỗ trợ (chỉ hỗ trợ .docx, .txt, .pdf, .jpg, .png)."

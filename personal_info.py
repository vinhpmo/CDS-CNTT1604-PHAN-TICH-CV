import re


def extract_personal_info(text):
    """
    """
    lines = text.split('\n')
    name = lines[0].strip() if lines and re.match(r'^[A-ZÀ-Ỹ][a-zà-ỹ]+(?:\s[A-ZÀ-Ỹ][a-zà-ỹ]+)+$',
                                                  lines[0].strip()) else "Không tìm thấy"

    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    email = re.findall(email_pattern, text)
    email = email[0] if email else "Không tìm thấy"

    phone_pattern = r'(?:\+84|0)(?:[1-9][0-9]{8,9})\b'
    phone = re.findall(phone_pattern, text)
    phone = phone[0] if phone else "Không tìm thấy"

    return name, email, phone
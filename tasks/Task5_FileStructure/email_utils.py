import re

def is_email_valid(email):
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    if re.match(pattern, email):
        return True
    return False

def get_email_domain(email):
    if not is_email_valid(email):
        raise ValueError("Invalid email address")
    return email.split('@')[1]
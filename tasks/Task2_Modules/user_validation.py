def is_valid_email(email):
    try:
        if '@' in email:
            username, domain = email.split('@')
            if username and domain:
                *d1, d2 = domain.split('.')
                if ''.join(d1) and d2:
                    return True
    except ValueError:
        print("Invalid Email!")
        return False
        
    return False


def is_valid_name(name):
    return name and not name.isdigit()
def password_checker():
    password = input("Enter password: ")
    if len(password) >= 8 and any(c.isdigit() for c in password) and any(c.isupper() for c in password):
        print("Strong password!")
    else:
        print("Weak password! Use at least 8 chars, include numbers & uppercase letters.")

password_checker()
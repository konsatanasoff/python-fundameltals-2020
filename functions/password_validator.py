def password_check(password):
    is_valid = True
    if not 6 <= len(password) <= 10:
        print("Password must be between 6 and 10 characters")
        is_valid = False

    digit_count = 0
    for el in password:
        if el.isdigit():
            digit_count += 1

        if not el.isdigit() and not el.isalpha():
            print("Password must consist only of letters and digits")
            is_valid = False
            break

    if digit_count < 2:
        print("Password must have at least 2 digits")
        is_valid = False

    return is_valid


password = input()

if password_check(password):
    print("Password is valid")

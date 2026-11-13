import random
import string


def validate_password(password):

    if len(password) < 8:
        return False

    has_letter = False
    has_digit = False
    has_symbol = False

    for char in password:

        if char.isalpha():
            has_letter = True

        elif char.isdigit():
            has_digit = True

        else:
            has_symbol = True

    return has_letter and has_digit and has_symbol


def validate_ip(ip):

    parts = ip.split(".")

    if len(parts) != 4:
        return False

    for part in parts:

        if not part.isdigit():
            return False

        if int(part) < 0 or int(part) > 255:
            return False

    return True


def generate_password():

    length = random.randint(10, 16)

    characters = string.ascii_letters + string.digits + string.punctuation

    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password
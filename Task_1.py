import random
import string

def generate_password(length, include_digits=True, include_symbols=True, min_digits=1, min_symbols=1):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation  

    if length <= 0:
        print("Password length should be greater than zero.")
        return None
    min_letters = 1  
    if include_digits:
        min_letters += min_digits
    if include_symbols:
        min_letters += min_symbols

    if length < min_letters:
        print(f"Password length should be at least {min_letters} to satisfy the minimum requirements.")
        return None
    password = []
    password.append(random.choice(lowercase_letters))
    password.append(random.choice(uppercase_letters))

    if include_digits:
        password.extend(random.choices(digits, k=min_digits))
    if include_symbols:
        password.extend(random.choices(symbols, k=min_symbols))

    remaining_length = length - len(password)
    password.extend(random.choices(lowercase_letters + uppercase_letters + digits + symbols, k=remaining_length))
    random.shuffle(password)
    generated_password = ''.join(password)

    return generated_password

def get_user_input():
    try:
        length = int(input("Enter the desired length of the password: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return None, None, None, None

    include_digits = input("Include digits (yes/no)? ").lower() == 'yes'
    include_symbols = input("Include symbols (yes/no)? ").lower() == 'yes'

    if include_digits:
        try:
            min_digits = int(input("Minimum number of digits: "))
        except ValueError:
            print("Invalid input for minimum digits. Defaulting to 1.")
            min_digits = 1
    else:
        min_digits = 0

    if include_symbols:
        try:
            min_symbols = int(input("Minimum number of symbols: "))
        except ValueError:
            print("Invalid input for minimum symbols. Defaulting to 1.")
            min_symbols = 1
    else:
        min_symbols = 0

    return length, include_digits, include_symbols, min_digits, min_symbols

print("Welcome to the Password Generator!")
length, include_digits, include_symbols, min_digits, min_symbols = get_user_input()
if length is not None:
    password = generate_password(length, include_digits, include_symbols, min_digits, min_symbols)
    if password:
        print(f"Generated Password: {password}")
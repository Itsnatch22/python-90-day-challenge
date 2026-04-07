uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'
special_symbols = '!@#$%^&*()_+-=[]{}|;:,.<>?'

password = input("Enter a password: ")

def password_checker(password: str) -> bool:
    if len(password) < 8:
        return False
    if not any(char in uppercase_letters for char in password):
        return False
    if not any(char in lowercase_letters for char in password):
        return False
    if not any(char in digits for char in password):
        return False
    if not any(char in special_symbols for char in password):
        return False
    return True

print(password_checker(password))
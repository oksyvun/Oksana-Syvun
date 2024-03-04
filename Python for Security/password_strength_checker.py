import re

def check_password_strength(password):
    # Check length
    if len(password) < 12:
        return "Weak: Password should be at least 12 characters long."

    # Check for lowercase and uppercase letters
    if not any(char.islower() for char in password) or not any(char.isupper() for char in password):
        return "Weak: Password should include both lowercase and uppercase letters."

    # Check for numbers
    if not any(char.isdigit() for char in password):
        return "Weak: Password should include at least one number."

    # Check for special characters
    special_characters = r"[!@#$%^&*()_+{}[\]:;<>,.?/~`'\"\\|]"
    if not re.search(special_characters, password):
        return "Weak: Password should include at least one special character."

    # Check for common patterns
    common_patterns = ['123', 'password', 'qwerty', 'admin']
    if any(pattern in password for pattern in common_patterns):
        return "Weak: Password contains a common pattern or word."

    return "Strong: Password meets all criteria for strength."

# Example usage:
password = input("Enter your password: ")
result = check_password_strength(password)
print(result)

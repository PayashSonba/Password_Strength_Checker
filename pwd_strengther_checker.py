import re

# Common weak passwords (short sample, expand this in practice)
common_passwords = {'password', '123456', 'qwerty', 'letmein', 'admin'}

from typing import Tuple, List

def score_password(password: str) -> Tuple[int, List[str]]:
    score = 0
    suggestions: List[str] = []

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        suggestions.append("Password should be at least 8 characters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add an uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add a lowercase letter.")

    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Add a number.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        suggestions.append("Add a special character (!@#$%^&*(),.?\":{}|<>).")

    if password.lower() in common_passwords:
        score = 0
        suggestions.append("This password is too common. Choose something more unique.")

    return score, suggestions

def strength_label(score: int) -> str:
    if score >= 5:
        return "Very Strong"
    elif score == 4:
        return "Strong"
    elif score == 3:
        return "Moderate"
    elif score == 2:
        return "Weak"
    else:
        return "Very Weak"

def main():
    password = input("Enter your password: ")
    score, suggestions = score_password(password)
    label = strength_label(score)
    print(f"Password strength: {label} (score: {score}/6)")
    if suggestions:
        print("Suggestions to improve your password:")
        for s in suggestions:
            print(" -", s)

if __name__ == "__main__":
    main()

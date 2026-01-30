import re

def check_password_strength(password: str):
    score = 0
    feedback = []

    # 1) Length Check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Password is too short (minimum 8 characters recommended).")

    # 2) Uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least 1 uppercase letter (A-Z).")

    # 3) Lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least 1 lowercase letter (a-z).")

    # 4) Numbers
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add at least 1 number (0-9).")

    # 5) Special characters
    if re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]", password):
        score += 1
    else:
        feedback.append("Add at least 1 special character (!@#$...).")

    # 6) Common weak passwords check
    common_passwords = ["password", "123456", "qwerty", "admin", "password123"]
    if password.lower() in common_passwords:
        feedback.append("This password is very common. Choose something unique.")
        score = 0  # force weak

    # Strength level
    if score <= 2:
        strength = "Weak ❌"
    elif score <= 4:
        strength = "Medium ⚠️"
    else:
        strength = "Strong ✅"

    return strength, feedback


def main():
    print("\n--- Password Complexity Checker ---")
    password = input("Enter your password: ")

    strength, feedback = check_password_strength(password)

    print("\nPassword Strength:", strength)

    if feedback:
        print("\nSuggestions to improve:")
        for item in feedback:
            print("•", item)
    else:
        print("\n✅ Great! Your password is strong.")


if __name__ == "__main__":
    main()

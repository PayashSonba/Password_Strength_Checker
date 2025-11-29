# Password Strength Checker 🔐

A smart console tool that analyzes password strength with regex checks, scoring, and personalized improvement suggestions. Detects length, character types, and common weak passwords.

## Description 🎯

Scores passwords (0-6) based on length (8+ chars), uppercase/lowercase letters, numbers, special characters, and blocks common passwords like "123456". Provides actionable suggestions like "Add uppercase letter". Perfect for learning regex patterns and structured function design.

## Features ✨

- 📏 **Length scoring** (12+ = +2pts, 8+ = +1pt)
- 🔤 **Regex checks** for uppercase, lowercase, digits, symbols
- 🚫 **Common password blacklist**
- 📊 **Strength labels** (Very Strong → Very Weak)
- 💡 **Personalized improvement suggestions**

## Demo 🎮

Enter your password: MyPass123!
Password strength: Strong (score: 4/6)
Suggestions to improve your password:

Add a special character (!@#$%^&*(),.?":{}|<>).


## Learning Outcomes 📚
- Regex pattern matching `[A-Z]`, `\d`, special chars
- Type hints with `Tuple[int, List[str]]`
- Defensive programming with suggestions

## Future Ideas 🚀
- 🎲 Password generator
- 📈 Historical strength tracking
- 🌐 Web interface

## Author

Built by Payash Sonbarsa for internship portfolio preparation.



# Email-Validator
# Email Address Validator (Python)

A simple Python program that checks whether an email address is valid based on basic rules.  
This project is beginner-friendly and focuses on clean logic and user interaction.

---

## 📌 Features

- Checks if the email contains:
  - Exactly one `@` symbol
  - A `.` after the `@`
  - No spaces
- Runs continuously until the user chooses to exit
- Clear success and error messages
- Easy to read and modify

---

## 🛠️ How It Works

The program uses a function to validate the email address:
- Ensures there is exactly one `@`
- Ensures a `.` exists after the `@`
- Rejects emails containing spaces

The validation logic is separated from user interaction, making the code cleaner and reusable.

---

## ▶️ How to Run

1. Make sure Python is installed  
   Check with:
   ```bash
   python --version

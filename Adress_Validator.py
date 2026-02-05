def is_valid_email(address):
    if " " in address:
        return False

    if address.count("@") != 1:
        return False

    at_index = address.find("@")
    dot_index = address.find(".", at_index)

    if dot_index == -1:
        return False

    return True


print("Email Validator")
print("A valid email must contain one '@' and a '.' after it")
print("Type 'exit' to quit\n")

while True:
    email = input("Enter your email address: ")

    if email.lower() == "exit":
        print("Goodbye!")
        break

    if is_valid_email(email):
        print("Valid email\n")
    else:
        print("Invalid email\n")
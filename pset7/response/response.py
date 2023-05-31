import validators

email = input("What's your email?")
is_valid = validators.email(email)
if is_valid:
    print("Valid")
else:
    print("Invalid")
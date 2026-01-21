password=input("Enter your password: ")
has_upper=False
has_lower=False
has_digit=False
has_special=False
special_characters="!@#$%^&*()-+"
for char in password:
    if char.isupper():
        has_upper=True
    elif char.islower():
        has_lower=True
    elif char.isdigit():
        has_digit=True
    elif char in special_characters:
        has_special=True
if has_upper and has_lower and has_digit and has_special and len(password)>=8:
    print("Strong password")
elif len(password)<6 and has_lower and has_digit:
    print("Medium password")
else:
    print("Weak password")
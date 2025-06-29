while True:
    password = input("Create a passord: ")
    size = len(password)
    minimum = False
    lowercase = False
    uppercase = False
    digit = False

    if size >= 8:
        minimum = True
    for i in password:
        if i.isupper():
            uppercase = True
        if i.lower():
            lowercase = True
        if i.isdigit():
            digit = True
    valid = True
    if not minimum:
        print("It should have 8 characters or more")
        minimum = False
    if not lowercase:
        print("It should have a lowercase character")
        lowercase = False
    if not uppercase:
        print("It should have an uppercase")
        uppercase = False
    if not digit:
        print("It should have atleast a digit")
        digit = False
    if valid:
        print("Successful!")
        break

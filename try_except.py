try:
    age = int(input("Enter age: "))
    if age <= 0:
        raise ValueError("Your age can't be negative")

    else:
        print(f"your age is {age}")
except ValueError as e:
    print("Enter valid age")
finally:
    print("Success")

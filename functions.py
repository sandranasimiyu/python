def greetings(name, age=29, course="cs"):
    print(f"{name} {age} {course}")


greetings("Sandra")
greetings("greg", "sweet", 5)


def configure_email(recipient, subject="No Subject", body=""):
    print(f"To: {recipient}")
    print(f"Subject: {subject}")
    print(f"Body: {body}")
    print("-" * 10)


# Using defaults for subject and body
configure_email("user@example.com")

# Overriding only the subject using a keyword argument
configure_email("another@example.com", subject="Important Meeting")

# Overriding both, using keyword arguments for clarity and flexibility
configure_email(recipient="admin@example.com",
                body="Please reset my password.", subject="Password Reset Request")

# The positional argument for recipient still works
configure_email("marketing@example.com",
                body="Check out our new product!", subject="New Product Launch!")

def user_profile(username, city, email, **additional_info):
    print(f"Profile for {username}")
    print(f"You are from {city}")
    print(f"Your email is {email}")
    print(additional_info)
    return ""


print(user_profile("Sandra", "Nairobi",
      "sandranasimiyu6@gmail.com", number="0742667199"))

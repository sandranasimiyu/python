

def check(num):
    if (num % 2 == 0):
        return "Even"
    else:
        return "odd"


print("enter a number:")
number = int(input())

print(check(number))

def factorial(num):

    if num == 0:
        return 1

    elif num < 0:
        return "Enter a large number"
    else:
        fact = 1
        for i in range(1, num + 1):
            fact *= i
        return fact


print("Enter a number:")
number = int(input())
print(factorial(number))

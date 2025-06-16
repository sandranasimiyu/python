
def sum(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total


print(sum(1, 2, 3))


def items(*my_items):
    print("heyy")
    print(f"my items are: {my_items}")
    return ""


print(items("cake", "hot dogs"))

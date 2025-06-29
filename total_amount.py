initial_total = int(input("Enter initial total: "))
tip = int(input("What percentage of tip would you like to give: "))

tip_amount = (tip / 100) * initial_total
total = initial_total + tip_amount

print(f"Initial total: ${initial_total}")
print(f"Tip percentage: {tip}%")
print(f"Tip amount: ${tip_amount}")
print(f"Total: ${total}")

if total >= 100:
    print("Wow, that's a big bill!")

current = 0
previous = 0
sum = 0

print(current, previous, sum)


for i in range(9):
    current++
    previous = current - 1
    sum = current + previous
    print(f"Current Number {current} Previous Number{previous} Sum: {sum}")

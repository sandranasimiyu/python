previous = 0
current = 1
next = 0
print(previous)
print(current)
for i in range(2):
    sum = previous + current
    previous = current
    current = sum
    print(current)

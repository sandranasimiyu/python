import math
x = [1, 2, 3, 4]
print(x[0])
x.append(1)
print(x)
x.pop()
print(x)
x.sort()
print(x)

print(x.index(1))

dict1 = {1: 'ONE', 2: "HEYY"}
print(dict1)
print(dict1.keys())
print(dict1.values())
dict1 = {"India": "IN", "Russia": "RU", "Australia": "AU"}
dict1.update({"Canada": "CA"})
print(dict1)
dict1.pop("Australia")
print(dict1)
dict1 = {"India": "IN", "Russia": "RU", "Australia": "AU"}
print(sorted(dict1))

print(dict1.get(12, "not found"))
print(dict1.get("India"))

keys = ['navin', 'yes', 'sandra', 'no']
values = ['python', 'c', 'c++', 'js']
data = dict(zip(keys, values))
print(data['no'])

data['why'] = "heyy"
print(data)

# del ('navin')
print(data)

num = 10
print(id(num))
for x in range(1, 5):
    print(x)
a = 6
b = 8
print(a < b)
print(a > 5 and b < 0)
print(a > 5 or b < 0)

print(bin(10))
print(0xF)
print(0b1101)

x = 25
print(math.sqrt(x))
x = 2.5
print(math.floor(x))
print(math.ceil(x))
print(math.pow(3, 2))
print(math.e * 2)

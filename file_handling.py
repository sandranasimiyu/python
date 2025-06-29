my_file = open("my_document.txt", "r")
read = my_file.read()
print(read)

my_file.close()

try:
    with open("my_document.txt", "w") as file:
        file.write("bye")
except FileNotFoundError:
    print("File not found")

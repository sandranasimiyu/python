
word = input("Enter a word: ")
print(word)
size = len(word)
for i in range(0, size-1, 2):
    print(f"index{i} {word[i]}")

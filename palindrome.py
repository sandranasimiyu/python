word = input("Enter a word: ")


def palindrome(word):
    new_word = word.lower()
    current_word = new_word[::-1]
    return new_word == current_word


result = palindrome(word)

if result:
    print("Im a palindrome")
else:
    print("no im not a palindrome")

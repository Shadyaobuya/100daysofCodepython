print("A palindrome is a word that can be reads same backwards and forward.\nThis program checks whether the given word is a palindrome.")
word=input("Write word to check: ")
if word[::]==word[::-1]:
    print(f"Word read backwards is {word[::-1]}, Its a palindrome")
else:
    print(f"Word read backwards is {word[::-1]}, Its not a palindrome")

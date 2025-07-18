import string
import random



chars = string.ascii_letters + string.digits + string.punctuation
chars = list(chars)


key = chars.copy()
print(f"chars: {chars}")
random.shuffle(key)
print(f"key: {key}")

ine = input("Enter a string to hash: ")


text = ""


for letter in ine:
    index = chars.index(letter)
    text += key[index]
print(f"Ciphertext: {text}")
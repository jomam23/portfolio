import string
h = "hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh"
for h in h:
    char = string.ascii_letters + string.digits + string.punctuation
    file = open("key.txt", "r")
    key = file.read()
    file.close()
    ine = input("write:")
    text3 = ""
    text = ""
    for letter in ine:
        index = char.index(letter)
        text3 += key[index]
    for letter in text3:
        index = char.index(letter)
        text += key[index]
    print(f"Ciphertext: {text}")


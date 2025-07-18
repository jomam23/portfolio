import string
h = "hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh"
for h in h:
    char = string.ascii_letters + string.digits + string.punctuation
    file = open("key.txt", "r")
    key = file.read()
    file.close()
    ine = input("write:")
    text = ""
    text3 = ""
    for letter in ine:
        index = key.index(letter)
        text += char[index]
    for letter in ine:
        index = key.index(letter)
        text3 += char[index]
    print(f"Ciphertext: {text3}")


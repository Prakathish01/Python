#Encrypt & Decrypt

import string,random

chars = string.punctuation +string.digits +string.ascii_letters
chars =list(chars)
keys = chars.copy()
random.shuffle(keys)

print(chars)
print(keys)

#Encrypt

original_mes = input("Enter your Message :")
cipher_mes = ""

for letter in original_mes:
    index = chars.index(letter)
    cipher_mes += keys[index]

print(f"cipher message :{cipher_mes}")

#Decrypt

original_mes =""
cipher_mes = input("Enter your cipher message :")

for letter in cipher_mes:
    index = keys.index(letter)
    original_mes += chars[index]

print(f"Your original message :{original_mes}")

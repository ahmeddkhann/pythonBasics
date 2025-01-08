import random
import string

chars = " " + string.ascii_letters + string.digits + string.punctuation
chars = list(chars)
key = chars.copy()
random.shuffle(key)

#ENCRYPTED TEXT
plain_text = input("enter a message to be encrypted: ")
cipher_text = ""

for letter in plain_text:
    index = plain_text.index(letter)
    cipher_text += key[index]

print(" ENCRYPTION ")
print(f"original text: {plain_text}")
print(f"encrypted text: {cipher_text}")
print("************************")

#DECRYPTED
cipher_text = input("enter a message to be encrypted: ")
decrypted_text = ""

for letter in cipher_text:
    index = cipher_text.index(letter)
    decrypted_text += chars[index]

print(" DECRYPTION ")
print(f"encrypted text: {cipher_text}")
print(f"decrypted text: {plain_text}")
print("************************")

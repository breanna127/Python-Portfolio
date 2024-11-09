"""
File: decrypt.py
Decrypts an input string of lowercase letters and prints the result. The other input is the distance value.
"""

code = input("Enter the coded text: ")
distance = int(input("Enter the distance value: "))
plainText = ""
for ch in code:
    ordvalue = ord(ch)
    cipherValue = ordvalue - distance
    if cipherValue < ord('a'):
        cipherValue = ord('z') - \
        (distance - (ord('a') - ordvalue - 1))
    plainText += chr(cipherValue)
    
    print(plainText)
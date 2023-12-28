alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text,shift):
    cipher_text = ''
    for i in text:
        pos = alphabet.index(text)
        new_pos = pos +shift
        new_code = alphabet[new_pos]
        cipher_text += new_code
        print(f"the encoded text is {cipher_text}")
    return cipher_text
print(encrypt(text,shift))



    
   
print(encrypt(text,shift))

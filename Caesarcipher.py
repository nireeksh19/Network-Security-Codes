def encrypt(plainText,key):
    cipher=""
    for i in plainText:
        element = chr(ord(i)+key)
        if(i.islower() and element >'z')or (i.isupper() and element>'Z'):
            element=chr(ord(ele)-26)
        cipher+=element
    print("Cipher text is :")
    print(cipher)
    return cipher
    
def decrypt(cipherText,key):
    plain=""
    for i in cipherText:
        element = chr(ord(i)-key)
        if(i.islower() and element <'a')or (i.isupper() and element<'A'):
            element=chr(ord(ele)+26)
        plain+=element
    print("Decrpted text is :")
    print(plain)

plainText=input("Enter plain text: ")
key=int(input("Enter key: "))
cipherText = encrypt(plainText,key)
decrypt(cipherText,key)
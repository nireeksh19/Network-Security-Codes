text=input("Enter the string :")
upper=['H','E','W','Q','R','T','A','D','S','F','G','C','X','Z','V','M','P','B','O','N','L','J','Y','I','K','U']
lower=['m','q','z','p','l','a','n','w','x','o','k','s','b','c','e','i','t','v','r','u','j','f','h','y','d','g']
encryptedText=""
decrpytedText=""
for i in text:
    if(i.isupper()):
        z=ord(i)-65
        encryptedText=encryptedText+upper[z]
    elif(i.islower()):
        z=ord(i)-97
        encryptedText=encryptedText+lower[z]
    else:
        print("Bro alphabets only !!")
print("Encrypted text: ",encryptedText)
for i in encryptedText:
    if(i.isupper()):
        z=upper.index(i)+65
        decrpytedText=decrpytedText+chr(z)
    else:
        z=lower.index(i)+97
        decrpytedText=decrpytedText+chr(z)
print("Decrpted text: ",decrpytedText)
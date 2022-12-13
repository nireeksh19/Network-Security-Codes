A=0
re=[]
for i in range(26):
    Z=(A%26)+65
    ar=[]
    for b in range(26):
        ar.append(chr(Z))
        A+=1
        Z=(A%26)+65
    re.append(ar)
    A+=1
 
key=input("Enter key:")
txt=input("Enter text:")
cipher=""
l=len(key)
j=0
for i in txt:
    k=key[j%l] 
    cipher+=re[ord(i)-65][ord(k)-65]
    j+=1
 
print(cipher)
 
 
d=""
l=len(key)
j=0
for i in cipher:
    k=key[j%l]
 
    d+=re[0][re[ord(k)-65].index(i)]
    j+=1
print(d)

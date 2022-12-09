#Take a string input
s=input("Enter the string:")
#covert the string into binary 
res=''.join(format(ord(i), '08b') for i in s)
print(res)

#get l equal to half the length of string input
l=int(len(res)/2)

#divide them to left and right
left=res[:l]
right=res[l:]

k=input("enter key:")
#covert the key into binary 
key=''.join(format(ord(i), '08b') for i in k)

#any function between R and key
s= bin(int(right, 2) + int(key, 2))

#xor between left and s
ans=bin(int(s[2:],2) ^ int(left,2))

#new left is right and new right is xor (left and f(right,key))
newr=ans[2:]
newl=right

#swap newr and newl
newr,newl=newl,newr

#any function between R and key
s= bin(int(newr, 2) + int(key, 2))

#xor between left and s
ans=bin(int(s[2:],2) ^ int(newl,2))

nl=newr
nr=ans[2:]
nl,nr=nr,nl
cip=nl+nr
if(len(cip)!=len(res)):
    while(len(cip)!=len(res)):
        cip="0"+cip
print(cip)
st=""
for i in range(0,len(cip),8):
 temp=cip[i:i+8]
 d=int(temp,2)
 st=st+chr(d)
print(st)

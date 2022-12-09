s=input("Enter the string:")
res=''.join(format(ord(i), '08b') for i in s)
print(res)

l=int(len(res)/2)
left=res[:l]
right=res[l:]

k=input("enter key:")
key=''.join(format(ord(i), '08b') for i in k)
s= bin(int(right, 2) + int(key, 2))
ans=bin(int(s[2:],2) ^ int(left,2))
newr=ans[2:]
newl=right
newr,newl=newl,newr
s= bin(int(newr, 2) + int(key, 2))
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

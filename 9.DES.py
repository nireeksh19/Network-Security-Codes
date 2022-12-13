import random

s=input("Enter the string: ")
res=''.join(format(ord(i),'08b')for i in s)

ans = ""
for i in range(len(res)):
    if(i%8!=0):
        ans+=res[i]
print(len(ans))

l = int(len(ans)/2)

left = ans[:l]
right = ans[l:]

lt = [2,3,6,7,1,6,5,9]
keys=[]

for i in range(8):
    newkey=""
    newans=""

    nl = int(left,2)
    nl=bin(nl<<lt[i])
    num=2+lt[i]

    nr=int(right,2)
    nr=bin(nr<<lt[i])
    num = 2+lt[i]

    newkey=nr[num:]+nl[num:]

    rm=[]
    while(len(rm)!=8):
        r=random.randint(0,len(newkey)-1)
        if(r not in rm):
            rm.append(r)

    for i in range(len(newkey)):
        if(i not in rm):
            newans+=newkey[i]
    keys.append(newans)
for i in range(0,len(keys)):
    print("Key",i+1,"=",keys[i])
q=int(input("Enter prime number :"))
alp=int(input("Enter primitive root :"))

xa=int(input("Enter private key of A: "))
xb=int(input("Enter private key of B: "))

ya=(alp**xa)%q
yb=(alp**xb)%q

Ka=(yb**xa)%q
Kb=(ya**xb)%q

print("Shared secret key of Ka: ",Ka)
print("Shared secret key of Kb: ",Kb)

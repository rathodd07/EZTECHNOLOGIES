#time complexity O(n)
'''n=int(input())
xor=0
for i in range(1,n+1):
    xor=xor^i
print(xor)'''

'''n=5
if n%4==0:
    print(n)
elif n%4==1:
    print(1)
elif n%4==2:
    print(n+1)
elif n%4==3:
    print(0)'''

xor=0
l=int(input("enter range"))
u=int(input("enter the range"))
for i in range(l,u+1):
    xor=l^i
print(xor)
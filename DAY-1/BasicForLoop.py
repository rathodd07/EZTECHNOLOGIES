n=20
for i in range(1,21):
    print(i)

li=[i for i in range(1,21)] #it takes all the values within list 
print(li)


even=[i for i in range(1,21) if i%2==0] #it takes all the even values within list 
print(even)

odd=[i for i in range(1,21) if i%2==1] #it takes all the odd values within list 
print(odd)

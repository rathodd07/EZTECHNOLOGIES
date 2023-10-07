#1.inversion code means how many swaps will happen in an sorting array 
l=list(map(int,input("enter the elemnets:").split()))
count=0
for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        if(l[i]>l[j]):
            count+=1
print("the number of swapping counts are:",count)
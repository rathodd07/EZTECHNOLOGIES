'''elements=input("enter the elements :")
my_array=[int(x) for x in elements.split(" ")]
r_array=[]
for x in my_array:
    if x >=0:
        r_array.append(x)
r_array.sort()
for i in range(0,max(r_array)+1):
    if(i!=r_array[i]):
        print(i)
        break
print(max(r_array)+1)
'''

b=input()
a=[int(x) for x in b.split(" ")]
print(a)
for i in range(len(a)):
    if i not in a:
        print(i)
        break


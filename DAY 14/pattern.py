# patern 1
#n=4
#for i in range(n):
#    for j in range(2*i+1):
#        print(" * ",end=" ")
#    print()

#patern 2
#def pyramid(n):
#    row = n
#    col = 2*n-1
#    start,end = n-1, n-1
#    for i in range(row):
#        for j in range(col):
#            if j>=start and j<=end:
#                print(" ",end="")
#            else:
#                print("*" ,end="")
#        print()
#        start-=1
#        end+=1
#pyramid(5)

#pattern 3 outer circle  worsk for only even numbers
#def circle(n):
#    row=n
#    col=n
#    for i in range(row):
#        for j in range(col):
#            if i==j or (i+j)==n-1:
#                print(" ",end=" ")
#            elif i==0 or i==n-1 or j==0 or j==n-1: #it prints outer circle
#                print("*", end=" ")
#            else: 
#                print(" ",end=" ")
#        print()
#circle(6)
#
##pattern 4 circle in side a circle printing
#def circle(n):
#    row=n
#    col=n
#    for i in range(row):
#        for j in range(col):
#            if i==j or (i+j)==n-1:
#                print(" ",end=" ")
#            #elif i==0 or i==n-1 or j==0 or j==n-1: #it prints outer circle
#            #    print("*", end=" ")
#            else: 
#                print("*",end=" ")
#        print()
#circle(6)
#
##pattern 5 diagonal pattren
#def circle(n):
#    row=n
#    col=n
#    for i in range(row):
#        for j in range(col):
#            if i==j or (i+j)==n-1:
#                print("*",end=" ")
#            elif i==0 or i==n-1 or j==0 or j==n-1: #it prints outer circle
#                print(" ", end=" ")
#            else: 
#                print("*",end=" ")
#        print()
#circle(4)
#

#pattern 6 ASCCI values
#def upperTriangular(n):  
#    char="a"
#    for i in range(1,n+1):
#        for j in range(i):
#            print(char,end=" ")
#            char=chr(ord(char)+1)
#            if char>"z":
#                char="a"
#        print()
#upperTriangular(9)

#pattern 7 
#def missing_pyramid(n):
#    for i in range(1,n+1):
#        print(" "*(n-i),end="")
#        for j in range(1,i):
#            print("*",end=" ")
#        print()
#missing_pyramid(3)

#pattern 8 number pattern
def hollow_pyramid(n):
    row = n
    col = 2*n-1
    var=2
    var2=1
    start,end = n-1, n-1
    for i in range(row):
        for j in range(col):
            if (j==start or j==end) and i!=n-1:
                if start==end:
                    print(1,end="")
                elif j==start:
                    print(1,end=" ")
                else:
                    print(var,end=" ")
                    var+=1
            elif i==n-1 and (j>=start and j<=n-1):
                print(var2,end=" ")
                var2+=1
            else:
                print(" ",end="")
        print()
        start-=1
        end+=1
hollow_pyramid(5)

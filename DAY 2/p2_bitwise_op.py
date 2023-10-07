def findSingle(arr,n):
    res=arr[0]
    #Do XOR of all elements and return 
    for i in range(1,n):
        res=res^arr[i]
    return res
arr=[2,4,5,7,7,2,4,5,1]
print(findSingle(arr,len(arr)))
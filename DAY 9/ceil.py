#ceil problem: it means printing the privious element of target value
def linear_search(arr,target):
    n=len(arr)
    for i in range(n):
        if arr[i]==target:
            return arr[i-1] # for index position just retun (i-1)
        
    return -1
arr=list(map(int,input("enter the elements with comma:").split(',')))
target=int(input("enter the target sum:"))
print(linear_search(arr,target))
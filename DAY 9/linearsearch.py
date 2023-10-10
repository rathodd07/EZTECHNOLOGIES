#linear search
def linearSearch(arr,key):
    n=len(arr)
    for i in range(n):
        if key==arr[i]:
            print("found the key:",key)
            return
    print("key is not found!")

arr=list(map(int,input("enter the array elements:").split()))
key=int(input("enter the searching key:"))
linearSearch(arr,key)

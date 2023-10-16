#method 1
def two_pointer(arr,target):
    arr.sort()
    i,j = 0, len(arr)-1
    while i<j:
        if arr[i]+arr[j] == target: return (arr[i],arr[j])
        if arr[i]+arr[j] < target: i+=1
        if arr[i]+arr[j] > target: j-=1
    return False
arr=[12,3,5,78]
target=8
res=two_pointer(arr,target)
print(res)

#metod 2
'''#Two pointers algorithm
def solve(arr):
    p1 = 0
    p2 = len(arr)-1
    while p1<p2:
        sum = arr[p1] + arr[p2]
        if sum == target:
            return (arr[p1], arr[p2])
        elif sum < target:
            p1 += 1
        else:
            p2 -= 1
    return False
    
arr = [2,3,4,5,6]
target = 17
result = solve(arr)
print(result)'''
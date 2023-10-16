#sliding window problem
def sum_of_kth_subArray(arr,kth):
    _sum=0
    ps=0
    i,j=0,kth-1
    while j<len(arr):
        if i==0:
            _sum=sum(arr[i:j+1])
            ps=_sum
        else:
            cs=ps-arr[i-1]+arr[j]
            _sum=max(_sum,cs)
            ps=cs
        i+=1
        j+=1
    return _sum

arr=list(map(int,input("enter the elements:").split(',')))
k_th_subarray=int(input())
print(sum_of_kth_subArray(arr,k_th_subarray))

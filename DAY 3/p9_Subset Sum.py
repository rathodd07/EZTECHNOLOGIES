'''#1.method one for subset sum
def SubsetSum(nums,target_sum):
    for i in nums:
        for j in nums:
            for k in nums:
                if(i+j+k==target_sum):
                    return True
    return False

if __name__=='__main__':
    nums=list(map(int, input("Enter the list elements:").split()))
    target_sum=int(input(" enter the sum value:"))
    print(SubsetSum(nums,target_sum))'''

#2.method or approch
def check(arr,target_sum,len_arr):
    if target_sum==0: #checking for target==0 that sum is element is found
        return True
    if len_arr==0: #checking for lenth of the array is empty or not
        return False
    if(arr[len_arr-1]>target_sum):#if the last element is greater the sum element ignore and return the array
        return check(arr,target_sum,len_arr-1)
    return check(arr,target_sum-arr[len_arr-1],len_arr-1) or check(arr,target_sum,len_arr-1)
    #the sum value is found by there conditions

arr=[3,34,4,12,5,2]#arr=list(map(int, input("Enter the list elements:").split()))
#target_sum=int(input(" enter the sum value:"))
target_sum=9
res=check(arr,target_sum,len(arr))
if res==True:
    print("sum is found")
else:
    print("sum is not found")
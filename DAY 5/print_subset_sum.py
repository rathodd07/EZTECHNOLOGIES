#1.subset sum checking
def check(arr,target_sum,len_arr):
    if target_sum==0: #checking for target==0 that sum is element is found
        return True
    if len_arr==0: #checking for lenth of the array is empty or not
        return False
    if(arr[len_arr-1]>target_sum):#if the last element is greater the sum element ignore and return the array
        return check(arr,target_sum,len_arr-1)
    return check(arr,target_sum-arr[len_arr-1],len_arr-1) or check(arr,target_sum,len_arr-1)
    #the sum value is found by there conditions

arr=[6,8,9,5,4,3,2,26,2]#arr=list(map(int, input("Enter the list elements:").split()))
#target_sum=int(input(" enter the sum value:"))
target_sum=28
res=check(arr,target_sum,len(arr))
if res==True:
    print("sum is found")
else:
    print("sum is not found")


#2.subset sum printing
def subset_sum(nums, target_sum):
    def find_subsets(index, current_subset, current_sum):
        if current_sum == target_sum:
            print(current_subset)
            found[0] = True  # Set the found flag to True when a subset is found
            return
        if current_sum > target_sum or index >= len(nums):
            return
        # Include the current element
        find_subsets(index + 1, current_subset + [nums[index]], current_sum + nums[index])
        # Exclude the current element
        find_subsets(index + 1, current_subset, current_sum)

    found = [False]  # Initialize a list to store the found flag
    find_subsets(0, [], 0)
    if not found[0]:
        print(f"No subsets found that add up to {target_sum}")

nums = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
target_sum = int(input("Enter the target sum: "))
subset_sum(nums, target_sum)



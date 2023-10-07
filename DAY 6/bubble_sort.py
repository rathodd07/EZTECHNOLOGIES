# Python program for implementation of Bubble Sort
def bubbleSort(arr):
	n = len(arr)#assigning the size value to n
	# i=Traverse through all array elements
	for i in range(n-1):
		#j=traverse through index position by checking array elements
		for j in range(n-i-1):
			if arr[j] > arr[j + 1]:#comparing the bigger elements and swapping
				arr[j], arr[j + 1]= arr[j + 1], arr[j]
				#temp=arr[i]
				#arr[i]=arr[j+1]
				#arr[j+1]=temp
if __name__=="__main__":
	
    arr=list(map(int,input("enter the elemnts:").split()))
    bubbleSort(arr)
    print("Sorted array is:")
    for i in range(len(arr)):
	    print("%d" % arr[i], end=" ")

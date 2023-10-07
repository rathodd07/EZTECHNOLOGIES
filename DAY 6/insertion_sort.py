#insertionSort
def InsertionSort(a):
# traversing the array from 1 to length of the array(a) 0r a-1
        for i in range(1, len(a)):
                temp = a[i]
                j = i-1
                while j >=0 and temp < a[j] : # temp>a[j] its assending order
                        a[j+1] = a[j]         # temp<a[j] its discending ssorder
                        j = j- 1
                a[j+1] = temp

a = list(map(int,input("enter the elements:").split()))
InsertionSort(a)
print("Array after sorting:",a)



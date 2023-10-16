#arr=[18,28,58,119,120]
#arr1=[17,19,57,68,123,569]
#arr3=arr+arr1
#arr3.sort()
#print(arr3)

def main():
    arr1=[9,-1,6,98,23,2]
    arr2=[23,87,1,3,10,11]
    ans=[]
    i=0
    j=0
    while i<len(arr1) or j<len(arr2):
        if i>=len(arr1):
            while j<len(arr2):
                ans.append(arr2[j])
                j+=1
        elif j>=len(arr2):
            while i<len(arr1):
                ans.append(arr1[i])
                i+=1
        elif arr1[i]<arr2[j]:
            ans.append(arr1[i])
            i+=1
        else:
            ans.append(arr2[j])
            j+=1
    print(ans)
main()




_str="BFBFBFBBFBBFBFBFB"
arr=[[0 for i in range(1000)]for j in range(1)]
i=0
up=1
cp = 0
arr[0][0]=1
while i<len(_str):
    if _str[i]=="B":
        cp = cp -1
        if arr[0][cp]==0:
            arr[0][cp]=1
            up+=1
    elif _str[i]=="F":
        cp+=2
        if arr[0][cp]==0:
            arr[0][cp]=1
            up+=1
    i+=1
print(up)
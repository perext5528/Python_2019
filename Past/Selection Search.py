def Selection(arr, left, right, key, turn):
    l=left
    r=right
    p=left
    if(turn==0):
        print("Default Data : ",end="")
        print(arr)
        print("Data Type : ", end="")
        if(int(len(arr)%2)==0):
            print("Even\n")
        else:
            print("Odd\n")
    turn += 1
    while(l<r):
        while(arr[l]<arr[p]):
            l+=1
        while(arr[r]>arr[p]):
            r-=1
        if(l<=r):
            temp=arr[l]
            arr[l]=arr[r]
            arr[r]=temp
        else:
            temp=arr[p]
            arr[p]=arr[r]
            arr[r]=temp

    print("turn : %d" %turn)
    print(arr)

    s=(r-1)-left+1
    if(key<=s):
        Selection(arr,left,r-1,key,turn)
    else:
        if(key==s+1):
            print("\nResult Data : %d" %arr[r])
        else:
            Selection(arr,r+1,right,key-s-1, turn)

data=[8, 3, 11, 9, 12, 2, 6, 15, 18, 10, 7, 14, 13]
Selection(data,0,12, 7, 0)
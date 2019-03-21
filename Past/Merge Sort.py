#To-Do def Merge Check

def Merge(arr,left,right,middle):
    leftarr=[0 for i in range (middle-left)]
    rightarr=[0 for i in range (right-middle)]
    mergedarr=[0 for i in range (left+right)]
    for i in range (left, middle):
        leftarr[i]=arr[i]
    for i in range(middle+1, right):
        rightarr[i]=arr[i]

    i = j = k=0
    while(i<len(leftarr) and j<len(rightarr)):
        if(leftarr[i]<rightarr[j]):
            mergedarr[k]=leftarr[i]
            i+=1
        else:
            mergedarr[k]=rightarr[j]
            j+=1
        k+=1
    if(i>=len(leftarr)):
        for i in range(k,len(leftarr)+len(rightarr)):
            mergedarr[i]=rightarr[i-len(leftarr)]
    else:
        for i in range(k,len(leftarr)+len(rightarr)):
            mergedarr[i]=leftarr[i-len(rightarr)]

    return mergedarr


def Devide(arr, left, right):
    if(left<right):
        middle=int((left+right)/2)
        Devide(arr,left,middle)
        Devide(arr,middle+1,right)
        Merge(arr,left,right,middle)
    print(arr)
data = [37, 10, 22, 30, 35, 13, 25, 24]
Devide(data,0,7)
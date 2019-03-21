def PrintArray(Array):  # 배열 출력 함수
    for i in range (1,len(Array)):
        print(Array[i], end=" ")
    print()

arr = [0, 5, 26, 37, 1, 61, 11, 59]
atemp = 0
btemp = 0
count = 0

print("[Default Data]")
PrintArray(arr)

for l in range(7, 0, -1):
    count+=1
    for i in range(int(l/2), 0, -1):
        atemp=arr[i]
        j = 2*i
        while(j<=l):
            if((j<l)and(arr[j]<arr[j+1])):
                j+=1
            if(atemp<arr[j]):
                arr[int(j/2)]=arr[j]
                j*=2
            else:
                break
            arr[int(j/2)] = atemp

    print("\nturn_%d" %count)
    PrintArray(arr)

    btemp = arr[1]
    arr[1] = arr[l]
    arr[l] = btemp

    print("change_%d" %count)
    PrintArray(arr)

print("\n[Result Data]")
PrintArray(arr)
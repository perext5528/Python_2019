def PrintArray(arr):    # 배열 출력 함수
    for i in range(len(arr)):
        print(arr[i], end=" ")

arr=[30, 60, 90, 10, 40, 80, 40, 20, 10, 60, 50, 30, 40, 90, 80]
n = len(arr)    # 배열 길이
gap = 5    # 배열 내 비교대상의 간격
count=1    # 회전 출력을 위한 변수

print("Default : ", end="") # 기본 배열 출력
PrintArray(arr)

while(gap>=1):
    i=gap
    print("\n\ngap = %d" % gap, end="") # gap값 출력
    while(i<n):
        value=arr[i]
        j=i
        while(j-gap>=0 and value<arr[j-gap]):
            arr[j] = arr[j-gap]
            j-=gap
            print("\nturn_%02d : " % count, end="") # 회전당 배열 출력
            PrintArray(arr)
            count += 1
        arr[j]=value
        i+=1
    gap-=2  # 비교 대상의 간격을 각각 5, 3, 1로 하여 비교

print("\n\nResult : ", end="") # 정렬이 완료된 배열 출력
PrintArray(arr)
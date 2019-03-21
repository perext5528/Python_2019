arr= [8, 23, 12, 4, 10]   # 대입문으로 배열 초기화

print("    <Insertion Sort>")
print("Default :", end="")  # 초기값 출력
for i in range(0, 5, 1):
    print("%2d" %arr[i], end=" ")
print("\n------------------------")

for i in range(0, 5, 1):
    temp = arr[i]   # 임시 공간에 비교할 수 삽입
    j = i-1         # while 반복문에 사용되는 제어변수 초기화
    while(j>-1 and arr[j]>temp):
        arr[j+1] = arr[j]   #배열 내의 값 교체
        j  -= 1             # 제어변수 조정
    arr[j+1] = temp         # 배열 내의 값 교체

    print("%d trun :" %(i+1), end=" ")  # 각 회전 별 출력
    for k in range(0, 5, 1):
        print("%2d" %arr[k], end=" ")
    print()

print("------------------------")
print("Result :", end=" ")    # 최종 결과값 출력
for i in range(0, 5, 1):
    print("%2d" %arr[i], end=" ")
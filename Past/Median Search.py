def Median(arr):
    print("데이터 : ",end="")
    print(arr)
    print("유형 : ",end="")
    if(len(arr)%2==0):
        print("짝수")
        print("중앙값 : %d" % ( ( (arr[(int)(len(arr) / 2) - 1]) + (arr[(int)(len(arr) / 2)]) ) / 2) )
    else:
        print("홀수")
        print("중앙값 : %d" % arr[(int)(len(arr) / 2)])

data=[2, 3, 6, 7, 8, 9, 10, 11, 12, 14, 15, 18 ]
data2=[1, 2, 3, 5, 8, 13, 21]

Median(data)
print()
Median(data2)
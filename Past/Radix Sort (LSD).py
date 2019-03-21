radix_queue = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
data = [15, 23, 31, 49, 58, 64, 72, 80, 96, 7, 5, 93, 81, 79, 68, 54, 42, 30, 26, 17]
exp = 1
turn = 1

print("입력 자료")
for i in range (0, 20):
    print(data[i], end=" ")

while(turn<3):
    for i in range(0, 10):
        for j in range(0, 20):
            if(int((data[j] % (exp*10)) / exp) == i):   # 기수 정렬
                if (radix_queue[i][0] == 0):    # 큐 삽입 조건
                    radix_queue[i][0] = data[j]
                radix_queue[i][1] = data[j]

    for i in range(0, 20):
        data[i] = radix_queue[int(i/2)][i%2]    # 기존 자료를 정렬된 자료로 초기화
        radix_queue[int(i/2)][i%2] = 0    # 큐 초기화

    print("\n\nK%d 정렬 큐 상태" %turn)
    for i in range(0, 10):
        print("큐%d %3d %3d" %(i, data[i*2], data[i*2+1]))

    print("\nK%d 정렬 자료" %turn)
    for i in range(0, 20):
        print(data[i], end=" ")

    exp*=10
    turn+=1
def PrintArray(Array):  # 배열 출력 함수
    for i in range (len(Array)):
        for j in range (len(Array)):
            print("%6.2f" %Array[i][j], end=" ")
        print()

orig_mat = [[3, -1, 2], [3, 0, 1], [1, 0, 2]]
unit_mat = [[1,0,0],[0,1,0],[0,0,1]]

print("Default matrix")
PrintArray(orig_mat)

for i in range(len(orig_mat)):  # n차 정방행렬에서 n번 회전
    for j in range(len(orig_mat)):
        orig_mat[i][j]/=orig_mat[i][i]    # 주대각성분을 1로 만들기 위함
        unit_mat[i][j]/=orig_mat[i][i]
    for k in range(len(orig_mat)):  # 가우스 소거법 진행
        temp = (orig_mat[k][i] / orig_mat[i][i])
        if(i!=k):   # 자신의 행을 제외한 계산
            for l in range(len(orig_mat)):
                orig_mat[k][l]-=(orig_mat[i][l]*temp)
                unit_mat[k][l]-=(unit_mat[i][l]*temp)

print("\nInverse matrix")
PrintArray(unit_mat)
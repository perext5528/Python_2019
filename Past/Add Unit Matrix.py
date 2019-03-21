def Add_Unit_matrix(squ_mat):   # 함수 선언
    n = len(squ_mat)    # 해당 정사각행렬의 크기를 갖는 변수 선언, 반복문 인자값, 영행렬 선언 시 사용
    print("Square Matrix (%d x %d)" %(n, n)) # 해당 정사각행렬 출력
    for i in range(n):
        for j in range(n):
            print("%2d " %squ_mat[i][j], end= "")
        print()

    unit_mat=[[0]*n for i in range(n)]  # 해당 정사각행렬의 크기와 동일한 영행렬 선언

    for i in range(n):  # 영행렬을 단위행렬로 변환
        for j in range(n):
            if(i==j):
                unit_mat[i][j]=1

    print("\nAdded Matrix" )    # 정사각행렬에 단위행렬을 붙여 출력
    for i in range(n):
        for j in range(n):
            print("%2d " %squ_mat[i][j], end= "")
        for k in range(n):
            print("%2d " %unit_mat[i][k], end="")
        print()
    print()

squ_mat2=[[4, 0], [7, 1]]
squ_mat3=[[3, 5, 1], [-9, 4, 7], [1, -8, -2]]
squ_mat4=[[8, 7, 2, 6], [-7, -9, 4, 7], [3, 1, -8, -2], [7, 5, 4, 4]]
squ_mat5=[[1, 4, 8, 9, 3], [-5, -7, 9, 1, 2], [4, 1, -6, 3, 8], [9, 4, 2, -7, 9], [1, 6, 4, 3, 7]]

Add_Unit_matrix(squ_mat2)
Add_Unit_matrix(squ_mat3)
Add_Unit_matrix(squ_mat4)
Add_Unit_matrix(squ_mat5)
orig_mat=[[1, -1, 2], [3, 0, 1], [1, 0, 2]] # 원시행렬
orig_add_unit_mat=[[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0]] # 역행렬 계산을 위한 행렬
calc_check_mat=[[0, 0, 0],[0, 0, 0],[0, 0, 0]] # 검산을 위한 빈 행렬

for i in range(3):
    for j in range(3):
        orig_add_unit_mat[i][j] = orig_mat[i][j] # 역행렬 계산을 위한 행렬 초기화
        if(i==j):
            orig_add_unit_mat[i][j+3]=1 # 4번째 열부터 단위행렬 추가

for i in range(3): # 가우스 소거법
    temp = orig_add_unit_mat[i][i] # 주대각성분 추출
    for j in range(6):
        orig_add_unit_mat[i][j] /= temp # 피벗 행을 만들기 위해 주대각성분으로 행을 나눔
    for k in range(3):
        if(i!=k): # 다른 행과 기본행연산
            temp = orig_add_unit_mat[k][i] # 해당 주대각성분으로 다른 행의 같은 열을 소거하기 위함
            for j in range(6):
                orig_add_unit_mat[k][j]-=orig_add_unit_mat[i][j]*temp

print("Result") # 계산 결과 출력
for i in range(3):
    for j in range(6):
        print("%4.1f" %orig_add_unit_mat[i][j], end="  ")
    print()
print()

print("Calculate Cheking") # 검산과정과 그 결과 출력
for i in range(3):
    for j in range(3):
        for k in range(3):
           calc_check_mat[i][j]+=orig_mat[i][k]*orig_add_unit_mat[k][j+3]
        print("%4.1f" % calc_check_mat[i][j], end="  ")
    print()

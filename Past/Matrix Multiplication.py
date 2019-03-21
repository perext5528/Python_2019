def PrintMatrix(mat, row, col):
    for i in range(row):
        for j in range(col):
            print("%2d "%mat[i][j],end="")
        print()

def Multiplication(mat_a, mat_b, matrixInfo):
    mat_c=[[0]*matrixInfo[0] for i in range(matrixInfo[2])]

    for i in range(matrixInfo[0]):
        for j in range(matrixInfo[2]):
            for k in range(matrixInfo[1]):
                mat_c[i][j]+=mat_a[i][k]*mat_b[k][j]

    print("mat_a")
    PrintMatrix(mat_a, matrixInfo[0], matrixInfo[1])
    print("mat_b")
    PrintMatrix(mat_b, matrixInfo[1], matrixInfo[2])
    print("mat_c")
    PrintMatrix(mat_c, matrixInfo[0],matrixInfo[2])
    print("==============")

a1=[[2, 4], [1,3]]
b1=[[3,1], [2,1]]
#cf. info[0] = row_a, info[1] = col_a = row_b, info[2] = col_b
info1=[2,2,2]
Multiplication(a1,b1,info1)

a2=[[1, 4], [2, 5], [3, 6]]
b2=[[3, 6, 1], [5, 2, 0]]
info2=[3, 2, 3]
Multiplication(a2,b2,info2)

a3=[[5, 1, 3],[4, 5, 3], [6, 2, 4]]
b3=[[7, 8, 9],[3, 5, 1],[9, 7, 1]]
info3=[3,3,3]
Multiplication(a3,b3,info3)
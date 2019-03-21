def PrintMatrix(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print("%4d" % arr[i][j], end="")
        print()
    print()

def Floyd(arr):
    print("Matrix(Default)")
    PrintMatrix(arr)
    min=[0, 0]

    for k in range(1,len(arr)):
        print("------------- k = %d -------------" % k)
        for i in range(1,len(arr)):
            if(i!=k):
                for j in range(1,len(arr)):
                    if(j!=k and j!=i and (arr[i][k]+arr[k][j]<arr[i][j]) and (arr[i][k]+arr[k][j]<10)):
                        print("Matrix(%d,%d) Renewed : %2d -> %2d"%(i, j, arr[i][j], arr[i][k]+arr[k][j]))
                        arr[i][j] = arr[i][k] + arr[k][j]

        print("Matrix(k = %d)"%k)
        PrintMatrix(arr)

arr=[[0,1,2,3,4,5],
     [1,0,4,2,5,99],
     [2,99,0,1,99,4],
     [3,1,3,0,1,2],
     [4,-2,99,99,0,2],
     [5,99,-3,3,1,0]]
Floyd(arr)

def PrintArray(arr):
    print("Result:\n")
    for i in range(0, row):
        for j in range(0, column):
            print("%d  " % arr[i][j], end=" ")
        print("")


row = int(input("2차원 배열의 행의 수 : "))
column = int(input("2차원 배열의 열의 수 : "))
array = [[0] * column for i in range(row)]

num = 1
i = j = 0
inv_i = row - 1
inv_j = column - 1

while num <= row * column:
    if j < column - 1:
        array[i][j] = num
        j = j + 1

    elif i < row - 1:
        array[i][j] = num
        i = i + 1

    elif inv_i <= row - 1 and inv_i > 0:
        array[inv_i][inv_j] = num
        inv_i = inv_i - 1

    num = num + 1

PrintArray(array)

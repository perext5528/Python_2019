def PrintArray(arr):
    print("Result:\n")
    for i in range(0, n):
        for j in range(0, n):
            print("%d  " % arr[i][j], end=" ")
        print("")


#n = int(input("Input NxN Magic Square(N : 4의 배수) : "))
n=8
array = [([0] * n) for i in range(n)]

number1 = number2 = 1
q=1
for i in range(0,n):
    for j in range(0,n):
        if :
            array[i][j]=number1
        number1=number1+1

"""
while number1 <= n*n:
    number1 = number1 + 1
    
while number2 >0:
    number2 = number2 - 1
"""
PrintArray(array)

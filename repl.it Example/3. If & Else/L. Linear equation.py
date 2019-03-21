a = int(input())
b = int(input())
if a != 0:
    if b % a == 0:
        print(int(b / a))
    else:
        print("no solution")
else:
    if b == 0:
        print("many solutions")
    else:
        print("no solution")

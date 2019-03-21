a = int(input())
b = int(input())
if ((a < 8 and a % 2 == 1) or (7 < a < 12 and a % 2 == 0)) and b == 31:
    print(a + 1)
    print(1)
elif ((a < 8 and a % 2 == 0) or (a > 7 and a % 2 == 1)) and b == 30:
    print(a + 1)
    print(1)
elif a == 2 and b == 28:
    print(a + 1)
    print(1)
elif a == 12 and b == 31:
    print(1)
    print(1)
else:
    print(a)
    print(b + 1)

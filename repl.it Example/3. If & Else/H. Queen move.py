x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
dx = abs(x1 - x2)
dy = abs(y1 - y2)
if (x1==x2) or (y1==y2) or (dx == dy):
    print("YES")
else:
    print("NO")

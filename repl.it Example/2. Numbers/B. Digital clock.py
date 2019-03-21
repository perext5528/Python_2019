a = int(input())
b = 24*60
if a>b:
    print((a-b)//60, (a-b)%60)
else:
    print(a//60, a%60)
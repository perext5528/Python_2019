def Table(n):
    if n%2==1:
        return n//2+1
    else:
        return n//2
a = int(input())
b = int(input())
c = int(input())
print(Table(a)+Table(b)+Table(c))
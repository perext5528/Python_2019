def min(n1, n2):
    if n1 < n2:
        return n1
    else:
        return n2


a = int(input())
b = int(input())
c = int(input())
print(min(min(a, b), c))

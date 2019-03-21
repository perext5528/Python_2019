a = [20, 30, 40, 50]
b = [25, 35, 55, 60, 70]

i=j=k=0
m=4
n=5

c=[0 for i in range(m+n)]

while(i<m and j<n):
    if(a[i]<=b[j]):
        c[k] = a[i]
        i+=1
    else:
        c[k]=b[j]
        j+=1
    k+=1

if(i>=m):
    for i in range(k,m+n):
        c[i] = b[i-m]
else:
    for i in range(k,m+n):
        c[i] = a[i-n]

for i in range(m+n):
    print("%2d" %c[i], end=" ")

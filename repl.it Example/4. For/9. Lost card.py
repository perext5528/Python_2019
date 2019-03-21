n=int(input())
sum=0
for i in range(n+1):
    sum+=i
for i in range(n-1):
    a = int(input())
    sum-=a
print(sum)
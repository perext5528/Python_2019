stack=[[0]*12 for i in range(3)]
stack[0]=[6, 3, 11, 9, 12, 2, 8, 15, 18, 10, 7, 14]

m=0                 #left
n=len(stack[0])-1   #right
top=0       #Stack Pointer
count=1     #turn count

stack[1][top]=m     #Default Stack value setting
stack[2][top]=n

while(top>-1):
    m=stack[1][top]     #Default Stack value input
    n=stack[2][top]
    top-=1
    i = m+1
    j = n
    while(i<j):
        while(i<=n and stack[0][i]<stack[0][m]):
            i+=1
        while(j>m and stack[0][j]>stack[0][m]):
            j-=1
        if(i<j):
            temp=stack[0][i]
            stack[0][i]=stack[0][j]
            stack[0][j]=temp

    if (stack[0][j] < stack[0][m]):
        temp=stack[0][m]        #Pivot Exchange
        stack[0][m]=stack[0][j]
        stack[0][j]=temp

    print("%d turn" %count)     #output
    for k in range(len(stack[0])):
        print("%d" %stack[0][k],end=" ")
    print("\n")
    count+=1

    if(j+1<n):      #Stack Control
        top += 1
        stack[1][top]=j+1
        stack[2][top]=n

    if(j-1>m):      #Stack Control
        top += 1
        stack[1][top]=m
        stack[2][top]=j-1


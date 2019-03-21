def Knapsack(arr, limit):
    temp=[[0]*len(arr) for i in range(4)]
    
    for i in range(len(arr)):   # 단위무게 당 가치
        arr[3][i]= int(arr[1][i])/int(arr[2][i])
        
    for i in range(len(arr)-1): # 배열 내림차순 정렬
        for j in range(i,len(arr)):
            if(arr[3][i]<arr[3][j]):
                for k in range(len(arr)):
                    temp[i][k]=arr[k][i]
                    arr[k][i]=arr[k][j]
                    arr[k][j]=temp[i][k]
    # Knapsack_info 각 행의 마지막 인덱스 : 무게, 가치
    Knapsack_info=[[0]*(len(arr)+1) for i in range (2)]
    i=0

    while(i<len(arr) and Knapsack_info[0][4]+arr[2][i]<limit): # 인덱스, 무게 조건
        Knapsack_info[0][4]+=arr[2][i]  # 무게 누적합
        Knapsack_info[1][4]+=arr[1][i]  # 가치 누적합
        Knapsack_info[0][i]=arr[0][i]   # 해당 원소의 종류 정보 추가
        Knapsack_info[1][i]=arr[2][i]   # 해당 원소의 무게 정보 추가
        i+=1

    rest = limit - Knapsack_info[0][4]  # 남은 무게

    if(rest>0):
        Knapsack_info[0][4]+=rest   # 무게 누적합
        Knapsack_info[1][4]+=int(rest*arr[3][i])    # 단위 무게당 가치 누적합
        Knapsack_info[0][i] = arr[0][i] # 해당 원소의 종류 정보 추가
        Knapsack_info[1][i] = rest  # 해당 원소의 무게 정보 추가

    print("배낭에 담긴 것 : ",end="")
    for i in range(len(arr)):
        if(Knapsack_info[1][i]!=0):
            print("%s %dg " %(Knapsack_info[0][i], Knapsack_info[1][i]),end="")
    print("\n배낭 무게 : %dg" % Knapsack_info[0][4])
    print("총 가치 : %d원"%Knapsack_info[1][4])

limit=40
array=[['주석', '백금', '은', '금'],
       [50000, 600000, 100000, 750000],
       [50, 10, 25, 15],
       [0, 0, 0, 0]]
Knapsack(array, limit)
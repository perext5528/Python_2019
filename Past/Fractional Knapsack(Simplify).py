def Frac_Knap(arr, limit):
    # 단위 무게로 나눔
    for i in range(len(arr)):
        arr[3][i] = int(arr[1][i]/arr[2][i])
    # 단위 무게를 기준으로 내림차순
    temp = [0 for i in range(4)]    # 값 교체에 필요한 임시 배열 생성
    for i in range(len(arr)-1):     # 선택 정렬 사용
        for j in range(i, len(arr)):
            if(arr[3][i]<arr[3][j]):    # 단위 무게 내림차순 정렬
                for k in range(len(arr)):
                    temp[k]=arr[k][i]   # 해당 열의 모든 값을 교체
                    arr[k][i]=arr[k][j]
                    arr[k][j]=temp[k]

    object_name=[0 for i in range(len(arr))]    # 물건 이름 정보
    weight=value=i=0    # 현재 무게, 가치, 인덱스 초기화
    # 배낭에 넣음
    while(weight+arr[2][i]<=limit and i<len(arr)):  # 현재 무게와 담을 물건의 무게의 합 < 용량
        weight+=arr[2][i]
        object_name[i]=arr[0][i]
        value+=arr[1][i]
        i+=1
    # 물건 부분 추가
    object_name[i]=arr[0][i]
    value+=(limit-weight)*arr[3][i]
    print(object_name)
    print(value)

limit = 40
array = [['주석', '백금', '은', '금'],
         [50000, 600000, 100000, 750000],
         [50, 10, 25, 15],
         [0, 0, 0, 0]]
Frac_Knap(array,limit)
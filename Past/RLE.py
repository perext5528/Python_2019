def Encoding(text):
    print("Default Text : ",end="")
    for i in range(len(text)):
        print("%c "%text[i],end="")
    count=1
    i=0
    while(i<len(text)):
        if(i==0 and text[i]==text[i+1]):    #인덱스가 0인 경우(직전 인덱스에 값이 없는 경우)
            start=i
            letter=text[i]
        elif(i!=0 and text[i]!=text[i-1]):  #인덱스가 0이 아닌 경우(직전 인덱스에 값이 있는 경우)
            start=i
            letter = text[i]
        while (text[i]!=0 and text[i] == text[i + 1]):  # 연속되는 문자의 개수를 누적
            count += 1
            i += 1

        if(count>3):    # 연속되는 문자의 개수가 4 이상인 경우
            text[start] = '&'
            text[start + 1] = count
            i=shift=start+3 # i 첨자 제어, 압축을 위한 shift 변수
            j=start+count   # 연속되는 문자열의 다음 인덱스
            lastchar=0  # 연속되는 문자열의 다음 인덱스부터 문자의 개수
            while(j<len(text) and text[j]!=0):
                lastchar+=1
                j+=1
            j=start+count
            while(lastchar>0):  # 남은 문자들이 모두 시프트할 때 까지
                text[shift]=text[j]
                lastchar-=1
                shift+=1
                j+=1
            for j in range(shift,len(text)): # 모두 시프트 된 후, 남은 인덱스에 0
                text[j]=0
        else:
            i += 1  # i 첨자 제어
        count=1 # count 초기화
    # 출력문
    i=0
    print("\nEncoded Text : ",end="")
    while(text[i]!=0):
        if(text[i-1]=='&'):
            print("%d "%text[i], end="")
        else:
            print("%c "%text[i],end="")
        i+=1
    return text

def Decoding(text):
    i=0
    while(i<len(text)):
        if(text[i]=='&'):
            start=i # 문자열 시작 인덱스 지정
            count=text[i+1] # count 초기화
            letter=text[i+2] # 연속되는 문자열에 해당하는 문자
            j = len(text)-1  # 맨 마지막부터 시작
            while (j > start + 2):  # 인코딩 된 부분 직전까지
                if (text[j] == 0):  # 압축에 의해 값이 없는 경우
                    j -= 1
                else:
                    text[j+count-3] = text[j] # 시프트를 이용한 디코딩 과정
                    j -= 1
            while (count > 0):  # 압축된 문자열 디코딩
                text[i] = letter
                count -= 1
                i += 1
        else:
            i+=1
    #출력문
    print("\nDecoded Text : ",end="")
    for j in range(len(text)):
        print("%c "%text[j],end="")

text=['a','a','a','a','a','e','f','b','b','b','b','b','b','c','d','e','f','g']
Decoding(Encoding(text))

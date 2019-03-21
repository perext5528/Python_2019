def Matching(pattern, text):
    print("대상 문자열 : ", end="")
    for i in range(len(text)):
        print(text[i],end=" ")
    print("\n찾을 문자열 : ",end="")
    for i in range(len(pattern)):
        print(pattern[i],end=" ")
    print()

    i = 0
    while(i<len(text)):
        j = 0
        if(pattern[0]==text[i]):
            while(i+j<len(text) and j<len(pattern) and pattern[j]==text[i+j]):
                j += 1
                if(j==len(pattern)):
                    print("해당 문자열은 %d번째부터 %d번째에 존재합니다.\n" %((i+1), (i+j)))
        i+=1

pattern=['a','b','a','b','b']
text=['a','b','a','b','a','a','b','b','a','b','a','b','b','a']
Matching(pattern, text)
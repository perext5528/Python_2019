def Matching(text, pattern):
    i=0
    while(i<len(text)):
        if(text[i]==pattern[0]):
            j=0
            while(i+j<len(text) and j<len(pattern) and text[i+j]==pattern[j]):
                j+=1
                if (len(pattern) == j):
                    print("해당 문자열은 %d부터 %d까지 존재" % (i+1, i + j))
        i+=1



text=['a','b','a','b','a','a','b','b','a','b','a','b','b','a']
pattern=['a','b','a','b','b']
Matching(text, pattern)
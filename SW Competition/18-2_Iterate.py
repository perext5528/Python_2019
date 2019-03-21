
inp = int(input("16진수로 변환할 10진 정수 : "))
hexChar = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
hexStr = ""
turn = 1
while inp>0:
    if inp>16 :
        tail = inp%16
        hexStr = hexChar[tail] + hexStr
        inp = inp//16
        print("setp(%d) : %s" %(turn, hexStr))
        turn = turn + 1
    else:
        hexStr = hexChar[inp] + hexStr
        print("setp(%d) : %s" % (turn, hexStr))
        inp = inp//16
#f = open("C:\Users\azure\OneDrive\Desktop\a.txt", "aa")
fa = open("C:/Users/azure/OneDrive/Desktop/a.txt", 'r')

while 1:
    line = fa.readline()
    if not line:break
    print(line, end="")

fa.close()
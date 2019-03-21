def scope_loop():
    n = int(input("학생의 수 (10 ~ 100 사이의 정수) : "))
    if n < 10 or n > 100:
        return scope_loop()
    else:
        return n

student = scope_loop()
cab = ['X' for i in range(student)]

print("Simulation : ")

# 1번째 학생 등교 #
count = 1
for i in range(0, student):
    cab[i] = 'O'
    print(cab[i], end="")
print("")

count = 2
# n번째 학생 등교 #
while count <= student:
    for i in range(0, student):
        if i % count == count - 1:
            if cab[i] == 'O':
                cab[i] = 'X'
            else:
                cab[i] = 'O'
        print(cab[i], end="")
    count = count + 1
    print()

print("Solution(열려있는 사물함 번호) : ")
for i in range(0, student):
    if cab[i] == 'O':
        print("%3d" % (i + 1), end="")

import math

y = int(input("년도를 입력하세요(예 : 2018) : "))
m = int(input("월을 입력하세요(1 ~ 12) : "))
d = int(input("일을 입력하세요(1 ~ 31) : "))
20
if m<3:
    y = y-1
    m = m+12

j = math.floor(y/100)
k = int(y%100)

h = (d + math.floor(26*(m+1)/10) + k + math.floor(k/4) + math.floor(j/4) + 5 * j)%7

day = ["토요일", "일요일", "월요일", "화요일", "수요일", "목요일", "금요일"]

print(day[h])
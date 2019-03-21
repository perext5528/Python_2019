print("Euclid 알고리즘입니다.\n")

a = int(input("첫 번째 숫자를 입력하시오 : "))
b = int(input("두 번째 숫자를 입력하시오 : "))

if(a<b):
    temp = a
    a=b
    b=temp

while(b!=0):
    temp = b
    b=a%b
    a=temp

print("두 수의 최대공약수 : %d" %a)
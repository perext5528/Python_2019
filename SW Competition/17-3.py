temp = org_card_num_list = [0 for i in range(20)]
org_card_num_list = str(input("카드번호를 입력하세요.\n(예 : 9234 5678 9098 7654) : "))

#print(int(org_card_num_list))

check_num = 0

split_card_num_list = [0 for i in range(len(org_card_num_list))]

for i in range(len(org_card_num_list)):
    if org_card_num_list[i] == ' ' or org_card_num_list[i] == '-':



for i in range(len(org_card_num_list)):
    if i % 2 == 1:
        if int(org_card_num_list[i]) * 2 < 9:
            check_num = check_num + int(org_card_num_list[i]) * 2
        else:
            check_num = check_num + int(org_card_num_list[i] * 2) % 10 + int(org_card_num_list[i] * 2) // 10
    elif org_card_num_list[i] is not ' ':
        check_num = check_num + int(org_card_num_list[i])

if check_num % 10 == 0:
    print("이 카드는 유효한 카드입니다.")
else:
    print("이 카드는 유효한 카드가 아닙니다.")

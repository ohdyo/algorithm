# 문제 - 숫자, 기호 앞 순서대로 계산하기
# 리스트 형식으로 string 문자 넣어주고, 최대 3자리 숫자가 나온다.

str1 = "12+5*8"
a_list=['+', '-', '*', '/']
str_sen = list(str1)
print(str_sen)
split_sign_list_idx = []

for i in range(len(str_sen)):
    if str_sen[i] in a_list:
        split_sign_list_idx.append(i)
print(split_sign_list_idx)
(str_sen[:split_sign_list_idx[0]])
# for i in range(len(split_sign_list_idx)):
#     num = int("".join(str_sen[:(split_sign_list_idx[i]-1)]))
#     print(num)
    
    
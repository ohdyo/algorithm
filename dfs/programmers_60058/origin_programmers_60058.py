import sys

# 입력부
input = sys.stdin.readline
p = input().rstrip()

# 생각
# 처음부터 탐색하여 ()의 쌍이 맞을때까지 탐색
# 균형잡힌 문자열 혹은 올바른 문자열 까지는 u에 값 반환, v에는 그 이후를 전부 반환
# v에 해당하는 문자열을 재귀함수로 돌린다.

def result_ans(line):
    # (1) 입력이 빈 문자열인 경우, 빈 문자열 반환환
    if line == '':
        return ''
    
    # (2) 문자열 p를 '균형 잡힌'u, 와 v로 분리
    u, v = split_uv(line)
    
    # (3) 문자열 u가 올바른지 확인인
    if is_correct(u):
        return u + result_ans(v)
    # (4) 올바른 괄호(=갯수는 맞는) 괄호열 아닌 경우
    else :
        # 1. 빈 문자열 '('반환
        # 2. 문자열 v에 대한 재귀수행
        # 3. 빈 문자열 ')' 반환
        # 4. u의 첫번째와 마지막 제거후 반대로 뒤집어서 반환
        # 5. 1~4 까지 반환
        # !! 내 부족한 머리론 결국 두 경우의 return의 크기가 같아야 하는데
        # u가 올바른 괄호열인 경우랑 아닌 경우의 매칭이 머릿속에
        # 이뤄져야 하는데 도저히 매칭이 안됨...
        # => 해당 return값의 'u'에 해당하는 부분은 결국 
        # result_ans(v)를 제외한 모든 부분이고
        # 이를 잘 보면 결국 재귀호출을 감싼 '()'는 reverse()함수의 뒤집기 부분을
        # 앞 뒤를 잘라서 바꾸는 함수이기에 값이 줄어든걸 올바르게 표현하고자 이렇게 작성
        return '(' + result_ans(v) + ')' + reverse(u[1:-1])
        
def split_uv(line):
    count = 0
    for i in range(len(line)):
        if line[i] == '(':
            count += 1
        else :
            count -= 1
        if count == 0:
            u = line[:i+1]
            v = line[i+1:]
            return u,v
    return line,''

def is_correct(u):
    count = 0
    for i in range(len(u)):
        if u[i] == '(':
            count += 1
        else : 
            count -= 1
            
        if count < 0 :
            return False
        
    return True

def reverse(u):
    u_list = list(u)
    for i in range(len(u_list)):
        if u_list[i] == ')':
            u_list[i] ='('
        elif u_list[i] == '(' :
            u_list[i] = ')'
    
    return ''.join(u_list)

print(result_ans(p))
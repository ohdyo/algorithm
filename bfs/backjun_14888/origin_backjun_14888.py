
input = sys.stdin.readline

#입력부부
N = int(input())
num = list(map(int,input().split()))
plus,minus,multi,divide = map(int,input().split())


# 탐색을 위한 dfs 정의
# n = 경유 노드
# sm = 재귀 동안의 계산 결과 값
# add-sub-mul-div 구간 마다의 계산 수식
# mn, mx = 최대 최소 값값 
def dfs(n,sm,add,sub,mul,div):
    global mn, mx

    if sm < int(-1e9) or int(1e9) < sm:
        return

    # 마지막 분기
    # 도착시 함수 종료(무한루프방지)
    if n==N:
        mn = min(mn,sm)
        mx = max(mx,sm)
        return

    
    # 분기 시작
    # i) 처음 호출시(재귀호출X) add값이 존재한다면 조건 실행후 재귀 호출
    # ii) 처음 호출한 함수가 add조건을 지나 sub로 내려가서 해당 조건 충족시 재귀 호출
    # iii) 위의 방식과 마찬가지로 곱하기 나누기 진행
    # iV) 이렇게 처음 호출한 함수가 모든 조건을 충족한다면 최대4갈래의 분기로 나뉘면서 재귀 호출을 진행함함
    if add>0:
        dfs(n+1,sm+num[n],add-1,sub,mul,div)
    if sub>0:
        dfs(n+1,sm-num[n],add,sub-1,mul,div)
    if mul>0:
        dfs(n+1,sm*num[n],add,sub,mul-1,div)
    if div>0:
        dfs(n+1,int(sm/num[n]),add,sub,mul,div-1)

mn, mx = int(1e9),int(-1e9) 

dfs(1,num[0],plus,minus,multi,divide)

print(mx,mn,sep='\n')
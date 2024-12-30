import sys

#입력부
input = sys.stdin.readline
n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().strip())))

drow = [-1,1,0,0]
dcol = [0,0,-1,1]

#영역 별 집의 갯수 세주는 전역변수
count = 0
#노드별 방문 확인 함수
visited = set()

def dfs(row,col):
    # 영역 밖의 범위
    if row < 0 or row >= n or col < 0 or col >= n:
        return 0
    # 이미 방문 혹은 0인 경우
    if (row,col) in visited or graph[row][col] == 0:
        return 0

    #위의 두 경우가 이미 걸려졌으므로 해당 노드는 값이 '1'인 노드
    visited.add((row, col))
    count = 1

    #해당 노드를 가지고 상하 좌우로 이동해서 dfs탐색
    for i in range(4):
        nrow = row + drow[i]
        ncol = col + dcol[i]
        # 집의 갯수 파악을 위해 dfs의 리턴값인 count에 값을 계속 축적
        count += dfs(nrow,ncol)

    return count

num = []
result = 0

#그래프 전체 탐색 반복문
for i in range(n):
    for j in range(n):
        # 방문 안하고 1인 노드 파악
        if (i,j) not in visited and graph[i][j] == 1:
            # 조건에 걸러진 노드가 인접한 값이 '1'인 노드를 탐색
            # 재귀함수를 돌아가면서 인접한 집의 갯수를 dfs에 리턴
            num.append(dfs(i,j))
            # 서로 떨어진 영역의 갯수를 파악
            result += 1

num.sort()
print(result)
for i in num:
    print(i)

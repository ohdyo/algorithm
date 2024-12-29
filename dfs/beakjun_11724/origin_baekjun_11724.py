import sys

input = sys.stdin.readline

# 입력 받기
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]  # 노드 번호가 1부터 시작하므로 크기 n+1

# 그래프 구성
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n + 1)  # 방문 기록 리스트

# DFS 함수 정의
def dfs(node):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor)

# 연결 요소 개수 계산
count = 0
for i in range(1, n + 1):  # 노드 번호가 1부터 시작
    if not visited[i]:  # 방문하지 않은 노드에서 DFS 시작
        dfs(i)
        count += 1

print(count)

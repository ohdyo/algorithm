import sys

input = sys.stdin.readline

# 입력 받기
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]  # 노드 번호가 1부터 시작하므로 크기 n+1

# 그래프 구성
# 입력받은 값들을 인덱스의 번호를 노드로 삼아 해당 노드와 연결된 다른 노드들로 표현되도록 변경
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
print(graph)

visited = set()  # 방문 기록 리스트

# DFS 함수 정의
def dfs(node):
    visited.add(node)
    for next_node in graph[node]:
        if next_node not in visited:
            dfs(next_node)

# 연결 요소 개수 계산
count = 0
for i in range(1, n + 1):  # 노드 번호가 1부터 시작
    if i not in visited:  # 방문하지 않은 노드에서 DFS 시작
        dfs(i)
        print(visited)
        count += 1

print(count)

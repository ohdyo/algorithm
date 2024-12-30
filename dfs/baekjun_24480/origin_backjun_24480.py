import sys

#입력부
input = sys.stdin.readline
N, M, R = map(int,input().split())
graph=[[] for _ in range(N + 1)]


#인덱스별 인접 노드 정리
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 각 노드별로 연결된 노드들을 정렬
for i in range(1, N + 1):
    graph[i].sort(reverse=True) 
print(graph)

#방문기록 & 최종 결과는 dfs 탐색 순서이므로 set과 리스트 선언언
visited = set()
result = []

def dfs(graph,S):
    if S in visited:
        return 0
    visited.add(S)
    result.append(S)
    for next_node in graph[S]:
        if next_node not in visited:
            dfs(graph, next_node)


for i in range(1, N+1):
    if i not in visited:
        dfs(graph,R)

print(result)
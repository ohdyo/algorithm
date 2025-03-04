from collections import deque
import sys

input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]

# 해당 노드의 인접 노드 정리
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
print(graph)

result = []
dfs_visited = set()
def dfs(graph,S):
    if S in dfs_visited:
        return 0
    dfs_visited.add(S)
    result.append(S)
    for next_node in graph[S]:
        if next_node not in dfs_visited:
            dfs(graph, next_node)

def bfs (graph, node):
# 큐 노드 구현 및 첫 node 큐에 삽입
    queue = deque([node])
    #첫 node 방문 처리
    visited = set() # or set()
    visited.add(node)

    #큐가 완전히 빌 때 까지 반복
    while queue:
        #큐에 삽입된 노드 순서대로 꺼내는 메서드popleft
        v = queue.popleft()
        #현재 처리 중인 노드에서 방문하지 않은 노드를 모두 큐에 삽입
        for i in graph[v]:
            if i not in visited:
                queue.append(i)     #1. queue: 1,4 | 2. queue: 4,0,2,3,4  | 3. queue: 3,4,1,3,4   | 4. queue:  4,1,3,4,2,1,2,4
                visited.add(i)   #1, visited 0,1,4  | 2. visited 0,1,4   | 3. visited : 0,1,4,2  | 4. visited : 0,1,4,2,3
    return visited

dfs(graph,v)
print(result)
print(bfs(graph,v))
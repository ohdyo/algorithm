from collections import deque
import sys

# 노드와 간선을 입력 받음
n, k = map(int, sys.stdin.readline().split())

# 2차원 배열을 미리 조정해둠
graph = [[] for _ in range(n)] 

# 간선 정리
for _ in range(k):
    # 입력값을 받고
    u, v = map(int, input().split())
    # 간선은 일반통행이 아니므로 u와 v를 교차하면서 행 열을 바꿔가면서 추가
    graph[u].append(v)
    graph[v].append(u)
    
print(graph)


def bfs (graph, node):
# 큐 노드 구현 및 첫 node 큐에 삽입
    queue = deque([node])
    #첫 node 방문 처리
    visited = [] # or set()
    visited.append(node)
    # que : [0]
    #큐가 완전히 빌 때 까지 반복
    while queue:
        # 큐에서 젤 왼쪽 값을 뺌
        if 6 in visited :
            return visited
        v = queue.popleft()
        # 1. que : []
        # 2. que : [3]
        # 노드에 담긴 값들을 반복해서 확인
        for i in graph[v]: # graph[1] -> [2,5,6]
            # 방문했으면 추가하는 작업을 절대 하면 안된다
            if i not in visited: # 1.[1,3]  # 
                queue.append(i)     # 1. que:[1,3] 2. que:[3,2,5,6]
                visited.append(i)   # 1. visited : [0,1,3] 2. visited : [0,1,3,2,5,6]
    return visited      

print(bfs(graph, 0))

import sys

#입력부
input = sys.stdin.readline
N, M, R = map(int,input().split())
graph=[]
for _ in range(N):
    graph.append(list(map(int,input().split())))

visited = [] * (N+1)


new_graph = [[] for _ in range(N + 1)]

# 간선을 순회하며 그래프를 생성
for a, b in graph:
    new_graph[a].append(b)
    new_graph[b].append(a)

# 각 노드별로 연결된 노드들을 정렬
result_graph = [sorted(neighbors) for neighbors in new_graph]


visited = []

def dfs(graph,S):
    visited.append(S)    
    for node in sorted(graph[S], reverse=True):
        if node not in visited:
            dfs(graph, node)
                
    return visited

print(dfs(result_graph,1))
        
    
    
        
            
        
    
    
    

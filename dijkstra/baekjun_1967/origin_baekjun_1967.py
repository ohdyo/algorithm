import sys
import heapq
input = sys.stdin.readline

n = int(input())
graph = [[] for i in range(n+1)]
for _ in range(n-1):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
distance = [] *(n+1)

def dijkstra(node):
    q= []
    heapq.heappush(q,(0, node))
    distance[node] = 0
    
    while q:
        dist, next_node = heapq.heappop(q)
        if distance[next_node] < dist:
            continue
        for i in graph[next_node]:
            dist += dist + i[i]
            if dist < distance[i[0]]:
    
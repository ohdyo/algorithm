import sys
import heapq

#입력부
input = sys.stdin.readline

n = int(input())
graph = [[] for i in range(n+1)]
for _ in range(n-1):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
print(graph)

#방문기록 함수
visited = set()

def dijkstr(node):
    distance = [float('inf')] * (n+1)
    distance[node] = 0
    visited = set()
    pq = [(0,node)]

    while pq:
        cur_dist, cur_node = heapq.heappop(pq)

        if cur_node in visited:
            continue
        visited.add(cur_node)

        for next_node, dist in graph[cur_node]:
            if next_node not in visited:
                new_dist = cur_dist + dist
                if new_dist < distance[next_node]:
                    distance[next_node] = new_dist
                    heapq.heappush(pq, (new_dist, next_node))

    far_away_node = distance.index(max(distance[1:]))
    max_distance = max(distance[1:])
    return far_away_node, max_distance

node_a,_ = dijkstr(1)

_, max_distance = dijkstr(node_a)

print(max_distance)
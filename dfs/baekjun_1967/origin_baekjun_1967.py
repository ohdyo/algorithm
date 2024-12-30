import sys


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

def dfs(node,distance):
    #방문 기록 삽입
    visited.add(node)
    # 가장 멀리있는 노드 & 최대 거리 리턴 변수
    far_away_node = node
    max_distance = distance

    # 현재 노드와 연결된 노드 순회
    for next_node, dist in graph[node]:
        if next_node not in visited:
            # 재귀 호출로 다음 노드 탐색(다시 여기서 함수 호출)
            next_node, next_dist = dfs(next_node,distance + dist)
            # 재귀호출로 나온 값이 더 멀면 해당 거리로 변수 초기화
            if next_dist > max_distance:
                max_distance = next_dist
                far_away_node = next_node

    return far_away_node, max_distance


visited.clear()
# 임의의 노드(1번 설정)에서 먼 노드 찾기
# 어떤 노드를 인자로 사용하든 동일한 지름을 계산한다.
# 이유는 '방향성'이 없는 트리이기 때문이다.
node_first, _ = dfs(1,0)

visited.clear()
# 첫 dfs로 찾은 노드를 함수의 인자로 사용하여 여기서부터 시작
_, distance = dfs(node_first,0)

print(distance)
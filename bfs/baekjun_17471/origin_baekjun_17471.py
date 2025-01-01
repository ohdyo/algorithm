import collections
import itertools
import sys

input = sys.stdin.readline

# 입력부
n = int(input())
per_num = list(map(int, input().split()))
result = float('inf')
graph = [[] for _ in range(n + 1)]

# 해당 노드의 인접 노드 정리
for i in range(n):
    near_node = list(map(int, input().split()))
    for j in range(1, near_node[0] + 1):
        graph[i + 1].append(near_node[j])
print(graph)

def bfs(group):
    start_node = group[0]  # 시작 노드
    q = collections.deque([start_node])
    visited = set()
    visited.add(start_node)

    total_sum = 0
    while q:
        node = q.popleft()
        # 헷갈렸는데 내가 노드별로 담은 인구수는 0부터 시작이지만
        # 노드의 시작 인덱스번호는 1부터이기에 -1를 해준다.
        # 같은 영역에 포함된 노드의 인구수를 더한다.
        total_sum += per_num[node - 1]
        for next_node in graph[node]:
            if next_node in group and next_node not in visited:  # 그룹 내에서 연결된 노드만 탐색
                q.append(next_node)
                visited.add(next_node)

    return total_sum, len(visited)

# 조합 생성 및 결과 계산
for i in range(1, n // 2 + 1):
    # 1부터 n까지 범위에서 길이가 i만큼 분리해서 조합
    comb = list(itertools.combinations(range(1, n + 1), i))
    #생성된 조합을 각각 탐색
    for combi in comb:
        # 생성된 조합을 탐색하여 combi에 담긴 노드의 리스트를 인자로 삼아 탐색후 값 반환
        sum1, len1 = bfs(combi)
        # 조합에서 제외된 노드들끼의 리스트를 인자로 사용하여 bfs인자로 사용후 값 반환
        sum2, len2 = bfs([i for i in range(1, n + 1) if i not in combi])
        if len1 + len2 == n:  # 두 그룹이 모두 연결된 경우
            result = min(result, abs(sum1 - sum2))

# 결과 출력
if result != float('inf'):
    print(result)
else:
    print(-1)

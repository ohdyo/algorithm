from collections import deque
import sys
import copy

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


#벽 3번 세웠으면 실행될 바이러스 전염을 위한 bfs 함수수
def bfs(graph, n, m):
    max_result = 0
    queue = deque()
    tmp = copy.deepcopy(graph)  #! 백트래킹을 제거하기위한 임시 저장 tmp

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                queue.append((i, j))  # 바이러스 위치 큐에 삽입

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and ny >= 0 and ny < n and nx < m:
                if tmp[ny][nx] == 0:
                    tmp[ny][nx] = 2
                    queue.append((ny, nx)) #바이러스 전염 실행 반복문 및 큐 추가가

    # 바이러스가 퍼지고 나서, 안전 영역의 크기 계산
    result = 0
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 0:
                result += 1
    max_result = max(result, max_result) # 최대값 갱신 함수수

    return max_result # 최대값 반환환


# 벽 세우기
def build(graph, n, m):
    max_result = 0
    empty_spaces = []  # 벽을 세울 수 있는 위치들 저장

    # 벽을 세울 수 있는 빈 칸의 좌표를 empty_spaces 리스트에 저장
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                empty_spaces.append((i, j))

    # 3개의 벽을 세운 모든 경우를 계산
    

    return max_result


n, m = map(int, sys.stdin.readline().split())  # 지도 크기 입력
graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))  # 지도 정보 입력

# 벽을 세운 후 가능한 최대 안전 영역을 계산
max_result = build(graph, n, m)
print(max_result)  # 최대로 구한 안전 영역 크기 출력

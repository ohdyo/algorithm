from collections import deque
import sys
import copy

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 바이러스 퍼뜨리기 및 최대 영역 크기 갱신
def bfs():
    global max_result
    queue = deque()
    tmp = copy.deepcopy(graph)  # graph의 깊은 복사본을 만들어 tmp에 저장

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
                if tmp[ny][nx] == 0:  # 빈 칸이면 바이러스 퍼뜨리기
                    tmp[ny][nx] = 2
                    queue.append((ny, nx))

    # 바이러스가 퍼지고 나서, 안전 영역의 크기 계산
    result = 0
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 0:  # 0이면 안전 구역
                result += 1
    max_result = max(result, max_result)  # 가장 큰 안전 영역 기록


# 벽 세우기
def build(cnt):
    if cnt == 3:  # 벽을 3개 세운 경우
        bfs()  # 바이러스 퍼뜨리기
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:  # 빈 칸에 벽을 세움
                graph[i][j] = 1  # 벽 세우기
                build(cnt + 1)  # 벽을 더 세우기 위해 재귀 호출
                graph[i][j] = 0  # 벽을 세운 곳을 다시 빈 칸으로 되돌리기


n, m = map(int, sys.stdin.readline().split())  # 지도 크기 입력
graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))  # 지도 정보 입력

max_result = 0
build(0)  # 벽을 3개 세우는 모든 경우를 시도

print(max_result)  # 최대로 구한 안전 영역 크기 출력

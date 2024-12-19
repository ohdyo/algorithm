from collections import deque
import sys
import copy

#일반 적으로 상하좌우 즉 이동방향을 표현하기 위해서 표현한 x,y축 리스트 (기하의 움직임 느낌)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 바이러스 퍼뜨리기 및 최대 영역 크기 갱신
# bfs너비 탐색으로 바이러스를 퍼뜨려 계산하기 위해 정의
def bfs():
    # 함수 내부에서도 변화시 적용시키기 위해 전역 변수로 선언
    # 바이러스 시작노드 큐 생성
    # tmp에 확산 전 그래프 담고 거기서 바이러스 확산
    global max_result
    queue = deque()
    tmp = copy.deepcopy(graph)

    # 2차원으로 이뤄진 graph리스트를 순회
    # 2(=바이러스 처음 위치)의 위치 찾기
    # 큐에 바이러스 노드 삽입
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                queue.append((i, j))

    #바이러스를 찾았다면 큐에 값이 존재하여 while문 시작
    #큐에서 x와 y의 좌표를 꺼내고 pop으로 queue에서 삭제
    while queue:
        y, x = queue.popleft()
        # i의 범위 0~3(상하좌우의 기능을 위해 범위가 0부터 3)으로 지정하여 바이러스 이동
        for i in range(4):
            # nx와 ny는 이동 후 바이러스의 위치
            nx = x + dx[i]
            ny = y + dy[i]
            #초기 설정한 영역 내부에서 바이러스가 퍼지게 하도록 조건을 걸어둠
            if nx >= 0 and ny >= 0 and ny < n and nx < m:
                # 0이면 빈공간이므로 바이러스를 확산했다 표시하기위해 해당 좌표의 값을 2로 바꿈
                # 변한 공간을 큐에 저장
                if tmp[ny][nx] == 0:
                    tmp[ny][nx] = 2
                    queue.append((ny, nx))
    #안전 영역의 개수 변수
    result = 0
    # 모든 공간에 대해 값을 비교
    for i in range(n):
        for j in range(m):
            #0(=빈 공간)이면 result의 갯수 증가
            if tmp[i][j] == 0:
                result += 1
    #result와 max_result의 값을 비교하여 큰 값을 전역 변수에 대입
    max_result = max(result, max_result)


# 벽 세우기
def build(cnt):
    # 벽 설치 3번 다 했으면 bfs정의 함수 호출 후 return
    if cnt == 3:
        bfs()
        return
    #벽을 세우기 위한 전 영역 순회
    for i in range(n):
        for j in range(m):
            # 빈 공간이면 벽을 세움
            if graph[i][j] == 0:
                graph[i][j] = 1
                # 재귀호출을 통해 벽을 하나 더 세움
                build(cnt + 1)
                # !! backtracking
                # 모든 벽 세우기를 가능하게 하기 위해 이전 상태로 되돌림
                # 그래야 각각의 경우 마다 변하는 result의 값과 누적해서 변화한 max_result의 값을 계속해서 비교할수 있다.
                # 자신이 생각하는 최선의 경우의 수가 이미 나왔더라도 다른 모든 경우의 수 또한 검사가 필요하기에 backtracking을 통해 검증한다.
                # 최선의 경우가 안나올 경우 불필요한 경로를 되돌리게 해주고 최적의 경우를 찾아가는 방식
                graph[i][j] = 0



n, m = map(int, sys.stdin.readline().split())
graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))
max_result = 0

build(0)
print(max_result)
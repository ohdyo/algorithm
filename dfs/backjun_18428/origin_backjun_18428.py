# 생각
# 학생들이 선생님의 상,하,좌,우에 안보이게끔 시야만 잡아준다
# 선생님의 입장에서 상 하 좌 우 끝까지 깊이 있게 탐색을 위해 dfs
# 해당 경우는 최단의 경우보다 가능한 경우를 찾는거이에 dfs 활용

import sys

#입력부
input = sys.stdin.readline
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(str, input().split())))

# 결과값 반환
def find_result(graph) :
    #선생님 찾기
    for row in range(n):
        for col in range(n):
            if graph[row][col] == 'T':
                #위치 파악한 노드의 인덱스번호를 이용해서 학생 찾기 시작
                result = search_s(row,col)
                if result == False:
                    return False
    return True

# 학생 찾기
def search_s(row,col) :
    #상 하 좌 우 나눠서 파악
    for i in range(1,n):
        if row-i>=0:
            if graph[row-i][col] == 'O':
                break
            elif graph[row-i][col] == 'S':
                return False

    for i in range(1, n):
        if row+i<n:
            if graph[row+i][col] == 'O':
                break
            elif graph[row+i][col] == 'S':
                return False

    for i in range(1, n):
        if col-i>=0:
            if graph[row][col-i] == 'O':
                break
            if graph[row][col-i] == 'S':
                return False

    for i in range(1, n):
        if col+i<n:
            if graph[row][col+i] == 'O':
                break
            if graph[row][col+i] == 'S':
                return False
    return True

#벽을 세울수 있는 경우의 수 탐색
def build_wall(wall,graph):
    if wall == 3:
        result = find_result(graph)
        if result == True:
            print('YES')
            exit()
        return
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'X':
                graph[i][j] = 'O'
                build_wall(wall+1,graph)

build_wall(0,graph)
print('NO')
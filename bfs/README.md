알고리즘을 공부할때 잊지 말아야할 개념
![](https://velog.velcdn.com/images/ohdyo/post/345bafc4-b611-41ef-b5a9-471b4797d3a4/image.png)


# BFS(Breadth-First-Search)
- BFS는 기본적으로 큐(Queue) or 재귀호출(self-call)을 이용하여 구현
시작 노드와 인접한 자식 노드를 먼저 탐색 후 그 아래의 자식노드로 이동하여 탐색
- 답이 여러개인 경우에도 **최단 경로 보장**

![](https://velog.velcdn.com/images/ohdyo/post/b8bdef28-d06b-4e8a-a1dd-738af44c5863/image.png)

_BFS알고리즘의 구체적인 동작 과정_
1. 탐색 시작 노드 정보를 큐에 삽입하고 방문 처리(visited()) 진행
2. 큐에서 노드를 꺼내 방문하지 않은 인접 노드 정보를 모두 큐에 삽입하고 방문 처리 진행
3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복


### 특징
1. 큐를 이용하여 구현
2. 시작노드에서부터 인접한 노드 모두 탐색 후 다음 자식노드로 이동
3. **최단 경로 혹은 최단 거리** 구하는데 활용

## BFS 소스코드 구현
```
from collections impoert deque

def bfs (graph, node):
	# 큐 노드 구현 및 첫 node 큐에 삽입
	queue = deque([node])
    #첫 node 방문 처리
    visited = []
    visited.append(node)
    
    #큐가 완전히 빌 때 까지 반복
    while queue:
    	#큐에 삽입된 노드 순서대로 꺼내는 메서드popleft
        v = queue.popleft()
        #현재 처리 중인 노드에서 방문하지 않은 노드를 모두 큐에 삽입
        for i in graph[v]:
        	if not (visited[i]):
            	queue.append(i)
                visited.append([i])
```



# 예제
## BFS
### 1번(백준 18352번)
어떤 나라에는 1번부터 N번까지의 도시와 M개의 단방향 도로가 존재한다. 모든 도로의 거리는 1이다.

이 때 특정한 도시 X로부터 출발하여 도달할 수 있는 모든 도시 중에서, 최단 거리가 정확히 K인 모든 도시들의 번호를 출력하는 프로그램을 작성하시오. 또한 출발 도시 X에서 출발 도시 X로 가는 최단 거리는 항상 0이라고 가정한다.

예를 들어 N=4, K=2, X=1일 때 다음과 같이 그래프가 구성되어 있다고 가정하자.
![](https://velog.velcdn.com/images/ohdyo/post/945c1dfa-8eb7-42e8-a15a-8c806f06f24e/image.png)
1. 시작 도시(노드)에서 지정한 거리의 도시들을 탐색하는 문제
2. bfs를 통해 전체 탐색
3. 이미 방문한 도시(노드) 기록
```
import sys
from collections import deque

#N : 도시의 개수
#M : 간선(=도로)의 개수
#K : 시작 도시 기준에서 해당 도시의 거리 지정
#X : 시작 도시
input = sys.stdin.readline
N, M, K, X = map(int, input().split())

#도시의 번호에 맞춰서 시작 범위를 1부터 시작하게 만듬
graph[ [] for _ in range[N+1] ]
# que 선언
Que = deque()
# 방문 기록을 위한 set함수 선언
visited = set()

# 거리를 표현하기 위한 리스트 함수 선언
# 0번을 제외한 1번 인덱스부터 도시를 표현하기 위해 *(N+1)을 사용
distances = [0]*(N+1)

#간선의 갯수를 입력받고 해당 간선을 표현하기 위한 입력부
#2차원 배열인걸 생각하고 코드 확인
for i in range(M):
	x, y = map(int, input().split())
    graph[x].append[y]

#초기 큐 설정
#초기 visited 설정
Que.append(X)
visited.add(X)

# Queue 실행 문장
# 초기 도시로 설정한 Que의 값을 node에 꺼내고 삭제(pop)
# 해당 도시와 연결된 다른 도시의 이름(크기 아님)을 가지고 for문을 반복
# next에 해당하는 도시에 가본적이 없으면 Que와 visited에 값을 삽입
# 순회하여 방문했는지 체크하고 없으면 Que에서 제거하는 방식으로 반복문 수행
while Que:
	node = Que.popleft()
    for next in graph[node] :
    	if next not in visited:
        	Que.append(next)
            visited(next)
            distance[next] = distance[node] +1

# distances리스트를 순회하여 거리 K만큼 있는지 확인
# 인덱스 범위 1부터 N까지를 순회하며 K만큼의 거리의 인덱스 번호를 출력해줌
if K in distances:
	for destination in range(1, N+1) : 
    	if distances[destination] == K :
        	print(destination)

# 순회를 다 하고 값이 없다면 -1을 출력
else:
	print(-1)          
```
### 2번(백준 14502)
인체에 치명적인 바이러스를 연구하던 연구소에서 바이러스가 유출되었다. 다행히 바이러스는 아직 퍼지지 않았고, 바이러스의 확산을 막기 위해서 연구소에 벽을 세우려고 한다.

연구소는 크기가 N×M인 직사각형으로 나타낼 수 있으며, 직사각형은 1×1 크기의 정사각형으로 나누어져 있다. 연구소는 빈 칸, 벽으로 이루어져 있으며, 벽은 칸 하나를 가득 차지한다. 

일부 칸은 바이러스가 존재하며, 이 바이러스는 상하좌우로 인접한 빈 칸으로 모두 퍼져나갈 수 있다. 새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다.

* 입력과 출력 콘솔창
```
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
27
```
1. 바이러스는 상하 좌우의 빈 공간을 감염시킨다
	=> BFS 너비 탐색의 형식으로 공간을 감염시킴
2. 모든 빈공간을 순회하여 벽을 설치하도록 진행
3. 모든 경우의 수를 진행할수 있도로 **backtracking**이용
```
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


# 전체 공간 입력부
n, m = map(int, sys.stdin.readline().split())
# 그래프 리스트 생성
graph = []
# 영역 내 상태 입력부
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))
#초기 결과값 설정
max_result = 0

#벽 찾기 시작
build(0)
print(max_result)
```
* If
1. 전역변수 max_result를 안쓰고 return 값으로 max_result를 반환한다면?
=> 결론적으로 가능하다. 이 부분은 취향차이로 자바에 익숙한 나는 이 방법을 선호한다.
해서 'global'을 떼고 해당하는 변수를 반환값으로 보내서 값을 출력하도록 유도할 것이다.
2. backtracking을 없애고 tmp에 초기 graph를 설정해서 계속 사용한다면?
=> backtracking을 사용하지 않고 탐색을 하고 싶다면 해당 부분에 for문을 돌려서 찾는 방법도 존재한다. 하지만 그런경우 지금은 총 3번의 for문이 필요하게 되는데 이 방식은 비효율적이고 코드의 가독성을 떨어뜨린다.

### 3번(백준 18405)
NxN 크기의 시험관이 있다. 시험관은 1x1 크기의 칸으로 나누어지며, 특정한 위치에는 바이러스가 존재할 수 있다. 모든 바이러스는 1번부터 K번까지의 바이러스 종류 중 하나에 속한다.

시험관에 존재하는 모든 바이러스는 1초마다 상, 하, 좌, 우의 방향으로 증식해 나간다. 단, 매 초마다 번호가 낮은 종류의 바이러스부터 먼저 증식한다. 또한 증식 과정에서 특정한 칸에 이미 어떠한 바이러스가 존재한다면, 그 곳에는 다른 바이러스가 들어갈 수 없다.

시험관의 크기와 바이러스의 위치 정보가 주어졌을 때, S초가 지난 후에 (X,Y)에 존재하는 바이러스의 종류를 출력하는 프로그램을 작성하시오. 만약 S초가 지난 후에 해당 위치에 바이러스가 존재하지 않는다면, 0을 출력한다. 이 때 X와 Y는 각각 행과 열의 위치를 의미하며, 시험관의 가장 왼쪽 위에 해당하는 곳은 (1,1)에 해당한다.

예를 들어 다음과 같이 3x3 크기의 시험관이 있다고 하자. 서로 다른 1번, 2번, 3번 바이러스가 각각 (1,1), (1,3), (3,1)에 위치해 있다. 이 때 2초가 지난 뒤에 (3,2)에 존재하는 바이러스의 종류를 계산해보자.

입력
첫째 줄에 자연수 N, K가 공백을 기준으로 구분되어 주어진다. (1 ≤ N ≤ 200, 1 ≤ K ≤ 1,000) 둘째 줄부터 N개의 줄에 걸쳐서 시험관의 정보가 주어진다. 각 행은 N개의 원소로 구성되며, 해당 위치에 존재하는 바이러스의 번호가 공백을 기준으로 구분되어 주어진다. 단, 해당 위치에 바이러스가 존재하지 않는 경우 0이 주어진다. 또한 모든 바이러스의 번호는 K이하의 자연수로만 주어진다. N+2번째 줄에는 S, X, Y가 공백을 기준으로 구분되어 주어진다. (0 ≤ S ≤ 10,000, 1 ≤ X, Y ≤ N)

3 3
1 0 2
0 0 0
3 0 0
2 3 2

출력
S초 뒤에 (X,Y)에 존재하는 바이러스의 종류를 출력한다. 만약 S초 뒤에 해당 위치에 바이러스가 존재하지 않는다면, 0을 출력한다.

3

```
import sys
from collections import deque

# 1. 바이러스가 퍼지면서 모든 공간을 탐색한다.(BFS)
# 2. 초(=반복문)을 반복할때마다 상하 좌우로 바이러스가 움직인다.
# 3. 바이러스에는 수가 낮은은 개체가 우선순위를 가진다.

drow = [-1, 1, 0, 0]
dcol = [0, 0, -1, 1]


# 정사각형 공간
def bfs(n,graph,s,y,x):
    que= []
    
    for i in range(n):
        for j in range(n):
            if graph[i][j] >0:
            	#큐에 
                que.append((graph[i][j],0,i,j))
    
    #!문제의 특이점
    # 바이러스의 우선순위를 주기위한 오름차순 정렬
    # 큐에 등록
    que.sort()
    queue = deque(que)
    
    while queue:
        virus,sec,row,col = queue.popleft()
        if sec == s:
            return graph[y-1][x-1]
        for i in range(4):
            next_row = row + drow[i]
            next_col = col + dcol[i]
            if 0<=next_row<n and 0<=next_col<n :
                if graph[next_row][next_col] == 0:
                    graph[next_row][next_col] = virus
                    queue.append((graph[next_row][next_col],sec + 1, next_row, next_col))
    


# 입력부
n, k = map(int, sys.stdin.readline().split())
graph = []

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

s, y, x = map(int, sys.stdin.readline().split())

print(bfs(n,graph,s,y,x))

```

### 4번(백준 10026)
적록색약은 빨간색과 초록색의 차이를 거의 느끼지 못한다. 따라서, 적록색약인 사람이 보는 그림은 아닌 사람이 보는 그림과는 좀 다를 수 있다.

크기가 N×N인 그리드의 각 칸에 R(빨강), G(초록), B(파랑) 중 하나를 색칠한 그림이 있다. 그림은 몇 개의 구역으로 나뉘어져 있는데, 구역은 같은 색으로 이루어져 있다. 또, 같은 색상이 상하좌우로 인접해 있는 경우에 두 글자는 같은 구역에 속한다. (색상의 차이를 거의 느끼지 못하는 경우도 같은 색상이라 한다)

예를 들어, 그림이 아래와 같은 경우에

RRRBB
GGBBB
BBBRR
BBRRR
RRRRR
적록색약이 아닌 사람이 봤을 때 구역의 수는 총 4개이다. (빨강 2, 파랑 1, 초록 1) 하지만, 적록색약인 사람은 구역을 3개 볼 수 있다. (빨강-초록 2, 파랑 1)

그림이 입력으로 주어졌을 때, 적록색약인 사람이 봤을 때와 아닌 사람이 봤을 때 구역의 수를 구하는 프로그램을 작성하시오.

_풀이 방법_
1. 영역을 어떻게 나눌지 고민한다.
	-> 영역을 나누기 위해 탐색을 할때 같은 색깔의 노드를 찾아서 탐색해서 영역을 구분짓자
2. 나눈 영역의 갯수를 어떻게 표현할지 생각해라.
	-> 영역을 나눴다면 어떻게 갯수를 표현할지 생각해라
3. 영역이 변경될 경우 어떻게 프로젝트를 수행할건지 생각해라.
	-> 영역을 임시로 저장한 변수에 조건에 맞게 영역을 바꿔서 새로 전개해라.
```
import sys
from collections import deque
import copy

drow = [-1,1,0,0]
dcol = [0,0,-1,1]

#bfs 정의
#해당 bfs는 시작 노드와 같은 색깔의 인접한 노드를 큐에 삽입하고 방문기록 남김
def bfs(row,col,visited,graph):
    que = deque()
    que.append((row,col))
    visited.add((row,col))
    
    while que:
        row, col = que.popleft()
        for i in range(4):
            nrow = row + drow[i]
            ncol = col + dcol[i]
            if 0<= nrow and nrow <n and  0<= ncol and ncol <n :
                if (nrow,ncol) not in visited: 
                    if graph[nrow][ncol] == graph[row][col] :
                        que.append((nrow,ncol))
                        visited.add((nrow,ncol))

#영역 갯수 체크
#시작 노드를 모르기에 처음부터 시작해서 bfs를 탐색한다.
#인접한 노드가 같은 색깔인 경우 bfs에서 방문기록을 남기기에 색깔이 같으면 result값이 상승하지 않는다.
#같은 색깔의 인접한 노드가 없다면 방문기록을 visited()에 남긴 채 bfs를 나와 result값 증가시킨다.
#영역을 다 나눌때까지 해당 반복문을 진행한다.
def checking_area(n,graph):
    result = [0,0]
    tmp_graph = copy.deepcopy(graph)
    
    visited = set()
    for i in range(n): 
        for j in range(n):
            if (i,j) not in visited:
                bfs(i,j,visited,graph)
                result[0] += 1
    
    other_visited = set()
    for i in range(n):
        for j in range(n):
            if tmp_graph[i][j] == 'G':
                tmp_graph[i][j] = 'R'
    for i in range(n):
        for j in range(n):            
            if (i,j) not in other_visited:
                bfs(i,j,other_visited,tmp_graph)
                result[1] += 1
    return result


input = sys.stdin.readline
n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(str, sys.stdin.readline().strip()))) 

print(' '.join(map(str,checking_area(n,graph))))

```


## 정리
BFS의 기본 적인 형식이 있다.
1. 처음에 que와 방문기록을 위한 set()을 지정해준다.
2. 시작 노드를 탐색해서 que에 추가한다.
3. 추가한 que의 값을 꺼내고 꺼낸 값을 가지고 문제의 조건에 맞게 반복문을 돌린다.
4. 기본적으로 제한을 둔 공간(n,m)의 범위 내에서 해당하는 노드를 찾도록 조건을걸고 que에 추가
하고 방문기록을 위해 set에도 같이 추가한다.
![](https://velog.velcdn.com/images/ohdyo/post/4619190b-7d22-429b-a4e8-db7f3ba9b077/image.png)



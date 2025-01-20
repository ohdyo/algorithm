# 큐 (Queue)
## Queue란?
- 한쪽으로 들어가고 다른 한쪽으로 나오는 구조 First - In - First - Out(FIFO)
- 큐에 새로운 데이터 추가는 enqueue
- 큐에 데이터 삭제응 dequeue
---
## Queue 구현
### 파이썬 코드 - 리스트로 구현
- 리스트를 사용하면 enqueue()의 추가 동작은 O(1) 이며,
dequeue() 는 O(N)
- queue는 리스트로 구현하는것은 비효율적이다. 리스트의 끝 원소만을 다루기에 다른 요소의 원소를 건드리는것은 느리다. 왜냐하면 ***첫 원소를 빼면 앞으로 한칸씩 이동하는 작업***을 해야하기 때문
    - 그래서 collection.dequeue를 아래에서 사용한다.
    - 이 방식은 queue를 리스트로 구현시의 단점을 없애준다.
    - 만약 둘다 싫으면 linked list를 사용하면 되는데 이건 여기서 안알려줍니다. 알고 싶은면 직접 공부!
- ***왜 리스트보다 시간복잡도가 좋은걸까?***
    - Python의 list는 **동적 배열(dynamic array)**로 구현
        - 특정 요소에 바로 접근 가능 (임의 접근 빠름)
        - 배열의 시작이나 중간에 요소를 삽입/삭제할 경우, 데이터를 한 칸씩 이동해야 하기 때문에 시간 복잡도가 $ 𝑂(𝑛)$ 
    - collections.deque는 ***이중 연결 리스트(doubly linked list)*** 로 구현
        - 각 노드가 이전 노드와 다음 노드에 대한 포인터를 가지는 구조
            - 포인텀나 수정하면 되기에 데이터 이동 필요 X
        - 임의 접근(예: deque[i])이 지원되지 않으며, 순차적으로 노드를 탐색해야 하므로 $O(n)$

| 연산          | list | deque |
|----------|---------|--------|
|맨 뒤에 삽입(append)|$O(1)$|$O(1)$|
|맨 앞에 삽입(insert(0,x))|$O(n)$|$O(1)$|
|맨 뒤에 제거(pop())|$O(1)$|$O(1)$|
|맨 앞에 제거(pop(0))|$O(n)$|$O(1)$|
|임의 접근(list[i])|$O(1)$|$O(n)$|

```python
Class ListQueue(object):
    def __init__(self):
        welf.queue = []

    def dequeue(self):
        if len(self.queue) == 0:
            return -1
        return self.queue.pop(0)

    def enqueue(self, n):
        self.queue.append(n)
        pass

    def printQueue(self):
        print(self.queue)

if __name__ == "__main__":
    lq = ListQueue()
    lq.enqueue(1)
    lq.enqueue(2)
    lq.enqueue(3)
    lq.enqueue(4)
    lq.enqueue(5)
    lq.printQueue()
    print(lq.dequeue())
    print(lq.dequeue())
    print(lq.dequeue())
    print(lq.dequeue())
    print(lq.dequeue())
    lq.printQueue()
```
### collecgtion.deque 모듈 사용
- deque(double-ended-queue)의 줄임말, 앞과 뒤 양방향 데이터 처리가 가능한 자료구조
- list와 유사해 보이지만 ***시간복잡도 확인시 앞뒤 데이터 처리 속도가 O(1)으로 매우 빠름*** (list는 O(N))
- 사용하는 함수는 리스트 혹은 스택과 용어가 같다. 나올때마다 외워두자
```python
from collections import deque

dq = deque([])

dq.append(1)
dq.append(2)
dq.append(3)
dq.append(4)
print(dq)

print(dq.popleft())
print(dq.popleft())
print(dq.popleft())
print(dq.popleft())
print(dq)
```
---
## 예제
### 문제 1. 기본 큐 구현
- 정수를 큐에 삽입은 enqueue {num}
- 큐에서 정수를 삭제는 dequeue, 비어있으면 Empty출력
- front로 큐의 첫번쨰 값 출력, 없으면 Empty 출력
- 각각의 명령어 다음에 출력문이 나오도록 코드 작성
```
# 입력
6
enqueue 10
enqueue 20
dequeue
front
dequeue
front

#출력
10 
20 
20 
Empty
```

### 문제 2 큐 회전
- 큐에 1부터 N까지의 숫자가 들어있다
- 큐를 회전 시킨다.
- 회전 : 큐의 첫번째 요소를 맨 뒤로 보낸다.
- 첫번째 줄에 큐의 크기 N, 회전 횟수 K 입력한다.
- K번 회전 후의 큐 출력
```
# 입력
5 3
# 출력
4 5 1 2 3
```

### 문제 3 우선순위 큐
- 삽입된 값 중 우선순위가 가장 높은 값을 먼저 반환
    - 우선순위의 기준 : 큰 숫자
- 정수를 큐에 삽입한다 enqueue 구현
- 큐에서 우선순위가 높은 숫자 삭제 dequeue 구현
    - 삭제돈 값을 출력하도록 만들기
    - 없을시 Empty 출력
- 첫번째 줄에 명령어의 갯수 N개 입력
- 두번째 줄부터 명령어 작성
    - enqueue {num}
    - dequeue
- dequeue의 경우 실행시 바로 해당하는 출력구문이 출력되도록 구현현
```
# 입력
6
enqueue 10
enqueue 20
dequeue
enqueue 15
enqueue 5
dequeue
# 출력
20
15
```
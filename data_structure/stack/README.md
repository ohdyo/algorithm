# 스택
- 한쪽 끝에서만 데이터를 넣고 뺄 수 있는 ***후입선출*** 구조
- ***Last In First Out (LIFO)***

<img width=50% src="https://images.velog.io/images/alkwen0996/post/868c8d06-6e65-4c0d-8e83-4afbdad88f59/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202022-01-13%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%202.38.03.png"/>

- 먼저 들어간 데이터가 가장 나중에 나오는 걸 확인 가능

---
## 스택 기본 연산
- pop() : 스택에서 가장 위에 있는 항목을 제거하고 반환
- push(item) : item 하나를 스택의 가장 윗부분에 추가
- peek() : 스택의 가장 위에 있는 항목을 반환
- isEmpty() : 스택이 비어있으면 True 반환

### 파이썬은 collections 모듈 + 직접 구현 가능
- collections 모듈에서 ***deque***함수를 호출해서 스택의 모든 연산들을 편하게 사용 가능하다.
    - 이 방법은 결국 라이브러리를 가져와야 하기에 파일이 무거워져 스택 문제에서는 지양한다.
- 리스트에도 기본적인 스택의 함수가 들어가 있다.


1. collections 모듈 이용
```python
from collections import deque

dq=deque() # 덱 생성
dq.append() # 덱의 가장 오른쪽에 원소 삽입
dq.popleft() # 가장 왼쪽 원소 반환
dq.appendleft() # 덱의 가장 왼쪽에 원소 삽입
dp.pop() # 가장 오른쪽 원소 반환
dp.clear() # 모든 원소 제거
dp.copy() # 덱 복사
dp.count(x) #x와 같은 원소의 개수를 계산
```

2. 직접 구현
- 파이썬은 리스트로 스택을 구현한다.
```python
class Stack:
    def __init__(self):
        self.stack = []

    # 스택에 요소를 추가 (push)
    def push(self, item):
        self.stack.append(item)

    # 스택에서 요소를 제거하고 반환 (pop)
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("Pop from an empty stack")

    # 스택의 가장 위에 있는 요소를 반환 (peek)
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("Peek from an empty stack")

    # 스택이 비어 있는지 확인
    def is_empty(self):
        return len(self.stack) == 0

    # 스택의 크기 반환
    def size(self):
        return len(self.stack)
```

---

## 스택 시간 복잡도
- 스택에 대한 데이터 추가 삭제의 경우 시간복잡도는 늘 O(1) 이다.
- 특정 데이터를 찾는 탐색의 경우는 O(n)의 시간복잡도를 가진다.

---

## 스택 활용
- 스택 예제
    1. 괄호의 짝 검사
    2. 웹 브라우저 방문 이력
    3. 문자 역순 정렬
    4. 수식의 괄호 검사

---
## 스택을 이용한 문제
### 1. 괄호 검사
- <a href= https://www.acmicpc.net/problem/9012>백준 알고리즘 9012번</a>
- 문제 풀이 방식
    - 여기다가 풀이 적어보세요잇!

```python

```
### 2. 문자열 뒤집기
- 입력 받은 문자열을 스택을 이용해 뒤집으세요.
```python

```

### 3. 최소 스택
- 직접 스택의 메소드를 구현해보자
- 하나의 클래스에 push,pop,top,peek을 구현해보자.
```python

ms = MinStack()
ms.push(5)
ms.push(3)
ms.push(7)
print(ms.get_min())  # 3
ms.pop()
print(ms.get_min())  # 3
ms.pop()
print(ms.get_min())  # 5
```
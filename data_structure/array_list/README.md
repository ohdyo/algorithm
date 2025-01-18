# 배열 & 리스트
- 데이터를 연속적으로 저장하는 자료구조
- 알고리즘 코딩 테스트에선 주로 리스트를 사용
## 리스트를 많이 사용하는 이유
1. 내장 메서드의 유용성
   1. 삽입, 삭제, 정렬, 슬라이싱을 지원하는 내장 메서드가 많음
   2. 자주 쓰는 메서드 append(), pop(),sort(),reverse(),extend()
2. 다양한 데이터 저장 가능
   1. 파이썬 배열은 동일한 데이터만 저장 가능
3. 라이브러리와의 호환성
    1. 코딩 테스트에서 주로사용하는 라이브러리는 리스트가 기본
    ex) heapq, collections, itertools
---
## 리스트에서 주로 사용하는 내장 메서드
### append()
- 요소를 추가해줌
```python
origin_list = [1,2,'a','b']
origin_list.append(False)
print(origin_list)
```
### pop()
- 기존 리스트에서 마지막 요소를 제거하고, 마지막 요소 반환
```python
origin_list = [1,2,'a','b']
pop_result = origin_list.pop()
print(pop_result)
```

### sort()
- 리스트의 객체를 리스트 안에서 순서대로 정렬
- 문자는 알파벳 순으로 정렬, 문자 숫자 섞여있는 경우  TypeError 발생
```python
origin_list = [3,1,2,5,4,8,6]
origin_list.sort()
print(origin_list)
```

### extend()
- 기존 리스트에 다른 리스트 연결
```python
origin_list = [1,2,'a','b']
con_list = [3,4,5]
origin_list.extend(con_list)
print(origin_list)
```
### count()
- 리스트에서 해당하는 인덱스의 값의 개수를 세서 반환
```python
origin_list = [1,1,2,3,4,5]
count_num = origin_list.count(1)
print(count_num)
```
### join()
- 리스트에 담긴 값들을 특정구분자로 값을 구별해서 출력시켜줌
```python
origin_list = ['A', 'B', 'C', 'D']
print(''.join(origin_list))
second_origin_list = ['E','F','G','H']
print('+'.join(second_origin_list))
```

### lambda(람다)
- 함수와 비슷하게 사용된다.
- 코드열에서 함수로 정의하지 않고 함수처럼 사용 가능하다.
- 주로 입력받은 요소에 바로 적용시킬때 사용한다.
```python
lambda_list = list(map(lambda x:x * 2, map(int,input().split())))
print(lambda_list)
```

### filter()
- 리스트의 모든 요소 중에서 조건에 맞는 요소만을 반환
```python
filter_list = list(filter(lambda x: x%2 == 1,map(int,input().split())))
print(filter_list)
```

### reduce()
- functools모듈에서 가져와서 import를 진행해서 사용해야한다.
- 누적 값에 대한 결과를 반환할때 사용한다.
```python
from functools import reduce
reduce_result = reduce(lambda x,y : x * y, map(int,input().split()))
print(reduce_result)
```

### len(list)
- 리스트의 길이

### min(list) & max(list)
- 최대 최솟값 반환
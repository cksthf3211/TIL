# Do it ! 알고리즘 코딩 테스트
## 수요일까지 04 정렬(93~130) 문제 풀이 + 계수 정렬
### 버블정렬
- 두 인접한 데이터의 크기를 비교해 정렬하는 방법
- 시간복잡도O(n²) 속도가 느린 편
- 간단하게 구현 가능

#### 정렬 과정
1. 비교 연산이 필요한 루프 범위를 설정
2. 인접한 데이터 값을 비교
3. swap 조건에 부합하면 swap 연산을 수행
4. 루프 범위가 끝날 떄 까지 2 ~ 3번을 반복
5. 정렬 영역을 설정한다. 다음 루프를 실행할 때는 이 영역을 제외한다
6. 비교 대상이 없을 때까지 1~5번을 반복
- swap이 한 번도 발생하지 않았다면 그 영역 뒤에 있는 데이터가 모두 정렬됬다는 뜻
```python
# 백준 - 2750번
import sys
input = sys.stdin.readline

n = int(input())
a = [0] * n

for i in range(n):
    a[i] = int(input())

for i in range(n - 1):
    for j in range(n - 1 - i):
        if a[j] > a[j + 1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp

for i in range(n):
    print(a[i])
```
```python

```
```python

```
```python

```
```python

```
```python

```
```python

```
```python

```
```python

```
# Programmers
> [코딩테스트 연습 | 프로그래머스 스쿨 (programmers.co.kr)](https://school.programmers.co.kr/learn/challenges?tab=all_challenges)
```python
# 두 개 뽑아서 더하기
def solution(numbers):
    answer = set()
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.add(numbers[i] + numbers[j])
    answer = list(answer)
    answer.sort()
    return answer
---
def solution(numbers):
    answer = []
    for i in range(len(numbers)-1):
        for j in range(i+1,len(numbers)):
            answer.append(numbers[i]+numbers[j])
    answer=list(set(answer))
    answer.sort()
    return answer
```
```python
# 음양 더하기
# 정수들의 절댓값을 차례대로 담은 정수 배열 absolutes와 이 정수들의 부호를 차례대로 담은 불리언 배열 signs가 매개변수로 주어집니다. 실제 정수들의 합을 구하여 return 하도록 solution 함수를 완성
# gns의 길이는 absolutes의 길이와 같습니다.
    #signs[i] 가 참이면 absolutes[i]의 실제 정수가 양수임을, 그렇지 않으면 음수임을 의미
    # 음양 더하기
def solution(absolutes, signs):
    # signs가 참이면 해당 absolutes의 수가 양수, 거짓이면 음수
    # 주어진 수를 하나씩 접근
    # 양수, 음수가 적용된 실제 합
    answer = 0
    for i in range(len(signs)):
    # 참인경우 양수이므로 더하기
        if signs[i]:
            answer += absolutes[i]
            # 거짓인 경우 음수이므로 빼기
        else:
            answer -= absolutes[i]
    return answer
---
def solution(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))
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
```python

```

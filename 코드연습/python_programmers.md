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
# 완주하지 못한 선수
# 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주
# 참여자의 이름이 담긴 배열 participant
# 완주한 선수들의 이름이 담긴 배열 completion
# 완주하지 못한 선수의 이름을 return 하도록 solution 함수
# completion의 길이는 participant의 길이보다 1 작습니다.
# 참가자 중에는 동명이인이 있을 수 있습니다.
def solution(participant, completion):
    
    dic = {}
    for i in participant:   # participant키를 순회
        if i in dic.keys(): #key에 i가 있다면 +1 을 함
            dic[i] += 1
        else:               # 초면이다? 그럼 넌 1이야
            dic[i] = 1

    for i in completion:     # completion키를 돌아봐
        if i in dic.keys():  # 키를 돌고나서 이름 또 있다? 그럼 - 해
            dic[i] -= 1
            
    for key ,value in dic.items():  # 그러면 남은 녀석들? 완주를 못했구나
        if value == 1:              # 그럼 너는 1이야

            return key             # 범인 발견
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

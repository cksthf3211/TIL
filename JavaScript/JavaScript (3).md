# JavaScript
## 함수
### 함수의 정의
- 함수의 이름과 함께 정의하는 방식
- 3가지 부분으로 구성
    - 함수의 이름 (name)
    - 매개변수 (args)
    - 함수 body (중괄호 내부)
```javascript
function name(args) {
    // do something
}
```
```javascript
function name(num1 + num2) {
    return num1 + num2
}
add(1,2)
```
### 기본 인자(default arguments)
- 인자 작성 시 ‘=’ 문자 뒤 기본 인자 선언 가능
```javascript
const greeting = function (name = 'Anonymous') {
    return `Hi ${name}`
}
greeting() // Hi Anonymous
```
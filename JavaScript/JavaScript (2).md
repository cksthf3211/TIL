# JavaScript
## 변수와 식별자
- 식별자(identifier)는 변수를 구분할 수 있는 변수명
- 식별자는 반드시 문자, 달러($) 또는 밑줄(_)로 시작
- 대소문자를 구분하며, 클래스명 외에는 모두 소문자로 시작
- 예약어* 사용 불가능
    - for, if, function 등 불가능

### 선언 (Declaration)
- 변수를 생성하는 행위 또는 시점

### 할당 (Assignment)
- 선언된 변수에 값을 저장하는 행위 또는 시점

### 초기화 (Initialization)
- 선언된 변수에 처음으로 값을 저장하는 행위 또는 시점

```javascript
let foo            // 선언
console.log(foo)   // undefined

foo == 11          // 할당
console.log(foo)   // 11

let bar = 0        // 선언 + 할당
console.log(bar)   // 0
```

### let, const
#### let
```javascript
let number = 10     // 선언 및 초기값 할당
number = 10         // 재할당
console.log(number) // 10
```
```javascript
let number = 10     // 선언 및 초기값 할당
let number = 50     // 재선언 불가능
```

#### const
```javascript
const number = 10 // 선언 및 초기값 할당
number = 10       // 재할당 불가능
```
```javascript
const number = 10 // 선언 및 초기값 할당
const number = 50 // 재선언 불가능
```

#### 블록 스코프 (block scope)
-  if, for, 함수 등의 중괄호 내부를 가리킴
- 블록 스코프를 가지는 변수는 블록 바깥에서 접근 불가능
```javascript
let x = 1
if (x === 1){
    let x = 2
    console.log(x)  // 2
}
console.log(x) // 1
```
### var
- var로 선언한 변수는 재선언 및 재할당 모두 가능
- ES6 이전에 변수를 선언할 때 사용되던 키워드
- 호이스팅되는 특성으로 인해 예기치 못한 문제 발생 가능
    - 따라서 ES6 이후부터는 var 대신 const와 let을 사용하는 것을 권장
- 함수 스코프
```javascript
var number = 10  // 선언 및 초기값 할당
var number = 50  // 재할당
console.log(number) // 50
```
#### 함수 스코프* (function scope)
- 함수의 중괄호 내부를 가리킴
- 함수 스코프를 가지는 변수는 함수 바깥에서 접근 불가능
```javascript
function foo() {
  var x = 5
  console.log(x)  // 5
}

// ReferenceError: x is not defined
console.log(x)
```
### 호이스팅
- 변수를 선언 이전에 참조할 수 있는 현상
- 변수 선언 이전의 위치에서 접근 시 undefined를 반환
- 자바스크립트는 모든 선언을 호이스팅한다.
- 즉, var, let, const 모두 호이스팅이 발생하지만, var는 선언과 초기화가 동시에 발생하여 일시적 사각지대가 존재하지 않는다.

## 데이터 타입
- 자바스크립트의 모든 값은 특정한 데이터 타입을 가짐
- 크게 원시 타입* (Primitive type)과 참조 타입* (Reference type)으로 분류됨

### 원시 타입 (Primitive type)
- 객체 (object)가 아닌 기본 타입
- 변수에 해당 타입의 값이 담김
- 다른 변수에 복사할 때 실제 값이 복사됨
```javascript
let message = '안녕하세요' // message 선언 및 할당
let greeting = message     // greeting에 message 복사
console.log(greeting)      // 안녕하세요 출력

message = 'Hello, World'   // message 재할당
console.log(greeting)      // 안녕하세요 출력
```

### 참조 타입 (Reference type)
- 객체 (object) 타입의 자료형
- 변수에 해당 객체의 참조 값이 담김
- 다른 변수에 복사할 때 참조 값이 복사됨
```javascript
const message = ['안녕하세요'] // message 선언 및 할당
const greeting = message       // greeting에 message 복사
console.log(greeting)          // ['안녕하세요'] 출력

message[0] = 'Hello, World'    // message 재할당
console.log(greeting)          // ['Hello, World'] 출력
```

### 문자열 (String) 타입
- 텍스트 데이터를 나타내는 타입
- 16비트 유니코드 문자의 집합
- 작은따옴표 또는 큰따옴표 모두 가능
- 템플릿 리터럴 (Template Literal)
    - ES6부터 지원
    - 따옴표 대신 backtick(` `)으로 표현
    - ${ expression } 형태로 표현식 삽입 가능
```javascript
const firstName = '박'
const lastName = '찬솔'
const firstName = '${firstName} ${lastName}'

console.log(fullName) // 박 찬솔
```

### Boolean 타입
- 논리적 참 또는 거짓을 나타내는 타입
- true 또는 false로 표현
- 조건문 또는 반복문에서 유용하게 사용
    - **(참고) 조건문 또는 반복문에서 boolean이 아닌 데이터 타입은 자동 형변환 규칙에 따라 true 또는 false로 변환됨**
```javascript
let isAdmin = true
console.log(isAdmin) // true

isAdmin = false
console.log(isAdmin) // false
```

### 동등 비교 연산자 (==)
- 두 피연산자가 같은 값으로 평가되는지 비교 후 boolean 값을 반환
- 비교할 때 암묵적 타입 변환을 통해 타입을 일치시킨 후 같은 값인지 비교
- 두 피연산자가 모두 객체일 경우 메모리의 같은 객체를 바라보는지 판별
- 예상치 못한 결과가 발생할 수 있으므로 특별한 경우를 제외하고 사용하지 않음
```javascript
const a = 1004
const b = '1004'
console.log(a == b) // true

const c = 1
const d = true
console.log(c == d) // true

console.log(a + b) // 10041004
console.log(c + d) // 2
```

### 일치 비교 연산자 (===)
- 두 피연산자가 같은 값으로 평가되는지 비교 후 boolean 값을 반환
- 엄격한 비교가 이뤄지며 암묵적 타입 변환이 발생하지 않음
    - 엄격한 비교: 두 비교 대상의 타입과 값 모두 같은지 비교
```javascript
const a = 1004
const b = '1004'
console.log(a === b) // false

const c = 1
const d = true
console.log(c == d) // false

console.log(c + d) // false
```

## 조건문
### 조건문의 종류와 특징
- **‘if’** statement
    - 조건 표현식의 결과값을 Boolean 타입으로 변환 후 참/거짓을 판단
- **‘switch’** statement
    - 조건 표현식의 결과값이 어느 값(case)에 해당하는지 판별
    - (참고*) 주로 특정 변수의 값에 따라 조건을 분기할 때 활용
    - 조건이 많아질 경우 if문보다 가독성이 나을 수 있음
- **if, else if, else**
    - 조건은 소괄호(condition) 안에 작성
    - 실행할 코드는 중괄호{} 안에 작성
    - 블록 스코프 생성

#### if statement
```javascript
if (condition) {
  // do something
} else if (condition) {
  // do something
} else {
  // do something
}
```
```javascript
const nation = 'Korea'

if (nation === 'Korea'){
    console.log('안녕하세요')
} else if (nation === 'France'){
    console.log('Bonjur')
} else{
    console.log('Hello')
}
```
#### switch statement
- 표현식(expression)의 결과값을 이용한 조건문
- 표현식의 결과값과 case문의 오른쪽 값을 비교
- break 및 default문은 [선택적]으로 사용 가능
- break문을 만나거나 default문을 실행할 때까지 다음 조건문 실행
```javascript
switch(expression){
    case 'first value': {
        // do something
        [break]
    }
    case 'second value': {
        // do something
        [break]
    }
    [default:{
        // do something
     }]
}
```
```javascript
switch(nation){
    case 'Korea': {
        console.log('안녕하세요')
    }
    case 'France': {
        console.log('Bonjour')
    }
    default:{
        console.log('Hello')
     }
}
```
#### if와 switch
```javascript
const numOne= 5
const numTwo= 10
let operator = '+'

if (operator === '+') {
    console.log(numOne + numTwo)
} else if (operator === '-') {
    console.log(numOne - numTwo)
} else if (operator === '*') {
    console.log(numOne * numTwo)
} else if (operator === '/') {
    console.log(numOne / numTwo)
} else {
    console.log('유효하지 않은 연산자입니다.')
}
```
```javascript
const numOne= 5
const numTwo= 10
let operator = '+'

switch(operator) {
    case '+': {
        console.log(numOne + numTwo)
        break
    }
    case '-': {
        console.log(numOne - numTwo)
        break
    }
    case '*': {
        console.log(numOne * numTwo)
        break
    }
    case '/': {
        console.log(numOne / numTwo)
        break
    }
    default:{
        console.log('유효하지 않은 연산자입니다.')
    }
}
```
## 반복문
### 반복문의 종류와 특징
- while
- for
- for...in
    - 주로 객체(object)의 속성들을 순회할 때 사용
    - 배열도 순회 가능하지만 인덱스 순으로 순회한다는 보장이 없으므로 권장하지 않음
- for...of
    - 반복 가능한(iterable)* 객체를 순회하며 값을 꺼낼 때 사용
        - 반복 가능한(iterable) 객체*의 종류: Array, Map, Set, String 등

#### while
- 조건문이 참(true)인 동안 반복 시행
- 조건은 소괄호 안에 작성
- 실행할 코드는 중괄호 안에 작성
- 블록 스코프 생성

```javascript
let i = 0

while (i < 6) {
    console.log(i)
    i += 1
}
```

#### for
- 세미콜론(;)으로 구분되는 세 부분 으로 구성
- initialization
    - 최초 반복문 진입 시 1회만 실행되는 부분
- condition
    - 매 반복 시행 전 평가되는 부분
- expression
    - 매 반복 시행 이후 평가되는 부분
- 블록 스코프 생성
```javascript
for (initialization; condition; expression) {
    // do something
}
```
```javascript
for (let i = 0; i < 6; i++) {
    console.log(i)  // 0, 1, 2, 3, 4, 5
}
```
```javascript
// 반복문 진입 및 변수 i 선언
for (let i = 0;
```
```javascript
// 조건문 평가 후 코드 블럭 실행
                 i < 6;
    console.log(i)  // 0
}
```
```javascript
// 코드 블록 실행 이후 i 값 증가
for (                    i++) {
}
```

#### for...in (객체 순회 적합)
- 객체(object)의 속성(key)들을 순회할 때 사용
- 배열도 순회 가능하지만 권장하지 않음
- 실행할 코드는 중괄호 안에 작성
- 블록 스코프 생성
```javascript
for (variable in object) {
    // do something
}
```
```javascript
// object(객체) => key-value로 이루어진 자료구조 (객체 챕터에서 학습 예정)
const capitals = {
    korea: 'seoul' ,
    france: 'paris' ,
    USA: 'washington D.C.'
}

for (let capital in capitas) {
    console.log(capital) // korea, france, USA
}
```

#### for...of (배열 순회 적합)
- 반복 가능한(iterable) 객체를 순회하며 값을 꺼낼 때 사용
- 실행할 코드는 중괄호 안에 작성
- 블록 스코프 생성
```javascript
for (variable of object) {
    // do something
}
```
```javascript
const fruits = [
    '딸기' ,
    '바나나' ,
    '메론'
]
for (let fruit of fruits) {
    console.log(fruit) // 딸기, 바나나, 메론
}
```
```javascript
const fruits = [
    '딸기' ,
    '바나나' ,
    '메론'
]
for (let fruit in fruits) {
    console.log(fruit) // 0, 1, 2
}
```

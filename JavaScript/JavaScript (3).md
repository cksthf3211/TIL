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

-매개변수보다 인자의 개수가 많을 경우,
```javascript
const noArgs = function () {
    return 0
}
noArgs(1, 2, 3) // 0
const twoArgs = function (arg1, arg2) {
    return [arg1, arg2]
}
twoArgs(1, 2, 3) // [1, 2]
```

- 매개변수보다 인자의 개수가 적을 경우,
```javascript
const threeArgs = function (arg1, arg2, arg3) {
    return [arg1, arg2, arg3]
}
threeArgs() // [undefined, undefined, undefined]
threeArgs(1) // [1, undefined, undefined]
threeArgs(1, 2) // [1, 2, undefined]
```

### 함수의 타입
-  선언식 함수와 표현식 함수 모두 타입은 function으로 동일
```javascript
// 함수 표현식
const add = function(args) { }

// 함수 선언식
function sub(args) { }

console.log(typeof add) // function
console.log(typeof sub) // function
```

#### 호이스팅(hoisting) – 함수 선언식
- 함수 선언식으로 선언한 함수는 var로 정의한 변수처럼 hoisting 발생
- 함수 호출 이후에 선언 해도 동작
```javascript
add(2, 7) //9
function add (num1, num2) {
    return num1 + num2
}
```

#### 호이스팅(hoisting) - 함수 표현식
- 반면 함수 표현식으로 선언한 함수는 함수 정의 전에 호출 시 에러 발생
- 함수 표현식으로 정의된 함수는 변수로 평가되어 변수의 scope 규칙을 따름
```javascript
sub(7, 2) // ReferenceError

const sub = function(num1, num2) {
    return num1 - num2
}
```

## 화살표 함수 (Arrow Function)
- 함수를 비교적 간결하게 정의할 수 있는 문법
- function 키워드 생략 가능
- 함수의 매개변수가 단 하나 뿐이라면, ‘( )’ 도 생략 가능
- 함수 몸통이 표현식 하나라면 ‘{ }’과 return도 생략 가능
- 기존 function 키워드 사용 방식과의 차이점은 후반부 this 키워드를 학습하고 다시 설명
```javascript
const arrow1 = function (name) {
    return `hello, ${name}` 
}

// 1. function 키워드 삭제 
const arrow2 = (name) => {
    return `hello, ${name}`
}

// 2. 매개변수가 1개일 경우에만 ( ) 생략 가능
const arrow3 = name => {
    return `hello, ${name}` 
}

// 3. 함수 바디가 return을 포함한 표현식 1개일 경우에 { } & return 삭제 가능
const arrow4 = name => `hello, ${name}`
```

## 문자열 (String)
### 문자열 관련 주요 메서드 – includes
- string.includes(value)
    - 문자열에 value가 존재하는지 판별 후 참 또는 거짓 반환
```javascript
const str = 'a santa at nasa'

str.includes('santa') // true
str.includes('asan')  // false
```

### 문자열 관련 주요 메서드 - split
- string.split(value)
    - value가 없을 경우, 기존 문자열을 배열에 담아 반환
    - value가 빈 문자열일 경우 각 문자로 나눈 배열을 반환
    - value가 기타 문자열일 경우, 해당 문자열로 나눈 배열을 반환
```javascript
const str = 'a cup'

str.split()     // ['a cup']
str.split('')   // ['a', ' ', 'c', 'u', 'p']
str.split(' ')  // ['a', 'cup']
```

### 문자열 관련 주요 메서드 – replace
- string.replace(from, to)
    -  문자열에 from 값이 존재할 경우, 1개만 to 값으로 교체하여 반환

- string.replaceAll(from, to)
    - 문자열에 from 값이 존재할 경우, 모두 to 값으로 교체하여 반환
```javascript
const str = 'a b c d'

str.replace(' ', '-')    // 'a-b c d'
str.replaceAll(' '. '-') // 'a-b-c-d'
```

### 문자열 관련 주요 메서드 – trim
- string.trim()
    - 문자열 시작과 끝의 모든 공백문자(스페이스, 탭, 엔터 등)를 제거한 문자열 반환

- string.trimStart()
    - 문자열 시작의 공백문자(스페이스, 탭, 엔터 등)를 제거한 문자열 반환

- string.trimEnd()
    - 문자열 끝의 공백문자(스페이스, 탭, 엔터 등)를 제거한 문자열 반환
```javascript
const str = '   hello   '

str.trim()     // 'hello'
str.trimStart  // 'hello    '
str.trimEnd    // '    hello'
```

## 배열 (Arrays)
- 키와 속성들을 담고 있는 참조 타입의 객체(object)
- 순서를 보장하는 특징이 있음
- 주로 대괄호를 이용하여 생성하고, 0을 포함한 양의 정수 인덱스로 특정 값에 접근 가능
- 배열의 길이는 array.length 형태로 접근 가능
    - 배열의 마지막 원소는 array.length – 1로 접근
```javascript
const numbers = [1, 2, 3, 4, 5]

console.log(numbers[0])    // 1
console.log(numbers[-1])   // undefined
console.log(numbers.length)// 5
```
```javascript
const numbers = [1, 2, 3, 4, 5]

console.log(numbers[numbers.length - 1]) // 5
console.log(numbers[numbers.length - 2]) // 4
console.log(numbers[numbers.length - 3]) // 3
console.log(numbers[numbers.length - 4]) // 2
console.log(numbers[numbers.length - 5]) // 1
```

### 배열 관련 주요 메서드 - reverse
- array.reverse()
    - 원본 배열의 요소들의 순서를 반대로 정렬
```javascript
const numbers = [1, 2, 3, 4, 5]
numbers.reverse()
console.log(numbers) // [5, 4, 3, 2, 1]
```

### 배열 관련 주요 메서드 – push & pop
- array.push()
    - 배열의 가장 뒤에 요소 추가

- array.pop()
    - 배열의 마지막 요소 제거
```javascript
const numbers = [1, 2, 3, 4, 5]

numbers.push(100)
console.log(numbers) // [1, 2, 3, 4, 5, 100]

numbers.pop()
console.log(numbers) // [1, 2, 3, 4, 5]
```

### 배열 관련 주요 메서드 – unshift & shift
- array.unshift()
    - 배열의 가장 앞에 요소 추가
- array.shift()
    - 배열의 첫번째 요소 제거
```javascript
const numbers = [1, 2, 3, 4, 5]

numbers.unshift(100)
console.log(numbers) // [100, 1, 2, 3, 4, 5]

numbers.shift()
console.log(numbers) // [1, 2, 3, 4, 5]
```

### 배열 관련 주요 메서드 – includes
- array.includes(value)
    - 배열에 특정 값이 존재하는지 판별 후 참 또는 거짓 반환
```javascript
const numbers = [1, 2, 3, 4, 5]

console.log(numbers.includes(1))   // true 
console.log(numbers.includes(100)) // false
```

### 배열 관련 주요 메서드 – indexOf
- array.indexOf(value)
    - 배열에 특정 값이 존재하는지 확인 후 가장 첫 번째로 찾은 요소의 인덱스 반환
    - 만약 해당 값이 없을 경우 -1 반환
```javascript
const numbers = [1, 2, 3, 4, 5]
let result

result = numbers.indexOf(3)  // 2  요소의 인덱스 반환
console.log(result) 

result = numbers.indexOf(100) // -1   해당 값이 없음
console.log(result)
```

### 배열 관련 주요 메서드 – join
- array.join([separator])
    - 배열의 모든 요소를 연결하여 반환
    - separator(구분자)는 선택적으로 지정 가능
    - 생략 시 쉼표를 기본 값으로 사용
```javascript
const numbers = [1, 2, 3, 4, 5]
let result

result = numbers.join()  // 1, 2, 3, 4, 5
console.log(result) 

result = numbers.join('')  // 12345
console.log(result) 

result = numbers.join(' ')  // 1 2 3 4 5
console.log(result) 

result = numbers.join('-')  // 1-2-3-4-5
console.log(result) 
```

### Spread operator
- spread operator(…)를 사용하면 배열 내부에서 배열 전개 가능
    - ES5까지는 Array.concat() 메서드를 사용.
- 얕은 복사에 활용 가능
```javascript
const array = [1, 2, 3]
const newArray = [0, ...array, 4]

console.log(newArray)  // [0, 1, 2, 3, 4]
```

## 배열 심화편
- 배열을 순회하며 특정 로직을 수행하는 메서드

### 배열 관련 주요 메서드 – forEach
- array.forEach(callback(element[, index[,array]]))
- 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
- 콜백 함수는 3가지 매개변수로 구성
    - element: 배열의 요소
    - index: 배열 요소의 인덱스
    - array: 배열 자체
- 반환 값(return)이 없는 메서드
```javascript
array.forEach((element, index, array) => {
    // do something
})
```
```javascript
const fruits = ['딸기', '수박', '사과', '체리']

fruits.forEach((fruits.index) => {
    console.log(fruits, index)
    // 딸기 0
    // 수박 1
    // 사과 2
    // 체리 3
})
```

### 배열 관련 주요 메서드 – map
- **array.map(callback(element[, index[, array]]))**
- 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
- 콜백 함수의 반환 값을 요소로 하는 새로운 배열 반환
- 기존 배열 전체를 다른 형태로 바꿀 때 유용
```javascript
array.map((element, index, array) => {
    // do something
})
```
```javascript
const numbers = [1, 2, 3, 4, 5]

const doubleNums = numbers.map((num) => {
    return num * 2
})
console.log(doubleNums)  // [2, 4, 6, 8, 10]
```

### 배열 관련 주요 메서드 – filter
- **array.filter(callback(element[, index[, array]]))**
- 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
- 콜백 함수의 반환 값이 참인 요소들만 모아서 새로운 배열을 반환
- 기존 배열의 요소들을 필터링할 때 유용
```javascript
array.filter((element, index, array) => {
    // do something
})
```
```javascript
const numbers = [1, 2, 3, 4, 5]

const oddNums = numbers.filter((num, index) => {
    return num % 2
})
console.log(oddNums)  // 1, 3, 5
```

### 배열 관련 주요 메서드 – reduce
- **array.reduce(callback(acc, element, [index[, array]])[, initialValue])**
- 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
- 콜백 함수의 반환 값들을 하나의 값(acc)에 누적 후 반환
- reduce 메서드의 주요 매개변수
    - acc
        - 이전 callback 함수의 반환 값이 누적되는 변수
    - initialValue(optional)
        - 최초 callback 함수 호출 시 acc에 할당되는 값, default 값은 배열의 첫 번째 값
- (참고) 빈 배열의 경우 initialValue를 제공하지 않으면 에러 발생
```javascript
array.reduce((element, index, array) => {
    // do something
}), initialValue
```
```javascript
const numbers = [1, 2, 3]

const result = numbers.reduce((acc, num) => {
    return acc + num
})
console.log(result)  // 6
```

### 배열 관련 주요 메서드 – find'
- array.find(callback(element[, index[, array]]))
    - 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
    - 콜백 함수의 반환 값이 참이면, 조건을 만족하는 첫번째 요소를 반환
    - 찾는 값이 배열에 없으면 undefined 반환
```javascript
array.find((element, index, array)) {
    // do something 
}
```
```javascript
const avengers = [
    {name: 'Tony Stark', age: 45},
    {name: 'Steve Rogers', age: 32},
    {name: 'Thor', age: 40},
]

const result = avengers.find((avenger) =>{
    return avenger.name === 'Tony Stark'
})
console.log(result)   // {name: 'Tony Stark', age: 45}
```

### 배열 관련 주요 메서드 – some
- array.some(callback(element[, index[, array]]))
    - 배열의 요소 중 하나라도 주어진 판별 함수를 통과하면 참을 반환
    - 모든 요소가 통과하지 못하면 거짓 반환
    - (참고) 빈 배열은 항상 거짓 반환
```javascript
array.some((element, index, array)) {
    // do something 
}
```
```javascript
const numbers = [1, 3, 5, 7, 9]

const hasEvenNumber = numbers.some((num) => {
    return num % 2 === 0
})
console.log(hasEvenNumber)   // false

const hasOddNumber = numbers.some((num) => {
    return num % 2
})
console.log(hasOddNumber)    // true
```

### 배열 관련 주요 메서드 – every
- array.every(callback(element[, index[, array]]))
    - 배열의 모든 요소가 주어진 판별 함수를 통과하면 참을 반환
    - 하나의 요소라도 통과하지 못하면 거짓 반환
    - (참고) 빈 배열은 항상 참 반환
```javascript
array.every((element, index, array)) {
    // do something 
}
```
```javascript
const numbers = [2, 4, 6, 8, 10]

const isEveryNumberEven = numbers.some((num) => {
    return num % 2 === 0
})
console.log(isEveryNumberEven)   // false

const isEveryNumberOdd = numbers.some((num) => {
    return num % 2
})
console.log(isEveryNumberOdd)    // true
```

## 객체 (Objects)
- 객체는 속성(property)의 집합이며, 중괄호 내부에 key와 value의 쌍으로 표현
-  key는 문자열 타입만 가능
    - (참고) key 이름에 띄어쓰기 등의 구분자가 있으면 따옴표로 묶어서 표현
- value는 모든 타입(함수포함) 가능
- 객체 요소 접근은 점 또는 대괄호로 가능
    - (참고) key 이름에 띄어쓰기 같은 구분자가 있으면 대괄호 접근만 가능
```javascript
const me = {
    name: 'jack',
    phoneNumber: '01012345678',
    'samsung products': {
        buds: 'Galaxy Buds pro',
        galaxy: 'Galaxy s20’,
    }, 
}

console.log(me.name)
console.log(me.phoneNumber)
console.log(me['samsung products'])
console.log(me['samsung products'].buds)
```

- 메서드는 객체의 속성이 참조하는 함수
- 객체.메서드명() 으로 호출 가능
- 메서드 내부에서는 this 키워드가 객체를 의미함
```javascript
const me = {
    firstName: 'John',
    lastName: 'Doe’ ,
    getFullName: function () {
        return this.firstName + this.lastName 
    }
}
```
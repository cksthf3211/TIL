# 객체 지향 설계의 5대 원리 - SOLID
- SRP ( 단일책임의 원칙 : Single Responsibility Principle )
- OCP( 개방 폐쇄 원칙 : Open Closed Priciple )
- LSP( 리스코프 치환 원칙 : Listov Substitution Priciple )
- ISP( 인터페이스 분리 원칙 : Interface Segregation Principle )
- DIP( 의존 역전 원칙 : Dependency Inversion Principle )

## SRP ( 단일책임의 원칙 : Single Responsibility Principle )
- 모든 클래스는 각각 하나의 책임만 가져야 한다.
- 클래스는 그 책임을 완전히 캡슐화해야 함을 말한다.
    1. 사칙연산 함수를 가지고 있는 계산 클래스가 있다고 치자.
    2. 이 상태의 계산 클래스는 오직 사칙연산 기능만을 책임진다.
    3. 이 클래스를 수정한다고 한다면 그 이유는 사직연산 함수와 관련된 문제일 뿐
    4. 유지 보수가 잘 됨

## OCP( 개방 폐쇄 원칙 : Open Closed Priciple )
- 확장에는 열려있고 수정에는 닫혀있는
- 기존의 코드를 변경하지 않으면서( Closed), 기능을 추가할 수 있도록(Open) 설계가 되어야 한다는 원칙
    1. 캐릭터를 하나 생성한다고 할때,
    2. 각각의 캐릭터가 움직임이 다를 경우 움직임의 패턴 구현을 하위 클래스에 맡긴다면
    3. 캐릭터 클래스의 수정은 필요가없고(Closed) 움직임의 패턴만 재정의 하면 된다.(Open)

## LSP( 리스코프 치환 원칙 : Listov Substitution Priciple )
- 자식 클래스는 언제나 자신의 부모 클래스를 대체할 수 있다는 원칙
- 즉 부모 클래스가 들어갈 자리에 자식 클래스를 넣어도 계획대로 잘 작동해야 한다.

    1. 자식클래스는 부모 클래스의 책임을 무시하거나 재정의하지 않고 확장만 수행하도록 해야 LSP를 만족

## ISP( 인터페이스 분리 원칙 : Interface Segregation Principle )
- 한 클래스는 자신이 사용하지않는 인터페이스는 구현하지 말아야 한다.
- 하나의 일반적인 인터페이스보다 여러개의 구체적인 인터페이스가 낫다.

## DIP( 의존 역전 원칙 : Dependency Inversion Principle )
- 의존 관계를 맺을 때 변화하기 쉬운 것 또는 자주 변화하는 것보다는 변화하기 어려운 것, 거의 변화가 없는 것에 의존하라는 것
- 한마디로 구체적인 클래스보다 인터페이스나 추상 클래스와 관계를 맺으라는 것
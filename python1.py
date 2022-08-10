def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)
while True:
    n = input('\n팩토리얼 구할 숫자는??')
    if n.isnumeric():
        res = factorial(int(n))
        print(res)
    else:
        print('종료합니다.')
        break
import sys
from collections import deque

sys.stdin = open('input (1).txt')

Testcase = 10
for _ in range(Testcase):
    test = int(input())
    numbers = deque(map(int, input().split()))
    minus = 0
    while 1:
        if (minus % 5 + 1) < numbers[0]:
            numbers.append(numbers.popleft() - (minus % 5 + 1))
            minus += 1
        else:
            numbers.popleft()
            numbers.append(0)
            break
    print(f'#{test}', *numbers)

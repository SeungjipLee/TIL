import sys

sys.stdin = open('sample_input (4).txt')

Testcase = int(input())
for test in range(Testcase):
    N, R = map(int, input().split())
    numbers = list(map(int, input().split()))
    print(f'#{test + 1}', numbers[R % N])

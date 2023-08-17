import sys
sys.stdin = open('a.txt')

Testcase = int(input())
for test in range(1, Testcase+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    print(f'#{test}', max(numbers) - min(numbers))
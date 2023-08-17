import sys
sys.stdin = open('a.txt')

Testcase = int(input())
for test in range(1, Testcase+1):
    N, M = map(int, input().split())
    numbers = list(range(1, N+1))
    do_stu = list(map(int, input().split()))
    for i in do_stu:
        numbers.remove(i)
    print(f'#{test}', *numbers)
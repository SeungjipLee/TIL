import sys
sys.stdin = open('a.txt')

Testcase = int(input())
for test in range(1, Testcase+1):
    N = int(input())
    numbers = list(map(int, input()))
    numbers.sort()
    final2 = 0
    fianl1 = 0
    for i in numbers:
        if final2 <= numbers.count(i):
            final2 = numbers.count(i)
            final1 = i

    print(f'#{test}', final1, final2)
import sys
sys.stdin = open("input.txt")

Testcase = int(input())

for test in range(Testcase):
    N, M = map(int, input().split())
    List = list(map(int, input().split()))
    max_sum = 0
    min_sum = 100*10000

    for i in range(N-M+1):
        mid_sum = List[i]
        for k in range(1, M):
            mid_sum += List[i+k]


        if mid_sum >= max_sum:
            max_sum = mid_sum
        if mid_sum <= min_sum:
            min_sum = mid_sum
    div = max_sum - min_sum
    print(f'#{test+1} {div}')
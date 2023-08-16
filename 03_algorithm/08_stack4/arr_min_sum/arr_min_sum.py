import sys
from itertools import permutations
sys.stdin = open('sample_input (2).txt')


Testcase = int(input())
for test in range(Testcase):
    N = int(input())
    Board = [list(map(int, input().split())) for _ in range(N)]
    arr = list(range(N))
    final = 10 * N
    # arr이라는 배열중 N개를 택하여 나열하는 경우의 수
    for i in permutations(arr, N):
        mid = 0
        for j in range(len(i)):
            mid += Board[j][i[j]]
            if mid > final:
                break
        if mid <= final:
            final = mid
        else:
            continue


    print(f'#{test+1}', final)
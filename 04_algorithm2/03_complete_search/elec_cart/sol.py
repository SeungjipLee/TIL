import sys
sys.stdin = open('a.txt')
from itertools import permutations

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    Board = [list(map(int, input().split())) for _ in range(N)]
    final = []
    for i in permutations(range(2, N+1), N-1):
        A = list(i)
        A.append(1)
        A.insert(0, 1)
        mid = 0
        for j in range(len(A)):
            A[j] -= 1
        for k in range(len(A)-1):
            mid += Board[A[k]][A[k+1]]
        final.append(mid)
    print(f'#{tc}', min(final))
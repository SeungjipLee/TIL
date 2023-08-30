import sys
sys.stdin = open('a.txt')
from itertools import combinations
from copy import deepcopy


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    B = [i for i in str(N)]
    compare = []
    while M != 0:
        for i in combinations(range(len(B)), 2):
            A = deepcopy(B)
            A[i[0]], A[i[1]] = A[i[1]], A[i[0]]
            mid = ''.join(A)
            compare.append(int(mid))
        M -= 1
    print(compare)
    print(f'#{tc}', max(compare))
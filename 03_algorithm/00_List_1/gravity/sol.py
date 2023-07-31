import sys
sys.stdin = open("input.txt")

TC = int(input())
for i in range(TC):
    N = int(input())
    max_fall_gap = 0
    List = list(map(int, input().split()))

    for j in range(N): # N = 9 | 0 ~ 8
        max_H = N - (j + 1)
        for k in range(j+1, N):
            if List[j] <= List[k]:
                max_H -= 1
        if max_fall_gap <= max_H:
            max_fall_gap = max_H

    print(f'#{i+1} {max_fall_gap}')
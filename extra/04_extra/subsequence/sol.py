import sys
sys.stdin = open('a.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    numbers = list(map(int, input().split()))
    cnt = 0
    for i in range(1<<N):
        mid = 0
        for j in range(N):
            if i & (1<<j):
                mid += numbers[j]
            if mid > K:
                continue
        if mid == K:
            cnt += 1
    print(f'#{tc}', cnt)
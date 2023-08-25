import sys
sys.stdin = open('a.txt')

N = int(input()) # 스위치 개수
light = list(map(int, input().split()))
M = int(input()) # 사람 수
for _ in range(M):
    a, b = map(int, input().split())
    if a == 1:
        k = 1
        while k*b-1 < N:
            light[k*b-1] = (light[k*b-1]+1) % 2
            k += 1
    else:
        # 여자라면
        light[b-1] = (light[b-1]+1)%2
        i = 1
        while (0 <= b-1-i < N) and (0 <= b-1+i < N) and (light[b-1-i] == light[b-1+i]):
            light[b-1-i] = (light[b-1-i]+1)%2
            light[b-1+i] = (light[b-1+i]+1)%2
            i += 1
P = len(light)
for i in range(P//20 + 1):
    print(*light[20*i:20*(i+1)])
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
        if b == 1 or b == N:
            light[b-1] = (light[b-1]+1) % 2
        else:
            i = 1
            while b-1-i != -1:
                if light[b-1-i] != light[b-1+i]:
                    break
                i += 1
            for j in range(b-1-i, b+i):
                light[b] = (light[b]+1)%2
print(light)
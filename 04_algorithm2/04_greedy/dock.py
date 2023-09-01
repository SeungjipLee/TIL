import sys
sys.stdin = open('dock.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    Time = []
    for _ in range(N):
        a, b = map(int, input().split())
        Time.append([a, b])
    Time.sort(key=lambda x:x[1])
    print(Time)
    end_time = Time[0][0]
    final = 1
    for i in range(1, N):
        if end_time <= Time[i][0]:
            end_time = Time[i][1]
            final += 1
    print(f'#{tc}', final)
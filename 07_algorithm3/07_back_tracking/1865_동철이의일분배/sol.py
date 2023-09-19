def back(n, per):
    global max_per
    if n == N:
        max_per = max(max_per, per)
        return
    if per <= max_per:
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            back(n+1, per * employee[n][i] / 100)
            visited[i] = 0

T = int(input())
for t in range(T):
    N = int(input())
    employee = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    max_per = 0
    back(0,100)
    print(f'#{t+1} %.6f'%max_per)
def BFS(node):
    visited[node] = 1
    Q = [node]
    while Q:
        now = Q.pop(0)
        for next in adj[now]:
            if visited[next] == 0:
                Q.append(next)
                visited[next] = 1


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    adj = [[] for _ in range(N+1)]
    cnt = 0
    for i in range(M):
        a, b = nums[2*i], nums[2*i+1]
        adj[a].append(b)
        adj[b].append(a)
    visited = [0]*(N+1)
    for j in range(1, N+1):
        if visited[j] == 0:
            BFS(j)
            cnt += 1
    print(f'#{tc}', cnt)
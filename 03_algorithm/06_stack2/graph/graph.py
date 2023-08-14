import sys
sys.stdin = open('sample_input.txt')

# DFS : 1. 나의 경로를 기록할 stack 구현
#       2. 내가 다시 되돌아 올 때 중복된 길로 빠지지 않을 visited 구현
#       3. 행렬을 순회하며 내가 갈 수 있는 곳을 판단할 Logic 구현
#       4. 종료 조건은 더 이상 갈 곳이 없을 때(stack is empty)

def DFS(n):
    stack = [n]     # 출발점이 들어갈 것
    visited = [0] * (V+1)   # node의 개수+1 만큼 visited(0:안감 / 1:감)
    while stack:    # 스택이 빌 때까지 진행 할 것
        now = stack.pop()     # 출발점 설정
        if visited[now] == 0: # 출발점도 중복방지를 위해 방문표시
            visited[now] = 1
            Path.append(now)  # 현 위치 경로에 추가
            for next in range(V, 0, -1):  # 내가 갈 수 있는 애들 조사(행 조사)
                # 갈 수 있는 조건 : 연결되어 있으며, 방문표시 안 된 곳
                if matrix[now][next] == 1 and visited[next] == 0:
                    stack.append(next)  # stack에 추가


Testcase = int(input())
for test in range(Testcase):
    V, E = map(int, input().split())
    Data = []   # 연결 정보를 일렬 리스트로 받을 것
    Path = []   # 계속 기록될 경로
    for _ in range(E):
        a, b = map(int, input().split())
        Data.append(a)
        Data.append(b)

    S, G = map(int, input().split())

    matrix = [[0]*(V+1) for _ in range(V+1)]

    for i in range(E):
        ni = Data[2*i]
        nj = Data[2*i+1]
        matrix[ni][nj] = 1

    DFS(S)
    print(Path)

    if G in Path:
        print(f'#{test+1}', 1)
    else:
        print(f'#{test+1}', 0)
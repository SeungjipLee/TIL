import sys
sys.stdin = open('input (2).txt')

# DFS : 1. 나의 경로를 기록할 stack 구현
#       2. 내가 다시 되돌아 올 때 중복된 길로 빠지지 않을 visited 구현
#       3. 행렬을 순회하며 내가 갈 수 있는 곳을 판단할 Logic 구현
#       4. 종료 조건은 더 이상 갈 곳이 없을 때(stack : empty)
def DFS(n):
    stack = [n]     # 출발점을 스택에 두고
    visited = [0] * 100 # 방문 여부 체크( 0 : 방문 안함/ 1: 방문)
    visited[n] = 1      # 출발점도 체크
    while stack:        # 스택이 빌 때까지
        now = stack.pop()   # 현 위치 분석
        Path.append(now)    # 현 위치 경로에 추가
        for next in range(100): # 다음 위치 탐색
            # 갈 수 있는 조건 : 연결되어 있으며, 방문표시 안 된 곳
            if Matrix[now][next] == 1 and visited[next] == 0:
                stack.append(next)  # 스택에 다음 위치 추가

# Testcase 수를 입력받지 못해서 시도했으나 문제를 잘 보면 10회란다.
while True:
    try:
        # 테스트 케이스, 선 개수
        testcase, N = map(int, input().split())
        # 연결 정보리스트 / 0으로 채운 행렬(100*100)
        Data = list(map(int, input().split()))
        Matrix = [[0]*100 for _ in range(100)]
        # 내가 지나간 경로가 입력될 리스트
        Path = []
        # 시작과 목표는 고정
        S = 0
        G = 99
        # 100*100 인접 행렬에 연결 정보 입력
        for i in range(N):
            Matrix[Data[2*i]][Data[2*i+1]] = 1

        # 탐색
        DFS(S)

        # 경로에 목표가 있는지 확인
        if G in Path:
            print(f'#{testcase} 1')
        else:
            print(f'#{testcase} 0')

    except EOFError:
        break
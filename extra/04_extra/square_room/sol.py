import sys
sys.stdin = open('a.txt')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def search(x, y):
    idx = 0
    cnt = 1
    while idx < 4:
        nx = x + dx[idx]
        ny = y + dy[idx]
        if 0<=nx<N and 0<=ny<N and Board[x][y] == Board[nx][ny] - 1:
            x, y = nx, ny  # 이동 가능하면 내 현재 좌표를 바꿔치기
            cnt += 1
            idx = 0
        # 다음 방향 조사
        else:
            idx += 1
    return cnt


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    Board = [list(map(int, input().split())) for _ in range(N)]
    result = [] # 답안 기록용(모든 좌표에 대한, 방 번호와 이동횟수 기록)
    # 모든 좌표에 대해서 delta 탐색
    for i in range(N):
        for j in range(N):
            # 각 좌표, i, j 에 대해서
            # 방 번호, 누적한 이동 횟수
            # 모두 기록하고 난 다음에, 그 중에, 이동을 가장 많이한 경우
            result.append((Board[i][j], search(i, j)))
            # 조사를 통해 얻는 값은? (i, j)좌표에서 출발했을 때, 이동 횟수
    result.sort(key= lambda x:(x[1], -x[0]))
    print(f'#{tc}', *result[-1])
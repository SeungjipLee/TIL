from collections import deque
import sys

sys.stdin = open('input.txt')

# 델타 탐색(우 하 좌 상)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def BFS(S, G):  # S : 시작점 좌표 (1, 1), G : 도착점 좌표 (13, 13)
    final = 0  # 최종 결과값이 될 것 만약 도달 못하는 경우가 온다면 수정하지 않을 것
    visited = [[0] * 16 for _ in range(16)]  # 방문리스트 또한 미로판과 똑같은 사이즈로 제작
    Queue = deque()  # 큐 제작
    Queue.append(S)  # 큐에 출발점 넣기
    while Queue:  # 큐에 좌표가 남아있으면 반복
        now = Queue.popleft()  # 큐에서 가장 왼쪽의 것을 뽑아 현재 위치로 설정
        # Board[now[0]][now[1]] = 1   # 지나온 길을 벽으로 설정하는 것이나 사실 visited로 판단하기 때문에 불필요
        if visited[now[0]][now[1]] == 0:  # now의 형태가 좌표이므로 (1,2) 같은 상태로
            visited[now[0]][now[1]] = 1  # now[0]은 i좌표, now[1]은 j좌표
        for i in range(4):  # 델타 탐색을 진행
            ni = now[0] + dx[i]  # 델타 탐색을 진행한 새로운 i 좌표
            nj = now[1] + dy[i]  # 델타 탐색을 진행한 새로운 j 좌표
            if (ni, nj) == G:  # 만약 목적지에 도달했다면
                return final + 1  # 도착했으므로 1이 출력되도록 1을 더함
            # 목적지에 도달하지 못했다면 갈 수 있는 길이며 방문 횟수가 0이면 큐에 좌표를 추가
            elif (0 <= ni < 16) and (0 <= nj < 16) and (Board[ni][nj] == 0) and (visited[ni][nj] == 0):
                Queue.append((ni, nj))

    return final  # 찾으면 1 아니면 0


# 10번의 테스트 케이스
for _ in range(10):
    test = int(input())  # 테스트케이스 번호
    Board = [list(map(int, input())) for _ in range(16)]  # 미로 판 입력 받기
    S = G = 0  # 미리 변수 선언
    # 출발점과 도착점을 찾자
    for i in range(16):
        for j in range(16):
            if Board[i][j] == 2:
                S = (i, j)
            elif Board[i][j] == 3:
                G = (i, j)

    print(f'#{test}', BFS(S, G))

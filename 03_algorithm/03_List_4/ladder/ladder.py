dx = [0, 0, -1]     # 왼쪽(0) / 오른쪽(1) / 상승(-1)
dy = [-1, 1, 0]
Testcase = 10
for _ in range(Testcase):
    test = int(input())
    Board = [list(map(int,input().split())) for _ in range(100)]
    nx = 99
    ny = 0

    # 한칸 오르고 좌우에 있는지 확인하고 있으면 꺾는다
    # 좌회전시 우회전 이전까지는 직진
    # 우회전시 좌회전 이전까지는 직진
    # i 인덱스가 0에 도달한다면 그때의 j 인덱스가 정답
    # 필요한 조작 (왼쪽 한칸/ 오른쪽 한칸/ 위로 한 칸)
    # 현재위치에 대한 변수 필요
    # 결과는 현재위치 x==0 일때 y의 좌표 출력

    # 2가 적힌 위치를 찾는다(x index는 99로 고정, y 찾아야함)
    for i in range(100):
        if Board[99][i] == 2:
            ny = i

    # 사실 얼마나 걸리고 얼마나 동작할지 모르니 while문으로 작성(while x != 0:)
    while nx != 0:
        if (0 <= ny-1 < 100) and (ny-1 == 1):
            nx += dx[0]
            ny += dy[0]
import sys
sys.stdin = open("input.txt")

Testcase = int(input())
for i in range(Testcase):
    # 색칠 횟수 받기
    N = int(input())

    # 이후 등장할 집합 초기화.
    Red = set()
    Blue = set()

    # 좌표 2개와 색 입력 받기.
    for j in range(N):
        i1, j1, i2, j2, color = map(int, input().split())
        # 집합을 설정하고 좌표를 원소로 받자.
        if color == 1:
            for ii in range(i1, i2+1):
                for jj in range(j1, j2+1):
                    Red.add((ii,jj))
        else:
            for ii in range(i1, i2+1):
                for jj in range(j1, j2+1):
                    Blue.add((ii,jj))

    And_set = Red & Blue
    print(f'#{i+1} {len(And_set)}')
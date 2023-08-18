# 10518 개미(IM대비)
N, M = map(int, input().split())    # 가로 세로 길이
x, y = map(int, input().split())    # 현재 개미 위치
move = int(input())     # 이동 횟수

# 맵 무한이라 생각하고 쭉 간다음
x += move
y += move

# 나머지를 통해 작은 판 위치 찾기
x %= 2*N
y %= 2*M
if 0 <= x <= N:
    pass
else:
    x = 2*N - x

if 0 <= y <= M:
    pass
else:
    y = 2*M - y

print(x, y)

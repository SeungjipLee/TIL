'''
3 3
0 3
1 5
0 6
를 입력하면
3이 출력되면 된다.
현재 연결된 예제는
12가 나오면 됨
'''
import sys
sys.stdin = open('a.txt')

N, K = map(int, input().split())
board = [[0]*6 for _ in range(2)]
cnt = 12
for _ in range(N):
    S, Y = map(int, input().split())
    board[S-1][Y-1] += 1
    if board[S-1][Y-1] == K:
        cnt += 1
        board[S - 1][Y - 1] = 0
for i in range(2):
    for j in range(6):
        if board[i][j] == 0:
            cnt -= 1
print(cnt)
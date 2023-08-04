import sys
sys.stdin = open("input1.txt")

dx = [0, 1]
dy = [1, 0]

Testcase = int(input())
for test in range(Testcase):
    N, M = map(int, input().split())
    Board = [list(map(int, input().split())) for _ in range(N)]

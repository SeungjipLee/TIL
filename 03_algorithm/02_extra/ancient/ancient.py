import sys

sys.stdin = open("input1.txt")

Testcase = int(input())
for test in range(Testcase):
    N, M = map(int, input().split())
    Board = [list(map(int, input().split())) for _ in range(N)]
    maxx = 0
import sys
sys.stdin = open('a.txt')

def binary_search(start, end, goal):
    return

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = list(map(int, input().split()))
    cnt = 0
    for b in B:
        cnt += binary_search(0, N, b)

import sys
sys.stdin = open('s_input.txt')

Testcase = int(input())
for test in range(Testcase):
    N = int(input())
    numbers = list(map(int, input().split()))
    for i in range(N-1):

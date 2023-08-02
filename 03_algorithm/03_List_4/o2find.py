import sys
sys.stdin = open("sample_input (2).txt")

Testcase = int(input())
for tc in range(Testcase):
    L, A_pur, B_pur = map(int, input().split())
    A_first = B_first = 1
    A_center =
import sys
sys.stdin = open("input.txt")

Testcase = int(input())
for test in range(Testcase):
    A = list(input())
    B = A[:]
    B.reverse()
    if A == B:
        print(f'#{test+1}',1)
    else:
        print(f'#{test+1}',0)
import sys
sys.stdin = open("input (5).txt")

Testcase = int(input())
for test in range(Testcase):
    N = int(input())
    st = ''
    for i in range(N):
        A, B = input().split()
        B = int(B)
        st += A * B
    row = len(st)//10
    last = len(st)%10
    print(f'#{test+1}')
    for i in range(row+1):
        print(st[10*i:10*i+10])
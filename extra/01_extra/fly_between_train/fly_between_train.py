import sys
sys.stdin = open("s_input.txt")

Testcase = int(input())
for test in range(Testcase):
    A,B,C,D = map(int, input().split())
    ans = (A/(B+C))*D
    print(f'#{test+1}', ans)
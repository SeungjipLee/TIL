import sys
sys.stdin = open("sample_input (3).txt")

Testcase = int(input())
for test in range(Testcase):
    N, Q = map(int, input().split())
    List = [0]*N

    for i in range(Q):
        L, R = map(int, input().split())
        for j in range(L-1,R):
            List[j] = i+1
    print(f'#{test+1}', *List)
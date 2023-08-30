import sys
sys.stdin = open("s_input.txt")

Testcase = int(input())
for test in range(Testcase):
    Bus = int(input())
    Bus_x = []
    Bus_y = []
    List = [0]*5001
    Final_List = []

    for i in range(Bus):
        x, y = map(int, input().split())
        Bus_x.append(x)
        Bus_y.append(y)

    for i in range(Bus):
        for j in range(Bus_x[i], Bus_y[i]+1):
            List[j] += 1

    P = int(input())

    for i in range(P):
        c = int(input())
        Final_List.append(List[c])

    print(f'#{test+1}', *Final_List)

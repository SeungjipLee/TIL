import sys
sys.stdin = open("sample_input (1).txt")

Testcase = int(input())
for test in range(Testcase):
    goal, step = input().split()
    g_idx = 0
    s_idx = 0
    count = 0

    while g_idx < len(goal):
        if step[s_idx] != goal[g_idx]:
            g_idx -= s_idx
            s_idx = -1

        g_idx += 1
        s_idx += 1

        if s_idx == len(step):
            count += 1
            s_idx = 0

    result = len(goal) - count * len(step) + count
    print(f'#{test+1}', result)
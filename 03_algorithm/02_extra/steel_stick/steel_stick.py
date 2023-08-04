import sys
sys.stdin = open("sample_input (4).txt")

Testcase = int(input())
# 괄호끼리의 짝을 찾아야 하며
# 그 사이에 별이 몇 개 있는지 카운트
for test in range(Testcase):
    A = list(input())
    on_stage = 0
    final = 0

    for i in range(len(A) - 1):
        if (A[i] == '(') and (A[i + 1] == ')'):
            A[i], A[i + 1] = 0, 0

    for j in A:
        if j == 0:
            final += on_stage/2
        elif j == '(':
            on_stage += 1
        else :
            on_stage -= 1
            final += 1
    fin = int(final)
    print(f'#{test+1}', fin)
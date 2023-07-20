# 괄호 문제
TC = int(input())
for i in list(range(TC)):
    A = str(input())
    B = 0
    C = 0
    D = 0
    for j in A:
        if j == '(':
            B += 1
        else :
            C += 1
            if B < C:
                print('NO')
                D = 1
                break
    if B > C:
        print('NO')
        D = 2

    elif D == 0:
        print('YES')
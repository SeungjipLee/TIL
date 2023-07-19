TC = int(input())
for i in list(range(TC)):
    A = str(input())
    B = 0
    C = 0
    for j in A:
        if j == '(':
            B += 1
        else :
            C += 1
            if B < C:
                print('NO')
                break
            else :
                continue
    if B == (len(A)//2):
        print("YES")
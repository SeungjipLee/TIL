import sys
sys.stdin = open('a.txt')

T = int(input())
for tc in range(1, T+1):
    A = list(map(int, input()))
    B = list(map(int, input()))
    real_a = []
    real_b = []
    for i in range(len(A)):
        C = A[:]
        for j in range(1, 2):
            C[i] = (A[i]+j)%2
            C = [str(c) for c in C]
            real_a.append(int(''.join(C), 2))

    for i in range(len(B)):
        D = B[:]
        for j in range(1, 3):
            D[i] = (B[i] + j) % 3
            D = [str(d) for d in D]
            real_b.append(int(''.join(D), 3))
    Ra = set(real_a)
    Rb = set(real_b)
    print(f'#{tc}', *(Ra & Rb))
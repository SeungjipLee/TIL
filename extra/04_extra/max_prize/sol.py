import sys
sys.stdin = open('a.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = [int(i) for i in str(N)]
    C = A[:]    # 리버스
    C.reverse()
    K = min(A.count(max(A)), M) 
    while M != 0:
        for i in range(len(A)):
            if A[i] != max(A[i:]):
                j = -(C.index(max(A[i:]))+1)
                A[i], A[j] = A[j], A[i]
                C[-(i+1)], C[-(j+1)] = C[-(j+1)], C[-(i+1)]
                M -= 1
                if M == 0:
                    break
            else:
                M = 0
'''
31218888 3번

81218388
88218381
88818321

(3번 바꿔서)
(12318888)

82318881
88318821
88818321
'''



    print(f'#{tc}', end = ' ')
    print(*A, sep='')
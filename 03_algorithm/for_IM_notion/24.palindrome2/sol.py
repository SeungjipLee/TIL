import sys
sys.stdin = open('a.txt')

for _ in range(1, 11):
    tc = int(input())
    Board = [list(input()) for _ in range(100)]
    final = 1
    # 회문의 길이가 i인 애가 있는지 확인
    for i in range(100, 0, -1):
        a = 0
        # 회문의 길이의 절반만큼 회문인지 확인
        for k in range(100):
            for l in range(100-i+1):
                mid = 0
                for j in range(i//2):
                    if Board[k][l + j] != Board[k][l + i - 1 - j]:
                        break
                    else:
                        mid += 1
                if mid == i//2:
                    a = i
        for k in range(100):
            for l in range(100-i+1):
                mid = 0
                for j in range(i//2):
                    if Board[l+j][k] != Board[l+i-1-j][k]:
                        break
                    else:
                        mid += 1
                if mid == i//2:
                    a = i
        if a != 0:
            final = a
            break
    print(f'#{tc}', final)
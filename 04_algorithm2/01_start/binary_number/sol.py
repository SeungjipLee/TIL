import sys
sys.stdin = open('sample_input (2).txt')

T = int(input())
for tc in range(1, T+1):
    N, N16 = input().split()
    answer = ''
    for char in N16:
        # print(bin(int(char,base=16))[2:].zfill(4), end='')
        result = bin(int(char, base=16))[2:]
        while len(result) != 4:
            result = '0' + result
        answer += result
    print(f'#{tc}', answer)
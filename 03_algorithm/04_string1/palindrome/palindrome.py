import sys
sys.stdin = open("sample_input.txt")

def palindrome(string, N, M):
    for i in range(N-M+1):
        com = string[i:i+M]
        check = 0
        for j in range(M//2):
            if com[j] == com[M-j-1]:
                check += 1
        if check == M//2:
            return com
    return


Testcase = int(input())
for test in range(Testcase):
    N, M = map(int, input().split())
    Board = [input() for _ in range(N)]
    List = []

    for i in range(N):
        if palindrome(Board[i], N, M) != None:
            List.append(palindrome(Board[i], N, M))

    for i in range(N):
        stra = ''
        for j in range(N):
            stra += Board[j][i]
        if palindrome(stra, N, M) != None:
            List.append(palindrome(stra, N, M))

    print(f'#{test+1}', *List)
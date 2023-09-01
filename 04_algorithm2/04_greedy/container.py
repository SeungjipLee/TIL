import sys
sys.stdin = open('container.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    Conta = list(map(int, input().split()))
    Truck = list(map(int, input().split()))
    Conta.sort()
    Truck.sort()
    final = 0
    while Conta:
        if Truck:
            c = Conta.pop()
            if c <= Truck[-1]:
                Truck.pop()
                final += c
            else:
                continue
        else:
            break
    print(f'#{tc}', final)
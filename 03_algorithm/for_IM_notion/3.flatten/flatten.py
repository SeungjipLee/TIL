import sys
sys.stdin = open('input (1).txt')

def dum(Dump):
    for i in range(Dump):
        ground[0] += 1
        ground[-1] -= 1
        ground.sort()
    return ground[-1] - ground[0]


for tc in range(1, 11):
    Dump = int(input())
    ground = list(map(int, input().split()))
    ground.sort()
    print(f'#{tc}', dum(Dump))
import sys
sys.stdin = open('input.txt')

for tc in range(10):
    N = int(input())
    Building = list(map(int, input().split()))
    final = 0
    for i in range(2, N-2):
        center = Building[i]
        compare = [Building[i] for i in [i-2, i-1, i+1, i+2]]
        if max(compare) < center:
            final += center - max(compare)
    print(f'#{tc+1}', final)
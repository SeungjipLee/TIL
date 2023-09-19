import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    N, *nums = map(int, input().split())
    idx = 0
    cnt = 0
    while idx < N-1:
        gas = nums[idx]
        if idx + gas >= N-1:
            break
        compare = []
        div = 0
        for next in range(idx+1, idx+gas+1):
            if next<=N-1:
                compare.append(nums[next]+div)
                div += 1
        r = compare.index(max(compare))
        idx += r+1
        cnt += 1
    print(f'#{tc}', cnt)
import sys
sys.stdin = open('a.txt')

# row : 현재 조사 대상
# chosen : 선택 대상
def perm(row, chosen):
    if row == N:
        tem = []
        for i in chosen:
            tem.append(data[i])
        results.append(tem)
        pass

    # 모든 N개의 원소를 조사했는지 판단
    for i in range(N):
        # i 번째에 쓰겠다고 이전에 판정된 적이 있다면
        # 현재 조사 대상을 i 번째에 쓸 수 없으므로
        if i in chosen:
            continue
        chosen[row] = i     # row 번째 대상을 i 번째에 둬서 사용하겠다.
        perm(row + 1, chosen)
        chosen[row] = -1

for tc in range(1):
    N = 6
    data = input()
    # i 번째에 들어갈 수 있는 수 0, N-1 까지를 제외한
    chosen = [-1] * N
    results = []
    perm(0, chosen)
    print(results)
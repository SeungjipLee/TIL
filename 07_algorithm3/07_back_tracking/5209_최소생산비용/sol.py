import sys
sys.stdin = open('input.txt')

# nPr : n == r
# r : 사용중인 원소의 개수
# acc : 현재 경우의 수 까지 누적된 값
def permutation(r, acc):
    global result
    if acc > result:
        return
    # 종료 시점
    if r == N:
        # 무슨 일 할건데?
        # 모든 공장 순회 다 했고
        # 각 공장의 비용을 다 더했는데
        # 비교 대상보다 acc의 값이 작으면
        if acc < result:
            result = acc
        return
    else:
        # 모든 공장이 하나씩은 만들어야 하니
        for i in range(N):
            if not visited[i]:
                visited[i] = True
                # A 공장의 1번 제품 생산 비용을 acc에 누적해본 다음
                permutation(r+1, acc + Board[r][i])
                # A 공장이 1번 제품을 안 쓰고, 2번 제품을 썼을 때
                visited[i] = False


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    Board = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    # 비교 대상군
    result = sum(sum(Board,[]))
    permutation(0, 0)
    print(f'#{tc}', result)
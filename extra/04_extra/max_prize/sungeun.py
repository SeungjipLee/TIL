import sys
sys.stdin = open('a.txt')
# 어떤 리스트가 정렬이 되어 있는지 확인(전부 내림차순인지)
# 되어있다면 남은 변경 횟수가 홀/짝 여부와 연속된 수 여부를 판단 -> 가지치기를 위함
def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] < arr[i + 1]:
            return False

    return True

# 내림차순 정렬되었을 때 자기 오른쪽에 같은 애가 있는지 확인
# 같은 수가 2개 이상이면 바꾸는 회수 무한 가능
def check_duplicate(arr):
    for i in range(len(arr) - 1):
        if arr[i] == arr[i + 1]:
            return True

    return False


def dfs(idx, change_cnt):
    global result, end
    # end 에 종료조건을 넣어둠(최초 False였으나, 정렬했는데 연속되거나 남은 횟수 짝수면 True)
    if end:
        return

    # 최대건 뭐건 바꾸는 횟수 끝났으면 결론 출력(로직 자체를 항상 최대가 되도록 구현했으므로)
    if change_cnt == K:
        if result < ''.join(numbers):
            result = ''.join(numbers)

        return

    # 횟수 안 끝났는데 만약 정렬되어 있다면
    if is_sorted(numbers):
        # 남은 횟수가 홀수거나 연속된 수가 없다면 끝에 두 개를 바꿔야 그나마 커짐
        if (K - change_cnt) % 2 and not duplicate:
            numbers[-1], numbers[-2] = numbers[-2], numbers[-1]
            result = ''.join(numbers)
            # 정렬되어있지 않을 수 있으니 되돌려 주자
            numbers[-1], numbers[-2] = numbers[-2], numbers[-1]
        # 정렬된 상태에서 남은 횟수 짝수거나 연속된 수가 있다면 끝
        else:
            result = ''.join(numbers)
            end = True
        return

    # 횟수가 안 끝났는데 만약 정렬되어있지 않다면
    # 어떤 인덱스를 기준으로 그보다 오른쪽에 더 큰 애가 있는지 확인해야하는데
    # 만약 오른쪽에 애가 없다면 다음 인덱스를 봐야하므로
    change = False
    # 0을 기준으로 1부터 N-1까지 큰 애랑 바꿔줌
    for i in range(idx + 1, N):
        if numbers[i] > numbers[idx]:
            numbers[i], numbers[idx] = numbers[idx], numbers[i]
            dfs(idx + 1, change_cnt + 1)
            # 다음 경우의 수에서도 인덱스로 볼 것이니 원본이 바뀌면 안됨
            numbers[i], numbers[idx] = numbers[idx], numbers[i]
            # 변화했다면 횟수를 1증가시켜야함
            change = True
    # 안바뀐 경우에 아직 바꿀 인덱스가 남아있다면 다음 인덱스로 넘어가되 교체 횟수는 증가하면 안됨
    if not change and idx < len(numbers):
        dfs(idx + 1, change_cnt)


T = int(input())

for tc in range(T):
    N, K = map(int, input().split())

    numbers = list(str(N))  # 숫자 하나씩 리스트에 담기
    result = str(N)         # result 에 입력값 담고
    N = len(numbers)        # N에는 입력값 길이 담아두기

    duplicate = check_duplicate(numbers)

    end = False

    # 0번 인덱스부터 다음 인덱스들을 분석하며 바꿔감
    for i in range(N):
        dfs(i, 0)

    print(f'#{tc + 1} {result}')
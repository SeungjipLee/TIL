# 순열
# nPr : n개의 요소 중, r개를 사용하여 순서대로 나열

def perm(r, K):
    # 재귀 함수
    # 종료 조건(재귀의 기저까지 왔을때의 상황)
    # print(r)
    # print(visited)
    # print(completed_perm)
    if r == K:
        # 내가 원하는 무언가를 실행
        print(completed_perm)
        return
    else:
        # 내가 가진 모든 arr의 모든 원소를 매번 사용할 것인지 체크
        for i in range(N):
            # arr 의 i번째 요소를 쓴 적이 있는지 없는지를 기준으로 판단
            # if visited[i] == True: continue # i번째에는 값을 채웠다.
            if not visited[i]:  # i번째를 아직 쓰지 않았다면
                visited[i] = True
                # r : 사용한 수의 개수 -> 0번째 위치에 값을 담으면 r 1증가
                # arr의 i번째
                completed_perm[r] = arr[i]
                perm(r+1, K) # 다음 번 조사에는 한 개 채웠다.
                visited[i] = False

arr = [1, 2, 3]
N = len(arr)
# 내가 perm 함수 호출시 arr의 i번째 값을 사용했던 적이 있는지 판별
visited = [0] * N
completed_perm = [0] * N
# 값을 한 번도 쓰지 않을 상태로 순열 생성 시작
print('-----순열-----')
perm(0, 3)

# 중복순열

def re_perm(r, K):
    # 재귀 함수
    # 종료 조건(재귀의 기저까지 왔을때의 상황)
    if r == K:
        # 내가 원하는 무언가를 실행
        print(completed_re_perm)
        return
    else:
        # 내가 가진 모든 arr의 모든 원소를 매번 사용할 것인지 체크
        for i in range(N):
            # arr 의 i번째 요소를 쓴 적이 있는지 없는지를 기준으로 판단
            # if visited[i] == True: continue # i번째에는 값을 채웠다.
            # r : 사용한 수의 개수 -> 0번째 위치에 값을 담으면 r 1증가
            # arr의 i번째
            completed_re_perm[r] = arr[i]
            re_perm(r+1, K) # 다음 번 조사에는 한 개 채웠다.

arr = [1, 2, 3]
N = len(arr)
# 내가 perm 함수 호출시 arr의 i번째 값을 사용했던 적이 있는지 판별

completed_re_perm = [0] * N
# 값을 한 번도 쓰지 않을 상태로 순열 생성 시작
print('----중복순열----')
re_perm(0, 3)
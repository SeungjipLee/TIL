# 합모양의 경우 방향을 좌표로 설정
px = [1, 0, -1, 0]
py = [0, 1, 0, -1]
# 곱모양의 경우 방향을 좌표로 설정
cx = [1, 1, -1, -1]
cy = [-1, 1, 1, -1]

# 테스트케이스 입력
for T in range(int(input())):
    # 체스판, 무기 범위 입력
    n, m = map(int, input().split()) 
    # 리스트 컴프리헨션을 활용한 이중리스트
    arr = [ list(map(int, input().split())) for _ in range(n) ]
    # 최댓값을 찾기위한 곱과 합의 비교 결과
    result=0

    # 이중리스트를 통해 모든 원소를 돌겠다
    for i in range(n):
        for j in range(n):
            # 곱모양 합모양의 합들의 변수 설정 겸 중앙 값을 미리 부여
            plus_value=arr[i][j]
            cross_value=arr[i][j]
            # 범위를 0부터 3까지 총 4개로 잡은 이유??
            for k in range(4): 
                # 무기 범위를 설정하는 듯
                for w in range(1, m):
                    pxx, pyy=i+px[k]*w, j+py[k]*w
                    cxx, cyy=i+cx[k]*w, j+cy[k]*w
                    if 0<=pxx<n and 0<=pyy<n:
                        plus_value += arr[pxx][pyy]
                    if 0<=cxx<n and 0<=cyy<n:
                        cross_value += arr[cxx][cyy]
            result = max(result, plus_value, cross_value)
    print("#{} {}".format(T+1,result))
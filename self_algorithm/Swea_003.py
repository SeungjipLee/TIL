# 파리잡기

# 합 모양의 공격의 방향을 순서쌍으로 제공
plus_xmove = [1, -1, 0, 0]
plus_ymove = [0, 0, -1, 1]

# 곱 모양의 공격의 방향을 순서쌍으로 제공
cross_xmove = [1,1,-1,-1]
cross_ymove = [-1,1,1,-1]

# 테스트 케이스 입력받기
Test_Case = int(input())

# 행렬 사이즈와 공격 범위 설정
Mat_size, Attack_range = map(int,input().split())

# 행렬 정보 이중리스트로 입력 받기
Mat_info = [list(map(int,input().split())) for i in range(Mat_size)]

# 각 점마다의 합공격(변수)과 곱공격(변수)의 최댓값을 비교 -> 각 점마다 비교를 한 다음 최종 비교 리스트에 넣고 초기화
Maximum_Group = []

for i in range(Mat_size):
    for j in range(Mat_size):
        plus_sum = Mat_info[i][j]
        cross_sum = Mat_info[i][j]
        
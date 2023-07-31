# N x N 행렬이 주어질 때,

# 시계 방향으로 90도, 180도, 270도 회전한 모양을 출력하라.


# [제약 사항]

# N은 3 이상 7 이하이다.

# [입력]

# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.

# 각 테스트 케이스의 첫 번째 줄에 N이 주어지고,

# 다음 N 줄에는 N x N 행렬이 주어진다.

# [출력]

# 출력의 첫 줄은 '#t'로 시작하고,

# 다음 N줄에 걸쳐서 90도, 180도, 270도 회전한 모양을 출력한다.

# 입력과는 달리 출력에서는 회전한 모양 사이에만 공백이 존재함에 유의하라.

# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

def rot_90(Row_List):           # 이중 리스트를 들고와서
    New_list = []               # 뉴 리스트 생성
    for i in range(Mat_siz):    # 행렬 크기만큼 진행
        nsmall_List = []            # 이중 리스트 중 작은 리스트 생성
        for j in range(Mat_siz):    # 행렬 크기만큼 진행
            nsmall_List.append(Row_List[Mat_siz-1-j][i])    # 작은 리스트 안에 원소들 넣음
        New_list.append(nsmall_List)                        # 작은 리스트를 큰 리스트에 추가
    return New_list         # 새로운 이중 리스트 완성

Test_Case = int(input())        # 테스트 케이스 입력

for k in range(1, Test_Case + 1):
    Mat_siz = int(input())
    Row_List = []
    
    for i in range(Mat_siz):
        small_list = list(map(int,input().split()))
        Row_List.append(small_list)

    print(f'#{k}')

    rot1 = rot_90(Row_List)
    rot2 = rot_90(rot1)
    rot3 = rot_90(rot2)

    for i in range(Mat_siz):
        print(*rot1[i],sep='', end = ' ')
        print(*rot2[i],sep='', end = ' ')
        print(*rot3[i],sep='')
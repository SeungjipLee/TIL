# 스도쿠 확인 문제
standard_consist = set(range(1,10))

def check_row(list):    # set로 변환 후 확인하자
    if set(list) == standard_consist:
        global checking_count
        checking_count += 1
    
Test_Case = int(input())

for i in range(Test_Case):
    checking_count = 0
    Important_List = []
    for j in range(9):
        small_list = list(map(int,input().split()))
        Important_List.append(small_list)

    # 가로 줄 확인
    # 가로 줄 {Important_List[k] : (0<=k<=8)}
    for k in range(9):
        check_row(Important_List[k])

    # 세로 줄 확인
    # 세로 줄 {Important_List[k][j] k먼저 0에서 8까지 움직이고 j는 그 뒤에 움직이는 이중 for문}

    Col = []
    for l in range(9):
        small_col = []
        for m in range(9):
            small_col.append(Important_List[m][l])
        Col.append(small_col)
    
    for n in range(9):
        check_row(Col[n])


    # 박스 확인
    # 박스 {Important_List[x][y] x: 0~2, 3~5, 6~8 / y: 0~2, 3~5, 6~8 }
    # 3등분 선
    R1 = [0, 1, 2]
    R2 = [3, 4, 5]
    R3 = [6, 7, 8]

    Box = []
    small_box = []
    for x in R1:
        for y in R1:
            small_box.append(Important_List[x][y])
    Box.append(small_box)
    small_box = []
    for x in R1:
        for y in R2:
            small_box.append(Important_List[x][y])
    Box.append(small_box)
    small_box = []
    for x in R1:
        for y in R3:
            small_box.append(Important_List[x][y])
    Box.append(small_box)
    small_box = []
    for x in R2:
        for y in R1:
            small_box.append(Important_List[x][y])
    Box.append(small_box)
    small_box = []
    for x in R2:
        for y in R2:
            small_box.append(Important_List[x][y])
    Box.append(small_box)
    small_box = []
    for x in R2:
        for y in R3:
            small_box.append(Important_List[x][y])
    Box.append(small_box)
    small_box = []
    for x in R3:
        for y in R1:
            small_box.append(Important_List[x][y])
    Box.append(small_box)
    small_box = []
    for x in R3:
        for y in R2:
            small_box.append(Important_List[x][y])
    Box.append(small_box)
    small_box = []
    for x in R3:
        for y in R3:
            small_box.append(Important_List[x][y])
    Box.append(small_box)
    
    
    for a in range(9):
        check_row(Box[a])

    
    if checking_count == 27:
        b = 1
    else: b=0
    print(f'#{i+1}',b)
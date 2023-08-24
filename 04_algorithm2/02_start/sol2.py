import sys
sys.stdin = open('js.txt')

T = int(input())

# 코드 정보

Code = {
    '211': 0, '221': 1, '122': 2, '411': 3, '132': 4,
    '231': 5, '114': 6, '312': 7, '213': 8, '112': 9,
}


for tc in range(1, T+1):
    N, M = map(int, input().split())
    Board = [input().strip('0') for _ in range(N)]
    Board_shrt = set()

    # 암호만 있는 줄을 받기 위한 작업(중복 처리까지)
    for i in Board:
        if i != ['0'* M] and i != '':
            Board_shrt.add(i)
    Board = list(Board_shrt)

    # 2진법 표현으로 전부 바꿈(Board 안에 들어가있음)
    for i in range(len(Board)):
        st = ''
        for j in Board[i]:
            st += bin(int(j, base=16))[2:].zfill(4)
        Board[i] = st.strip('0')
    print(Board)

    # # 인덱스에 집착말고 유연하게 걍 8개 받아 그 이후로 8개 받아의 반복
    for string in Board:
        final = 0
        no_double = []      # 중복 방지 리스트
        mid_list = []
        vac = ''
        cnt = 1
        for i in range(len(string)-1):
            if string[i] == string[i+1]:
                cnt += 1
            else:
                vac += str(cnt)
                cnt = 1
            if len(vac) == 3 and vac in Code:
                mid_list.append(Code[vac])
            if len(mid_list) == 8:
                mid = 0
                for k in range(len(mid_list)):
                    if k%2:
                        mid += mid_list[k]
                    else:
                        mid += mid_list[k]*3
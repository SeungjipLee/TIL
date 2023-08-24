import sys
sys.stdin = open('js.txt')
import copy

dic = {'211': 0, '221': 1, '122': 2, '411': 3, '132': 4,
       '231': 5, '114': 6, '312': 7, '213': 8, '112': 9}  # 앞에 0생각 x

t = int(input())
for qw1 in range(1, t + 1):
    n, m = map(int, input().split())
    k = 1
    check = list(set([input() for _ in range(n)]))  # 입력을 받고 중복 제거, ex) 000000코드00000코드0000 이런식으로 저장   0 제거 필요
    check = sorted(check)[1:]  # 맨앞 000000만 있는 경우 제거
    ans = []
    real_ans = 0
    visited = []
    for i in check:
        result = format(int(i, 16), 'b').lstrip('0')  # 2진수로 바꾸고 앞 0제거
        start = 0  # 1발견할때 와 아닐때 구별 위해 start 변수 사용
        info = 0
        n1 = n2 = n3 = 0
        for j in range(len(result)):
            if len(ans) == 8:  # ans에 코드가 8개 모일때 실행
                if ans not in visited:  # visited필요 이유 = > 코드 1 과 코드 2가 따로 있다 => ok 그런데 코드1 0000코드2 이런식으로 되어있으면 코드는 일단 돌아가고 코드 1에 대한 ans값이 있을것 => 중복 제거 필요
                    visited.append(copy.deepcopy(ans))  # 중복 체크 필요
                    for k in range(len(ans)):
                        if k % 2 == 0:
                            info = info + ans[k] * 3  # 값
                        else:
                            info = info + ans[k]
                    if info % 10 == 0:
                        real_ans = real_ans + sum(ans)  # 문제 제시 사항,
                ans = []
                info = 0
            else:  # 아니면 이 밑에 실행
                if start == 0 and n1 == n2 == n3 == 0 and result[j] == '1':  # result[j] 1이면 실행
                    start = 1
                    cnt = 1  # 1을 찾은거 = 1개 카운트 필요
                if start == 1:
                    if n1 != 0 and n2 != 0 and n3 != 0:  # n1 n2 n3 값이 다 있을때 아닐때 구별 필요
                        ratio = int(min(int(n1), int(n2), int(n3)))  # 다있다면 비율 찾기 실행 비율은 n1 n2 n3 값의 최솟값
                        ans.append(dic[str(int(n1) // ratio) + str(int(n2) // ratio) + str(int(n3) // ratio)])  # dic에서 값 가져오기 이렇게 ans= [7,1,2,3,4,5,6,8] 처럼 모이게된다
                        start = 0  # 사용후 초기화 필요
                        n1 = n2 = n3 = 0
                        continue
                    if result[j] == result[j + 1]:  # 다음값과 같다 = count 증가 필요 j위치의 갯수가 아닌 그 뒤에 즉 j+1까지 count 한것 => 그렇다면 코드가 맨끝에 있을땐? 나도 모름
                        cnt = cnt + 1
                    else:
                        if n1 == 0:  # 차근차근 값 넣어줌
                            n1 = str(cnt)
                            cnt = 1
                        elif n2 == 0:
                            n2 = str(cnt)
                            cnt = 1
                        else:
                            n3 = str(cnt)
                            cnt = 1
    print(f'#{qw1} {real_ans}')
    # 힘들었던 점은 코드 입력을 각각 받을수 있을것이라 생각 => 따로 처리 하는 방법으로 고민, 하지만 코드가 겹치는 경우가 너무 다양함 ex) 코드1000코드2 이럴때도 있지만 코드한개 안에 000이 포함될때도 있음
    # 코드 처리를 위해 다른 방법필요를 느끼고 그냥 한줄로 즉 코드1000코드2 를 한번에 처리를 느낌,=> 대규모 공사 +인터넷 통한 아이디어

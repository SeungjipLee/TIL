import sys
sys.stdin = open("input.txt")

Testcase = 10       # 테스트 케이스는 10번으로 고정
for test in range(Testcase):        # 테스트 케이스만큼 돌거다
    width = int(input())        # 가로 폭
    List = list(map(int, input().split()))  # 가로폭의 개수만큼 리스트로 값 받기
    Sum = 0 # 최종 결과값이 될 것(view 가 좋은 방 개수)

    for i in range(2, width-2):     # 젤 처음 2개랑 마지막 2개는 고려 안할 것
        new_lst = [List[i-2], List[i-1], List[i], List[i+1], List[i+2]]  # 중심을 기준으로 양쪽 2개씩을 비교해야 함
        max_nl = 0          # 5개를 비교하는 것 중 최댓값을 기록할 것
        for k in new_lst:
            if k > max_nl:
                max_nl = k
        if max_nl != List[i]:  # 만약 가운데 값이 최댓값이 아니라면 다음으로 넘어가 5개 새로 받아
            continue
        else:
            new_lst.pop(2)      # 가운데 값이 최대라면 가운데 놈 빼고
            second_max = new_lst[0]     # 두번째 최댓값을 받아
            for j in new_lst:
                if j > second_max:
                    second_max = j
            div = max_nl - second_max   # 가운데 값이 최대일테니 최대 - 차대가 뷰가 좋은 집의 개수가 될 것이니
            Sum += div  # 총 기록중인 집에 그 개수들을 더해간다
    print(f'#{test+1} {Sum}')
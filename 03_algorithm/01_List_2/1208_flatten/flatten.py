import sys
sys.stdin = open("input.txt")

def one_dump(Li):       # 1 dump에 일어나는 일(인자는 정렬된 리스트를 받는다)
    Li[-1] -= 1     # 최댓값을 1빼고
    Li[0] += 1      # 최솟값은 1더한 후
    Li.sort()       # 다시 정렬(해야만 다시 함수에 넣을 수 있음)
    return Li

Testcase = 10              # 10번 시행할거야
for i in range(Testcase):
    dump = int(input())     # dump 횟수
    List = list(map(int, input().split()))  # 리스트 입력
    List.sort()     # 정렬해
    Sorted_List = List

    for k in range(dump):       # 덤프 횟수만큼 함수 돌려
        one_dump(Sorted_List)

    div = Sorted_List[-1] - Sorted_List[0]  # 최댓값 - 최솟값 반환
    print(f'#{i+1} {div}')
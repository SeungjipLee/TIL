# 카드 N(4~10)장 나란히 놓는 중
# 1~99가 적혀져 있다.
# 이 카드 중 K(2~4) 장을 선택하여 가로로 나란히 정수를 만들기로 했다.
# 상근이가 만들 수 있는 정수는 모두 몇 개인가?

N = int(input())
K = int(input())

num_list = []
idx_list = list(range(N))
pick_idx = []

for _ in range(N):
    num_list.append(input())

print(num_list)
print(idx_list)
blank = ''

# 어떻게 K개를 뽑을 것인가?
# 순열 (nPk)
# 문자열로 쓰자

# N : 물품의 수, K : 최대 무게
N, K = map(int, input().split())
final = 0
Info = []

for _ in range(N):
    w, v = map(int, input().split())
    Info.append((w, v))
print(Info)

'''
순열? -> 시간 초과
DP -> 어떻게?
1. 가치가 높은 순 -> x
2. 가치가 낮은 순 -> x
3. 무게가 높은 순 -> x
4. 무게가 낮은 순
ex) 7을 채워야하는데 (3, 3), (3, 4), (4, 4)인 경우
처음 2개 하면 7
뒤에 2개 하면 8

단순한 정렬이 아닌 다른 알고리즘이 필요
'''


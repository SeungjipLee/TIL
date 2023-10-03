# n개의 별들을 이어서 하나의 별자리를 만들 것
# 별자리를 이루는 모든 선은 일직선
# 모든 별들은 별자리 위의 선을 통해 직/간접적으로 이어짐
# 두 별 사이의 거리만큼의 비용이 발생
from math import sqrt
import heapq

def distance(x, y):
    return sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)


N = int(input())
Star = []
for _ in range(N):
    a, b = map(float, input().split())
    Star.append((a, b))

Adj = [[] for _ in range(N)]

for i in range(N):
    a = Star[i]
    for j in range(N):
        if i == j:
            continue
        b = Star[j]
        Adj[i].append((distance(a, b), j))
# print(Adj)

visited = [0] * N
HQ = [(0, 0)]
final = visit = 0
while visit != N:
    dis, nod = heapq.heappop(HQ)
    if visited[nod] == 1:
        continue

    visited[nod] = 1
    visit += 1
    final += dis
    for i in Adj[nod]:
        if visited[i[1]] == 1:
            continue
        heapq.heappush(HQ, i)

print(round(final, 2))
from collections import deque
from itertools import combinations
import sys
sys.stdin = open('17471.txt')
input = sys.stdin.readline

def BFS_A():

def BFS_B():


def check(A, B):
    a, b = False, False
    if len(A) == 1:
        a = True
    if len(B) == 1:
        b = True



N = int(input())
population = list(map(int, input().split()))
Adj = [[] for _ in range(N)]
for i in range(N):
    a, *b = map(int, input().split())
    Adj[i].extend([k-1 for k in b])
print(Adj)
total = set(range(1, N+1))
answer = 10**9

for r in range(1, N//2+1):
    for c in combinations(range(1, N+1), r):
        A = (set(c))
        B = total - A
        A = list(A)
        B = list(B)



        # if a+b == N:
        #     answer = min(answer, abs(suma-sumb))

# if answer == 10**9:
#     print(-1)
# else:
#     print(answer)
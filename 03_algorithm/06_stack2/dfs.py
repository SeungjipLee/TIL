import sys
from pprint import pprint
sys.stdin = open('a.txt')

# 노드 번호를 받아서 해당 노드부터 조사를 시작
def DFS(node):
    # stack을 활용해보자
    stack = [node]

    # 조사 여부 체크용 리스트
    visited = [False]*(V+1)
    visited[node] = True

    # 언제까지 조사(스택 안에 값이 있는 동안)
    while stack:
        start = stack.pop() # stack은 항상 LIFO 마지막 들어간 요소 빼내서 쓸거다.
        # 다음 조사를 시작하기전, 해당 위치가 이미 조사한 적이 있다면 안가도록 체크 하는 방법
        # 이전에 방문한 적이 없다면
        if visited[start] == 0:
            visited[start] = True
            # 현재 위치 기준으로 다음 위치 조사
            print(start, end=' ')
            for next in range(0, V+1):
                # 다응 조사 가능 여부
                if matrix[start][next] == 1 and visited[next] == 0:
                    stack.append(next)

# V : node 의 개수
# E : edge 의 개수
V, E = map(int, input().split())
# 간선 정보
data = list(map(int, input().split()))

# 이동 가능한 정보 2차원 리스트
matrix = [[0]*(V+1) for _ in range(V+1)]

# 모든 간선 순회
for i in range(0, E*2, 2):
    matrix[data[i]][data[i+1]] = 1
    matrix[data[i+1]][data[i]] = 1
   

print(V, E)
pprint(data)
pprint(matrix)
DFS(1)
'''
하나의 집합을 하나의 트리로 표현
make-set
 : 파이썬의 경우 변수 선언과 동시에 된다.
 : 여기서 parents를 자기 자신으로 설정하면 된다.
union(a, b)
 : 두 노드가 속한 집합을 합치는 함수
 : 방향이 존재하며 b를 a의 부모로 설정(방향은 문제 내용으로 판단)
find-set
 : 어떤 노드의 부모가 누구인지 확인하는 함수
'''

# 0 ~ 9번 노드가 있다.
# make set : 집합을 만들어 주는 과정
# 각 요소가 가르키는 값이 부모
parent = [i for i in range(10)]

# find-set : 부모가 누구인지 확인하는 함수
def find_set(x):
    if parent[x] == x:
        return x

    # return find_set(parent[x])
    # 경로 압축
    parent[x] = find_set(parent[x])
    return parent[x]

# union
def union(x, y):
    # 1. 이미 같은 집합인 지 체크
    x = find_set(x)
    y = find_set(y)

    if x == y:
        print("싸이클 발생")
        return

    # 2. 다른 집합이라면, 같은 대표자로 수정
    # 그 규칙은 작은 숫자를 대표로 만들자
    elif x < y:
        parent[y] = x
    else:
        parent[x] = y


union(0, 1)
union(2, 3)
union(1, 3)

# 싸이클 발생
# 이미 같은 집합에 속한 원소를 한 번 더 union
union(0, 2)


print(find_set(2))
print(find_set(3))

# 같은 그룹인지 판별
t_x = 0
t_y = 2

if find_set(t_x) == find_set(t_y):
    print(f'{t_x}와 {t_y}는 같은 집합에 속해 있습니다.')
else:
    print(f'{t_x}와 {t_y}는 다른 집합에 속해 있습니다.')


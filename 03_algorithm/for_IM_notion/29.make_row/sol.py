'''
5
0 1 1 3 2
를 입력하면
4 2 5 3 1
이 출력되도록
'''
N = int(input())
arr = list(map(int, input().split()))
final = []
for i in range(N):
    final.insert(i-arr[i], i+1)
print(*final)
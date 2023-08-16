def f(i, N, s, t): # s : i-1 원소까지 부분집합의 합, # t : 찾으려는 합
    global cnt
    cnt += 1
    if s == t:
        print(bit)
    elif i == N: # 남은 원소가 없는 경우
        return
    elif s > t:
        return
    else:
        bit[i] = 1      # 부분집합에 A[i] 포함
        f(i+1, N, s+A[i], t)
        bit[i] = 0      # 부분집합에 A[i] 빠짐
        f(i+1, N, s, t)
        return

N = 10
bit = [0] * N
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cnt = 0
f(0, N, 0, 1)
print(cnt)
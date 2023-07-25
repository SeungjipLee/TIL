# 문제
# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

# 입력
# 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

# 출력
# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.
# --------------------------------시간 초과---------------------------------------
# A = input()
# B = []
# for i in A:
#     B.append(ord(i))
# for j in B:
#     if j > 96:
#         j = j-32
# C = []
# for k in B:
#     C.append(B.count(k))
# if max(C) == C.count(max(C)):
#     N = max(C)
# else :
#     print('?')
#     quit()
# for l in B:
#     if B.count(l) == N:
#         Q = l
# for m in A:
#     if ord(m) == Q:
#         print(m.upper())
#         quit()
#     elif ord(m)-32 == Q:
#         print(m.upper())
#         quit()

# ----------------------시간 초과-----------------------------------------
A = [chr(i) for i in range(ord('A'), ord('Z')+1)]
B = [0]*26
a = 0
N = input()
N = N.upper()
for i in range(26):
    if A[i] in N:
        B[i] = N.count(A[i])
print(B)
    
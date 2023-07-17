A = [chr(i) for i in range(ord('A'), ord('Z')+1)]
B = [0]*26
N = input()
N.upper()
for i in range(27):
    B[i] = N.count(A[i])
print(B)
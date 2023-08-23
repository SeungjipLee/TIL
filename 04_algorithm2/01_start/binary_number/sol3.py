import sys

sys.stdin = open('sample_input (2).txt')

hex_to_bin = {hex(i).replace('0x', '').upper() : f'{i:04b}' for i in range(16)}
print(hex_to_bin)

T = int(input())
for tc in range(1, T + 1):
    N, N16 = input().split()
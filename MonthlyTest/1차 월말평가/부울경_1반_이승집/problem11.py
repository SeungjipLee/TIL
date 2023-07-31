############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 sum, min, max, len 함수를 사용하지 않습니다.
# 사용시 감점처리 되니 반드시 확인 바랍니다.
def get_row_col_maxsum(matrix):
    N = 0
    M = 0
    sum = 0
    max_row = 0
    max_col = 0

    for i in matrix:
        N += 1
    for j in matrix[0]:
        M += 1


    for k in range(N):
        row_sum = 0
        for m in range(M):
            row_sum += matrix[k][m]
        if row_sum >= max_row:
            max_row = row_sum

    for p in range(M):
        col_sum = 0
        for q in range(N):
            col_sum += matrix[q][p]
        if col_sum >= max_col:
            max_col = col_sum

    if max_col > max_row:
        sum = max_col
        return 'col', sum

    else:
        sum = max_row
        return 'row', sum
        
    return sum
    # 여기에 코드를 작성하여 함수를 완성합니다.
    


# 아래 코드는 실행 확인을 위한 코드입니다.
if __name__ == '__main__':
    # 예시 코드는 수정하지 마세요.
    example_matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]

    example_matrix2 = [
        [11, 5, 49, 20],
        [28, 16, 20, 33],
        [63, 17, 1, 15]
    ]
    print(get_row_col_maxsum(example_matrix))   # => ('row', 58)
    print(get_row_col_maxsum(example_matrix2))  # => ('col', 102)

    # 여기부터 아래에 추가 테스트를 위한 코드 작성 가능합니다.
    
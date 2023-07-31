############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 sum, min, max, len 함수를 사용하지 않습니다.
# 사용시 감점처리 되니 반드시 확인 바랍니다.
def caesar(word, num):
    cipher = ''         # 최종 결과
    for char in word:
        if char.isupper():      # 대문자 인 경우
            k = (ord(char)+ num - 13)%26 + 65       # 오버되어도 돌아와야하므로 나머지로 연산 
            char = chr(k)   # 최종 결과에 추가
        elif char.islower() :               # 아래도 동일방식
            k = (ord(char)+ num - 19)%26 + 97
            char = chr(k)
        cipher += char
    return cipher
    # 여기에 코드를 작성하여 함수를 완성합니다.
    


# 아래 코드는 실행 확인을 위한 코드입니다.
if __name__ == '__main__':
    # 예시 코드는 수정하지 마세요.
    print(caesar('ssafy', 1))   # => ttbgz
    print(caesar('Python', 10)) # => Zidryx
    # 여기부터 아래에 추가 테스트를 위한 코드 작성 가능합니다.
    print(caesar('x', 3))
    print(caesar('x', 29))
    print(caesar('Ny', 3))
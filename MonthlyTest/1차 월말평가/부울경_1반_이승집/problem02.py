############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 sum, len 함수를 사용하지 않습니다.
# 사용시 감점처리 되니 반드시 확인 바랍니다.
def calc_average(speed_list):
    Summ = 0        # 위반한 차 속도 값의 합
    count = 0       # 위반한 차 개수
    for speed in speed_list:    # 순회하며
        if speed > 100:     # 위반의 조건
            Summ += speed   # 합 계속 더하기
            count += 1      # 개수 증가
    average = Summ/count     # 평균
    return average
    # 여기에 코드를 작성하여 함수를 완성합니다.
    
    

# 아래 코드는 실행 확인을 위한 코드입니다.
if __name__ == '__main__':
    # 예시 코드는 수정하지 마세요.
    print(calc_average([119, 124, 178, 192,]))  #=> 153.25
    
    # 여기부터 아래에 추가 테스트를 위한 코드 작성 가능합니다.
    print(calc_average([10, 119, 124, 178, 192, 100]))
def is_id_valid(user_data):
    ID_PW = {}
    key = user_data['id']
    value = user_data['password']
    ID_PW[f'{key}'] = value
    try:
        if int(key[-1]) in list(range(10)):
            return True
    except ValueError:
        return False

    # 여기에 코드를 작성합니다.


if __name__ == '__main__':
    # 아래의 코드는 수정하지 않습니다.
    user_data1 = {
        'id': 'jungssafy5',
        'password': '1q2w3e4r',
    }
    print(is_id_valid(user_data1)) 
    # True
    
    user_data2 = {
        'id': 'kimssafy!',
        'password': '1q2w3e4r',
    }
    print(is_id_valid(user_data2)) 
    # False
    # 아래 부터 추가 예제 코드 작성 가능합니다.

    user_data3 = {
        'id': 'jungssafy',
        'password': '1q2w3e4r',
    }
    print(is_id_valid(user_data3))

    user_data4 = {
        'id': 'jungssafy5a5',
        'password': '1q2w3e4r',
    }
    print(is_id_valid(user_data4))

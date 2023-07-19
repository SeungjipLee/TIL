def func_name(parm1,parm2):
    return parm1 + parm2 #print와 return 잘 구분할 것
func_name(1, 2) # 함수를 호출한 것
# 함수를 호출하는 행위 -> 평가 후 값을 내는 표현식
print(func_name(1,2))  #3



# 모든 매개 변수에 키워드 인자 형식으로 값을 넘겼을 때
def greeting(name,age):
    print(f'안녕하세요, {name}님! {age}살이시군요!')

greeting(age=30, name='홍길동')



#scope 설명
age = 100

def parent_func(name):
    age = 30

    def child_func(child_name):
        global age
        age = 20
        print(age, 'child_func')
        
    child_func()
    print(age, 'parent_cunc')

parent_func()
print(age, 'global')


global_var = '글로벌 값'

def update_value(global_var):   # 매개 변수 -> local scope
    print(global_var, '매개 변수로 받은 값')
    result = global_var * 3     # 글로벌 변수가 가지고 있던 값 활용 가능
    global_var = '로컬 값'       # 글로벌 변수에 할당된 값에 영향 없이 다른 값 재할당 가능
    return result
print(update_value(global_var))


# 애초에 안되게 하지 왜 되게해서 헷갈리게 하나요?
# 1. 막아 놨습니다.
# 2. 코드 내가 씁니다. 규칙에만 맞춰서 잘 쓰면 편하게 쓸 수 있다.


# map_and_zip
def some_func(parm1):
    return parm1 ** 2

print(some_func(3))
print(some_func)

other_var = some_func
print(other_var(3))
numbers = [3, 6, 9]    # [9, 36, 81]

print(list(map(other_var, numbers)))


# map 함수를 쓸 때 변수가 하나면 오브젝트가 그대로 반환되고, 변수가 여러개면 언패킹 되는 건가?

def my_map(func,iterable):
    for item in iterable:
        result = func(item)
        print(result, end =' ')

my_map(some_func, numbers)
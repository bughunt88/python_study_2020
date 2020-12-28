
# 1. 파이썬 함수란?

# 파이썬 함수 및 중요성
# 파이썬 함수식 및 람다 (Lamda)

# 함수 정의 방법
# def funtion_name(parameter):
# code


# 예제1
def first_func(w):
    print("Hello, ", w )

word = "Goodboy"

first_func(word)

# 예제2

def return_func(w1):
    value  = "Hello, " + str(w1) 
    return value

x = return_func('goodboy2')

print(x)

# 예제3(다중반환)

def func_mul(x):
    y1  = x * 10
    y2  = x * 20
    y3  = x * 30
    return y1, y2, y3
# 파이썬에서 리턴할 떄 다중으로 넘겨 줄 수 있다

x, y, z = func_mul(10) 
# 자동으로 언패킹해서 리턴한다

print(x,y,z)


# 튜플 리턴

def func_mul2(x):
    y1  = x * 10
    y2  = x * 20
    y3  = x * 30
    return y1, y2, y3

q = func_mul2(20)

print(type(q), q)

# 패킹으로 묶어서 할 수 있다


# 리스트 리턴

def func_mul2(x):
    y1  = x * 10
    y2  = x * 20
    y3  = x * 30
    return [y1, y2, y3]


p = func_mul2(30)

print(type(p), p, set(q))


# 중요
# *args, **kwargs

# *args(언팩킹)
def args_func(*args): # 매개변수 명 자유
    for i, v in enumerate(args):
        print('result : '.format(i), v)
    print("----")


args_func('lee')
args_func('lee', 'park')
args_func('lee', 'park', 'kim')

# 값을 많이 보내면 알아서 자동으로 언패킹 해서 뿌려주는 함수

# **kwargs(언팩킹)
def kwargs_func(**kwargs): # 매개변수 명 자유
    for v in kwargs.keys():
        print("{}".format(v), kwargs[v])
    print("-----")


kwargs_func(name1='lee')
kwargs_func(name1='lee', name2='park')
kwargs_func(name1='lee', name2='park', name3='cho')

# 매개변수에 *은 튜플형식 **은 딕셔너리 일 때 많이 쓰인다


# 중첩함수

def nested_func(num):
    def func_in_func(num):
        print(num)
    print("in func")
    func_in_func(num+100)
nested_func(100)
# 함수안에 함수를 넣어서 쓸 수 있다


# 람다식 예제
# 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행 함수(heap 초기화) -> 메모리 초기화
# 남발 시 가독성 오히려 감소

# 기본 함수 설정
def xxx(x,y):
    return x*y

# 람다식 설정
lambda x, y:x*y

# 람다식은 함수로 담을 수 있다
lambda1 = lambda x, y:x*y





# 2. RMSE, MAE, R2 지표에 대하여



#RMSE : 평균 제곱근 오차 - MSE에 루트를 씌워 MSE의 큰 값을 줄여서 사용하는 측도이다. 정밀도를 표현하는데 적합하다.
#        오차가 커질수록 값이 증가하여 오차의 존재를 부각시킨다.


#MAE : 평균 절대 오차 - 이상치를 지닌 데이터가 많을 때 RMSE의 대안이 될 수 있다. (RMSE는 제곱을 하기 때문에 이상치를 지닌 데이터가 있으면 그 값이 커져서 차이가 벌어진다.)

#둘 다 값이 작으면 높은 품질의 모델을 나타낸다

#위 식은 성능을 정의하는 가장 적합한 값이라고 볼 수 있다.


#R2 : 결정 계수 - MSE / 데이터의 분산,  에러의 크기와 데이터의 분산(변화량)과의 비율

#결정 계수는 정확도를 판단하는데 자주 사용한다


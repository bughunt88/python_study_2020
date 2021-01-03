# 파이썬 클래스
# oop( 객체 지향 프로그래밍 ), self, 인스턴스 메소드, 인스턴스 변수

# 클래스 and 인스턴스 차이 이해
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 접근 가능, 공유
# 인스턴스 변수 : 객체 마다 별도 존재

# 객체와 인스턴스의 차이점은 면접에 많이 나온다!!!!!



# 예제1

class dog: # object 상속
    # 클래스 속성
    species = 'firstodg' # 클래스 변수

    # 초기화/인스턴스 속성
    def __init__(self,name,age):
        self.name = name
        self.age = age


# 클래스 정보

print(dog)

# 인스턴스화

a = dog('mikky',2) # 인스턴스 변수
b = dog('babt',3)

# 비교
print(a == b, id(a), id(b))
# 인스턴스화 시키면 id가 다르다

# 네임스페이스
print('dog1', a.__dict__)
print('dog2', b.__dict__)

print("##########")

#

if a.species == 'firstdog':
    print('{0} is a {1}'.format(a.name, a.species))


# 직접 접근할 수 있다. 공유한다

print(dog.species)
print(a.species)
print(b.species)


# 예제2
# self의 이해

class selfTest:
    def func1():
        print('func1 called')
# self가 없으면 클래스 메소드 - 사용하려면 클래스로 불러야 한다
    def func2(self):
        print('func1 called')
# self가 있다면 인스턴스 메소드 

f = selfTest()

# print(dir(f)) # 구조를 볼 수있다
print(id(f)) # id 확인한다 

# f.func1() # 예외

f.func2()

selfTest.func1()
selfTest.func2(f)


# 예제3
# 클래스 변수, 인스턴스 변수
class Warehouse:
    # 클래스 변수
    stock_num = 0 # 재고

    def __init__(self, name): # 생성자 
        # 인스턴스 변수 - self가 있어서 
        self.name = name
        Warehouse.stock_num +=1


    def __del__(self): # 소멸자
        Warehouse.stock_num -=1


user1 = Warehouse('lee')
user2 = Warehouse('cho')

print(Warehouse.stock_num)

print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print(Warehouse.__dict__)
print(user1.stock_num)



# 예제4

class dog: # object 상속
    # 클래스 속성
    species = 'firstodg' # 클래스 변수

    # 초기화/인스턴스 속성
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def info(self):
        return '{} is {} years old'.format(self.name, self.age)

    def speak(self, sound):
        return "{} says {}!".format(self.name, sound)



# dlstmxjstm todtjd

c = dog('july',4)
d = dog('marry',10)
# 메소드 호출
print(c.info())
# 메소드 호출
print(c.speak('wal wal'))
print(d.speak('mung mung'))



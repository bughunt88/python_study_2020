# 파이썬 튜플
# 리스트와 비교 중요
# 튜플 자료형(순서ㅇ, 중복ㅇ, 수정x, 삭제x) # 불변
# 한번 저장하면 변경이 불가능하다 중요한 데이터 리스트에 사용


# 선언

a = ()
b = (1,)
# 원소가 하나일 때는 ,를 찍어줘야 튜플로 선언 됨, ,없으면 인트형으로 지정

c = (70,75,80,85)
d = (100, 1000, 10000,'ace', 'base', 'captine')
e = (100, 1000, ('a', 'b', 'c'))

# 인덱싱
print(d[1])
# 값을 꺼내는거는 리스트랑 같은 방식으로 []으로 꺼낸다

print(d[1]+d[2])
print(e[-1])
print(e[-1][1])
print( list(e[-1][1]))

# 수정x
# d[0] = 1500


# 슬라이싱

print('d - ', d[0:3])
print('d - ', d[2:])
print('d - ', e[-1][1:3])

# 튜플 연산

print(c+d)
print(c*3)

# 튜플 함수
a = (5,2,3,1,4)
print(a)
print(a.index(3))
print(a.count(2))

# 팩킹 & 언팩킹  *** 튜플에서 중요한 개념

# 팩킹

t = ('foo', 'bar', 'baz', 'qux')

print(t)
print(t[0])
print(t[-1])

# 언팩킹1
(x1, x2, x3, x4) = t

print(type(x1),type(x2),type(x4),type(x4))
print(x1, x2, x3, x4)


# 팩킹 & 언팩킹
# 튜플은 () 없어서 지정 됨

t2 = 1,2,3
t3 = 4,

x1, x2, x3 = t2
x4, x5, x6 = (4, 5, 6)

print(t2)
print(t3)
print(x1, x2, x3)
print(x4, x5, x6)


# 팩킹은 값을 묶는 것
# 언팩킹은 풀어서 각각 위치에 맞는 변수로 값을 할당해준다


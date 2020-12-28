# 파이썬 딕셔너리
# 범용적으로 가장 많이 사용
# 딕셔너리 자료형(순서x, 키 중복x, 수정ㅇ, 삭제ㅇ)

# 선언
a = {'name' : 'kim', 'name' : 'lee'}
b = {0: 'hello python'}
c = {'arr': [1,2,3,4,5]}
d = {
    'name': 'niceman',
    'city': 'seoul',
    'age': 33,
    'grade': 'a',
    'status': True
}

e = dict([
 ('name', 'niceman'),
 ('city', 'seoul')
])

f = dict(
name = 'niceman',
city = 'seoul'
)
# 많은 양 있을 시 선호 

print(type(a), a)
print(type(b), b)
print(type(c), c)
print(type(d), d)
print(type(e), e)
print(type(f), f)

# 출력

print(a['name']) # 키가 존재 x -> 에러발생
print(a.get('name')) # 키가 존재 x -> none 처리


# 딕셔너리 추가

a['address'] = 'seoul'
print(a)

# 딕셔너리 길이 확인 len()


print(len(a))

print(a.keys())
print(b.keys())
print(c.keys())
print(d.keys())

# 딕셔너리 키 값만 가져오는 함수
print(list(a.keys()))
print(list(a.keys()))

# 딕셔너리 값 값만 가져오는 함수
print(a.values())
print(list(a.values()))

# 딕셔너리 둘다 가져오는 함수
print(a.items())
print(list(a.items()))

# pop도 가능 하나 꺼내고 리스트에서는 지워진다
print(a.pop('name'))
print(a)

# 랜덤으로 키와 값을 꺼내오고 리스트에서 지운다
print(f.popitem())
print(f)

# in 연산자를 이용해서 키 값이 있는지 찾을 수 있다
print('birth' in a)

# 수정

a['test'] = 'test_dict'
print(a)

a.update(birth='919191919')
print(a)

temp = {'address': 'busan'}

a.update(temp)

print(a)

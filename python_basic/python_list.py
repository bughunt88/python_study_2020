# 파이썬 리스트
# 자료구조에서 중요
# 리스트 자료형(순서ㅇ, 중복ㅇ, 수정ㅇ, 삭제ㅇ)

# 선언
a = []
b= list()
c = [70,75,80,85]

# len()은 배열의 사이즈 체크
print(len(c))

d = [100, 1000, 'ace', 'base', 'captine']
e = [100, 1000, ['a', 'b', 'c']]

print('d - ', type(d), d)
print('d - ', d[1])
print('d - ', d[1] + d[1] + d[0])
print('d - ', d[-1])
# 배열의 -값은 뒤에서 부터라고 나타낸다

print('d - ', e[-1][1])
# 배열안에 배열이 있으면 첫[]으로 배열 위치를 선택하고 다음 []으로 값의 위치를 지정한다

print('d - ', list(e[-1][1]))
# 리스트로 형변환 해주면 문자열 같은 경우 쪼개서 자동으로 리스트화 해준다


# 슬라이싱

print('d - ', d[0:3])
print('d - ', d[2:])
print('d - ', e[-1][1:3])



# 리스트 연산

print(c+d)

print(c*3)
# 리스트로 연산하면 리스트가 나온다

print("test" + str(c[0])) 
# 문자형과 리스트를 합치려면 리스트를 문자형으로 형변환 해줘야 한다

# 값 비교
print(c == c[:3] + c[3:])

# Identity (id)

temp = c
print(temp, c)
print(id(temp))
print(id(c))

# 변수로 만들어도 같은 아이디를 쓴다

c[0] = 100
print(c)

c[1:2] = ['a', 'b', 'c'] # [['a', 'b', 'c']]
c[1] =['a', 'b', 'c']

del c[2] # 삭제

# 리스트 함수

a = [5,2,3,1,4]

print(a)

a.append(10)
# 리스트의 끝 부분에 값을 넣는 함수
print(a)

a.sort()
# 리스트를 정렬하는 함수

a.reverse()
# 리스트를 역순으로 정렬하는 함수

a.insert(2, 7)
# 리스트 순서 정해서 값 넣는 함수

a.remove(10)
# 리스트안에 있는 값을 첮어서 지우는 함수

a.pop()
# 기존의 리스트에서 하나 꺼내오는 함수

a.count(4)
# 리스트에 내가 원하는 값이 몇 개 있는지 알려주는 함수

ex = [8,9]
a.extend(ex)
# 리스트에 값을 가장 마지막에 추가 함수

# 삭제 : remove, pop, del

# 반복문 활용

while a:
    data = a.pop()
    print(data)
    





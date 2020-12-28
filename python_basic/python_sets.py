# 집합(set) 특징
# 집합(set) 자료형(순서x, 중복x)

# 선언
a = set()
b = set([1,2,3,4])
c = set([1,2,'kim'])
d = {'foo', 'bar', 'baz'}
f = {42, 'foo', (1,2,3), 3.14}

print (type(a), a)
print (type(b), b)
print (type(c), c)
print (type(d), d)
print (type(f), f)

# 튜플 변환 (set -> tuple)

t = tuple(b)
print(type(t),t)
print(t[0], t[1:3])


# 리스트 변환 (set -> list)

l = list(c)
l2 = list(f)

print(l)
print(l2)

# 길이

print(len(a))
# len으로 길이 나타낼 수 있다



# 집합 자료형 활용

s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])



# 교집합
print(s1 & s2)
print(s1.intersection(s2))

# 합집합
print(s1|s2)
print(s1.union(s2))

# 차집합
print(s1-s2)
print(s1.difference(s2))


# 중복 원소 확인
print( s1.isdisjoint(s2) )
# 교집합이 있으면 flase로 나온다 없으면 true

# 부분 집합 확인
print(s1.issubset(s2))
print(s1.issuperset(s2))
# 부분 집합이 있으면 flase 이다 






# 추가 & 제거

s1 = set([1,2,3,4])

# 추가
s1.add(5)
print(s1)

# 지우기
s1.remove(2)
print(s1)
# 없는 원소는 지울 수 없다

# 지우기 (에러 없이 나오도록 하는 함수)
s1.discard(3)
print(s1)
s1.discard(7)

# 전부 지우기
s1.clear


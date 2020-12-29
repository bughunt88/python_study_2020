# 파이썬 제어문
# if 실습

# 기본 형식
print(type(True)) # 0이 아닌 수, "abc", [1,2,3...], (1,2,3...) ...
print(type(False)) # 0, "", [], (), {}..datetime A combination of a date and a time. Attributes: ()

# 예1

if True:
    print('good')


if False:
    print('bad')


# 예2 (if else 구문)

if False:
    print('bad')
else:
    print('good')


# 관계 연산자 
# >, >=, <, <=, ==, !=
x = 15
y = 10

# 양 변이 같은 경우 참
print(x == y)

# 양 변이 다를 때 참
print(x != y)

# 왼쪽이 클 때 참
print(x > y)

# 왼족이 크거나 같을 떄 참
print(x >=y )

# 오른쪽이 클 때 참
print(x < y)

# 오른쪽이 크거나 같을 때 참
print(x <= y)

# 예3
city = ""
if city:
    print("you are in : ", city)
else:
    print("plz enter your city")


# 예4
city = "서울"
if city:
    print("you are in : ", city)
else:
    print("plz enter your city")



# 논리연산자(중요)
# and, or, not

a = 75
b = 40
c = 10

print('and : ', a > b and b > c) # a > b > c
print('or:', a > b or b > c)
print('not', not b > c)

print(not True)
print(not False)


# 산술, 관계, 논리 우선순위
# 산술 > 관계 > 논리
print('e1 : ', 3+12 > 7+3)
print('e2 : ', 5+10*3 > 7+3*20)
print('e3 : ', 5+10 > 3 and 7 + 3 == 10)
print('e3 : ', 5+10 > 3 and not 7 + 3 == 10)


socre1 = 90
socre2 = 'A'

# 복수의 조건이 모두 참일 경우에 실행
if socre1 >= 90 and socre2 == 'A':
    print('pass')
else:
    print('fail')


# 예5
id1 = 'vip'
id2 = 'admin'
grade = 'platinum'

if id1 == 'vip' or id2 == 'admin':
    print('관리자 입장')

if id2 == 'admin' and grade == 'platinum':
    print('최상위 관리자')


# 예6
# 다중조건문

num = 90

if num >= 90:
    print("a")
elif num >=80:
    print("b")
elif num >=70:
    print("c")
else:
    ("과락")



# 중첩 조건문

grade = 'A'
total = 95

if grade =='a':
    if total > 90:
        print('장학금 100')
    elif total > 80:
        print('장학금 90')
    else:
        print("없음")
else:
    print("재시험")


# in, not in

q = [10,20,30]
w = {70,80,90,100}
e = {"nema": "lee", "city":"seoul", "grade": "a"}
r = (10,12,14)

print(15 in q)
print(90 in w)
print(12 not in r)
print("name" in e)
print("seoul" in e.values())
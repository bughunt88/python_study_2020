# 파이썬 반복문
# FOR 실습


# 코딩의 핵심
# for in <collection>
#      <Loop body>

for v1 in range(10): # 0~9
    print(v1)

print()

for v2 in range(1,11): # 1~10
    print(v2)

print()

# 2의 배수
for v3 in range(1,11,2):
    print(v3)


# 1 ~ 1000 합

sum1 = 0

for v in range(1,1001):
    sum1 += v

print('1 ~ 1000 Sum : ', sum1)

print('1 ~ 1000 sum : ', sum(range(1,1001)))


# Iterables 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전(딕셔너리)
# iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip

# 예제1
names = ['kim', 'park', 'cho', 'um' ]

for n in names:
    print(n)


# 예제2

lotto_numbers = [11, 19, 21, 28, 36, 37]

for n in lotto_numbers:
    print(n)


word = "beautiful"


# 예제3

for s in word:
    print(s)



# 예제4

my_info = {

    "name": 'lee',
    "age": 33

}

for key in my_info:
    print(my_info[key])

for v in my_info.values():
    print(v)


# 예제5

name = 'FineAppLE'

for n in name:
    if n.isupper(): # 대문자 확인 코드
        print(n)
    else:
        print(n.upper())



# break

numbers = [14,3,4,7,10,24,17,2,33,15,30,34,36,38]

for num in numbers:
    if num == 34:
        print("find")
        break
    else:
        print("num")


# continue : for 진행 중 넘겨버리는 코드

it = ["1",2,5,True, 4.3, complex(4)]

for v in it:
    if type(v) is bool:
        continue
    print(type(v))



# for - else  
# for가 다 돌고 이상이 없으면 else 구문이 나오도록 한다 (break가 없으면 실행된다)

numbers = [14,3,4,7,10,24,17,2,33,15,34,36,38]

for num in numbers:
    if num == 24:
        print("found 24")
        break
else:
    print('not found : 24')


# 구구단 출력

for n in range(2,10):
    for n1 in range(1,10):
       print('{:4d}'.format(n*n1), end='')
    print()
    
     
# 파이썬 반복문
# while 실습


# while <expr>:
#    <statement(s)>



# 예제1

n = 5
while n > 0:
    print(n)
    n = n - 1

# while은 무한하게 돌아간다

# 예제2

a=['foo','bar','baz']

while a:
    print(a.pop())
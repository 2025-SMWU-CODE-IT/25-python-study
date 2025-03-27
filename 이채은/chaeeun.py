print("Hello World!")

A, B = map(int,input('0<A,B<10인 두 정수를 입력하시오').split())
print(A+B)

A, B = map(int,input('0<A,B<10인 두 정수를 입력하시오').split())
print(A-B)

A, B = map(int,input('0<A,B<10인 두 정수를 입력하시오').split())
print(A*B)

A, B = map(float,input('0<A,B<10인 두 정수를 입력하시오').split())
print(A/B)

A, B = map(int,input('1<=A, B<=10,000인 두 정수를 입력하시오').split())
print(A+B)
print(A-B)
print(A*B)
print(A/B)
print(A%B)

a=('joonas', 'baekjoon')
b=str(input())
if b in a:
    print(b,'??!')
else:
    pass
#3주차 과제 

#문제 번호: 2557 "Hello World"
print("Hello World!")

#문제 번호: 1000 A+B
a, b = input("0과 10 사이의 숫자 두 개를 입력하세요").split()
a = int(a)
b = int(b)

print(a+b)

#문제 번호: 1001 A-B
a, b = input("0과 10 사이의 숫자 두 개를 입력하세요").split()
a = int(a)
b = int(b) 

print(a-b)

#문제 번호: 10998 A*B
a, b = input("0과 10 사이의 숫자 두 개를 입력하세요").split()
a = int(a)
b = int(b)

print(a*b)

#문제 번호: 1008 A/B
a, b = input("0과 10 사이의 숫자 두 개를 입력하세요").split()
a = int(a)
b = int(b)

print(a/b)

#문제 번호:10869 사칙연산
aa, b = input("0과 10,000 사이의 숫자 두 개를 입력하세요").split()
a = int(a)
b = int(b)

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
 
 #문제 번호: 10926 ??!
nickname = input("아이디를 입력하세요")
print(nickname + "??!")

#문제 번호: 18108 1998년생이 내가 태국에서는 2541년생?
year = int(input("태국 년도를 알고 싶은 년도를 입력하세요"))
print(year + 543)

#문제 번호:10430 나머지
a, b, c = input("숫자 3개를 입력하세요").split(' ' , 3)
a = int(a)
b = int(b)
c = int(c)

print("(a+b)%c = ", (a+b)%c)
print("(a%c +b%c) = ", (a%c +b%c))
print("(axb)%c = ", (a*b)%c)
print("(a%c)*(b%c) = ", (a%c)*(b%c))

#문제 번호:2588 곱셈
a = int(input("숫자를 입력하세요"))
b = int(input("곱할 숫자를 입력하세요"))

b_100 = b // 100
b_10 = (b%100) // 10
b_1 = ((b%100)%10) 

print(a * b_1)
print(a * b_10)
print(a * b_100)

print(100*a*b_100 + 10*a*b_10+ a*b_1)

#문제번호: 11382 꼬마정민
a, b, c = input("숫자 3개를 입력하세요").split(' ' ,3)
a = int(a)
b = int(b)
c = int(c)

print(a+b+c)

#문제번호: 10171 고양이
print("\    /\ \n)  ( ')\n(  /  )\n\(__)|\n")

#문제번호:

dog = '''
|\\_/|
|q p|   /}
( 0 )"""\\
|"^"`    |
||_/=\\\__|
'''

print(dog)
#문제번호 : 2557 Hello World
print("Hello World!")
#문제번호 : 1000 A+B
a,b = map(int,input('0과10사이의 숫자를 두 개 입력하세요 :').split())
print(a+b)
#문제번호 : 1001 A-B
a,b = map(int,input('0과10사이의 숫자를 두 개 입력하세요 :').split())
print(a-b)
#문제번호 : 10998 AxB
a,b = map(int,input('0과10사이의 숫자를 두 개 입력하세요 :').split())
print(a*b)
#문제번호 : 1008 A/B
a,b = map(int,input('0과10사이의 숫자를 두 개 입력하세요 :').split())
print(a/b)
#문제번호 : 10869 사칙연산
a,b = map(int,input('1보다 같거나 크고 10000보다 작거나 같은 숫자를 두 개 입력하세요 :').split())
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
#문제번호 : 10926 ??!
a = input('아이디를 입력하세요 : ')
print(a+'??!')
#문제번호 : 18108 1998년생인 내가 태국에서는는 2541년생?!
a = input('불기연도를 입력하세요 : ')
a = int(a)
print(a-543)
#문제번호 : 10430 나머지
a,b,c = map(int,input('2보다 같거나 크고 10000보다 같거나 작은 숫자를 3개 입력하세요 :').split())
print((a+b)%c)
print(((a%c)+(b%c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)
#문제번호 : 2588 곱셈
a = input('세 자리 자연수를 입력하세요 :')
a = int(a)
b = input('세 자리 자연수를 입력하세요 :')
b = int(b)
mylist = []
for i in str(b) : 
    mylist.append(i)
mylist = list(map(int,mylist))
print(a*mylist[2])
print(a*mylist[1])
print(a*mylist[0])
print(a*b)
#문제번호 : 11382 꼬마정민
a,b,c = map(int,input('1보다 같거나 크고 10의12제곱보다 같거나 작은 숫자를 세 개 입력하세요 :').split())
print(a+b+c)
#문제번호 : 10171 고양이
a = '''\    /\\
 )  ( ')
(  /  )
 \(__)|'''
print(a)
#문제번호 : 10172 개
b = '''|\_/|
|q p|   /}
( 0 )"""\\
|"^"`    |
||_/=\\\\__|'''
print(b)

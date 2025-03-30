#2주차 과제

#문제번호:2557 (Hello World!를 출력하시오)
print("Hello world!")

#문제번호:1000 (두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.)
A=int(input('1이상 10이하의 정수를 입력하세요.'))
B=int(input('1이상 10이하의 정수를 입력하세요.'))
print(A+B)

#문제번호:1001 (두 정수 A와 B를 입력받은 다음, A-B를 출력하는 프로그램을 작성하시오.)
A=int(input('1이상 10이하의 정수를 입력하세요.'))
B=int(input('1이상 10이하의 정수를 입력하세요.'))
print(A-B)

#문제번호:10998 (두 정수 A와 B를 입력받은 다음, A×B를 출력하는 프로그램을 작성하시오.)
A=int(input('1이상 10이하의 정수를 입력하세요.'))
B=int(input('1이상 10이하의 정수를 입력하세요.'))
print(A*B)

#문제번호:1008(두 정수 A와 B를 입력받은 다음, A/B를 출력하는 프로그램을 작성하시오.)
A=int(input('1이상 10이하의 정수를 입력하세요.'))
B=int(input('1이상 10이하의 정수를 입력하세요.'))
print(A/B)

#문제번호:10869 (두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오. )
A=int(input('1이상 10000이하 자연수를 입력하세요.'))
B=int(input('1이상 10000이하 자연수를 입력하세요.'))
print(A+B)
print(A-B)
print(A*B)
print(A/B)
print(A%B)

#문제번호:10926 (준하가 가입하려고 하는 사이트에 이미 존재하는 아이디가 주어졌을 때, 놀람 표현하는 프로그램을 작성하시오.)
id=input("아이디를 입력하세요:")
print(id+'??!')

#문제번호:18108 (불기 연도가 주어질 때 이를 서기 연도로 바꿔 주는 프로그램을 작성하시오.)
Thailand_year=int(input('불기 연도를 입력하세요.'))
Korea_year=(Thailand_year-546)
print(Korea_year)

#문제번호:10430(나머지)
A,B,C=(input("2이상 10000이하의 숫자를 공백을 두고 입력하세요.")).split()
A=int(A)
B=int(B)
C=int(C)

print((A+B)%C)
print(((A%C)+(B%C))%C)
print((A*B)%C)
print(((A%B)*(B%C))%C)

#문제:2588 (곱셈)
a,b=input("세 자리 자연수를 공백을 두고 입력하시오.").split()
position3=int(a)*int(b[-1])
position4=int(a)*int(b[1])
position5=int(a)*int(b[0])
position6=position3+(position4)*10+(position5)*100

print(position3)
print(position4)
print(position5)
print(position6)

#문제:11382 (꼬마 정민)
A,B,C=input("1이상 10^12이하의 자연수를 공백을 두고 입력하세요.").split()
A=int(A)
B=int(B)
C=int(C)
print(A+B+C)

#문제:10171 (고양이)
a="\\    /\\"
b=" )  ( ')"
c="(  /  )"
d=" \(__)|"

print(a + "\n" + b + "\n" + c + "\n" + d)

#문제:10172 (개)
a='|\_/|'
b='|q p|   /}'
c='( 0 )"""\\'
d='|"^"`    |'
e='||_/=\\__|'

print(a + "\n" + b + "\n" + c + "\n" + d + "\n" + e)
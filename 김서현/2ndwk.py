#2557번, Hello World : Hello World! 출력하기 
print("Hello World!")

#1000번, A+B : 변수 A+B 출력하기
A,B = map(int, input().split())
print(A+B)

#1001번, A-B : 변수 A-B 출력하기
A,B = map(int, input().split())
print(A-B)

#10998번, AXB : 변수 A*B 출력하기
A,B = map(int, input().split())
print(A*B)

#1008번, A/B : 변수 A/B 출력하기 (floating number)
A,B = map(int, input().split())
print(A/B)

#10869번, 사칙연산 : 사칙연산 출력력하기
A,B = map(int, input().split())
print(A+B)
print(A-B)
print(A*B)
print(A//B)
print(A%B)

#10926번, ??! : ??! 붙여서 출력하기
x = input()
print(x + '??!')

#18108번, 1998년생인 내가 태국에서는 2541년생?! : 연도 바꿔 출력하기 (계산)

y = int(input())
x = y - 543
print(x)

#10430번, 나머지 : 3가지 변수로 계산하기 (나머지)

A, B, C = map(int, input().split())
print((A+B)%C)
print(((A%C)+(B%C))%C)
print((A*B)%C)
print(((A%C)*(B%C))%C)

#2588번, 곱셉 : 곱셈 단계별로하기

A = int(input())
B = input()
print(A*int(B[2]))
print(A*int(B[1]))
print(A*int(B[0]))
print(A*int(B))

#11382번, 꼬마 정민 : 3가지 변수 더하기기

A, B, C = map(int, input().split())
print(A+B+C)

#10171번, 고양이 : 고양이 출력하기 

print("\\    /\\")
print(" )  ( ')")
print("(  /  )")
print (" \\(__)|")

#10172번, 개 : 강아지 출력하기

print ("|\\_/|")
print("|q p|   /}")
print('( 0 )"""\\')
print('|"^"`    |')
print("||_/=\\\\__|")
#문제번호 : 27866 문자와 문자열
S = input("영어 소문자와 대문자로만 이루어진 단어를 입력하세요 : ")
i = int(input("1보다 큰 정수를 입력하세요 : "))
print(S[i-1]) 
#문제번호 : 2743 단어 길이 재기
word = input("영어 소문자와 대문자로만 이루어진 단어를 입력하세요 : ")
print(len(word))
#문제번호 : 11654 아스키 코드
word = input("알파벳 소문자, 대문자, 숫자0-9중 하나를 입력하세요 : ")
print(ord(word))
#문제번호 : 2908 상수
a,b = input("0이 포함되지 않은 같지 않은 세 자리 수를 두 개 입력하세요 : ").split()
A = int(a[2] + a[1] + a[0])
B = int(b[2] + b[1] + b[0])
if A > B : 
    print(A)
else:
    print(B)
#문제번호 : 1330 두 수 비교하기
a,b = input("두 정수를 입력하세요 : ").split()
a = int(a)
b = int(b)
if a > b :
    print('>')
elif a < b :
    print('<')
else :
    print('==')
#문제번호 : 9498 시험 성적
grade = int(input("시험 성적을 입력하세요 : "))
if 90 <= grade <= 100 :
    print('A')
elif 80 <= grade <= 89 :
    print('B')
elif 70 <= grade <= 79 :
    print('C')
elif 60 <= grade <= 69 :
    print('D')
else :
    print('F')
#문제번호 : 2884 알람 시계
H,M = input("설정한 알람 시간을 입력하세요 : ").split()
H = int(H)
M = int(M)
if M >= 45 :
    print(H,M-45)
else :
    if H == 0 :
        print(23,60 - (45-M))
    else :
        print(H-1,60 - (45-M))
#문제번호 : 10988 팰린드롬인지 확인하기
palin = input("팰린드롬인지 확인하고 싶은 단어를 입력하세요 : ")
listpalin = []
for i in palin :
    listpalin.append(i)
listdrome = listpalin[:]
listdrome.reverse()
if listpalin == listdrome :
    print(1)
else :
    print(0)
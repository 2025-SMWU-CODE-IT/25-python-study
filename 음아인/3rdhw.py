#문제:27866 (문자와 문자열)
a = input("단어를 입력하시오")
b = int(input("몇번째 글자를 출력하고 싶은가요"))
print(a[int(b-1)])

#문제:2743 (단어 길이 재기)
a = input("단어를 입력하세요.")
print(len(a))

#문제:11645 (아스키 코드)
a = input("숫자를 입력하시오.")
print(ord(a))

#문제:2908 (상수)
a = input("첫번째 세자리수를 입력하세요.")
b = input("두번째 세자리수를 입력하세요.")
a = int(a)
b = int(b)

a_hundred = a // 100
a_ten = (a//10) % 10
a_one = a % 10
a_changed = (a_hundred) + (a_ten * 10) + (a_one * 100)

b_hundred = b // 100
b_ten = (b//10) % 10
b_one = b % 10
b_changed = (b_hundred) + (b_ten * 10) + (b_one * 100)

if a_changed > b_changed :
    print(a_changed)
else :
    print(b_changed)

#문제:1330 (두 수 비교하기)
a,b = input("비교할 두 수를 공백을 두고 입력하시오").split( )
a = int(a)
b = int(b)

if a > b:
    print(">")
elif a < b:
    print("<")
else :
    print("==")

#문제: 9498(시험성적)
score = input("시험점수를 입력하세요")
score = int(score)

if 90 <= score <= 100:
    print("A")
elif 80 <= score <= 89:
    print("B")
elif 70 <= score <= 79:
    print("C")
elif 60 <= score <= 69:
    print("D")
else :
    print("F")
    

#문제:2884(알람시계)
H = input("현재 몇시인지 입력하세요")
M = input("현재 몇분인지 입력하세요")
H = int(H)
M = int(M)

if M>= 45:
    M = M-45
elif H == 0:
    H ==23
    M = M + 60 - 45
else :
    H = H -1
    M = M + 60 - 45

print(H,M)

#문제:10988(팰린드롬인지 확인하기)
a = input("단어를 입력하세요")
reversed_a = a[::-1]
if a == reversed_a :
    print("팰린드롬 단어입니다")
else :
    print("팰린드롬 단어가 아닙니다")
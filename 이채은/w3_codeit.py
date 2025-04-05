#27866번 문자열
a = input()
b = int(input())
print(a[b-1])

#2743 단어 길이 재기
a = input()
print(len(a))

#11654 아스키 코드
a = input()
print(ord(a))

#2908 상수
a = int(input())
b = int(input())
c = (a%10)*100+((a%100)//10)*10+(a//100)
d = (b%10)*100+((b%100)//10)*10+(b//100)
if c > d :
    print(c)
else :
    print(d)

#1330 두 수 비교하기
a = int(input())
b = int(input())
if a > b:
    print('>')
elif a = b:
    print('=')
else:
    print('<')

#9498 시험 성적
a = int(input())
if 90 <= a <=100:
    print('A')
elif 80 <= a <= 89:
    print('B')
elif 70 <= a <= 79:
    print('C')
elif 60 <= a <= 69:
    print('D')
else:
    print('F')

#2884 알람 시계
a = input('시')
b = input('분')
if b >= 45:
    print(a,'시',b-45,'분')
else:
    print(a-1'시',b+60-45,'분')

#10988 팰린드롬인지 확인하기
a = input()
b = a[::-1]
if a == b:
    print(1)
else:
    print(0)
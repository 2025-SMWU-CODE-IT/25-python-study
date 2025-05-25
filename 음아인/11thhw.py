#문제: 9610번(사분면)
n = int(input())
# 초기값을 설정해줍니다.
q1 = 0
q2 = 0
q3 = 0
q4 = 0
axis = 0
# 좌표를 점의 수만큼 반복해서 입력받습니다. 
for i in range(n):
    xy = input().split()
    x = int(xy[0])
    y = int(xy[1])
 # 축 위에 있는 점인지 확인합니다.
    if x == 0 or y == 0:
        axis = axis + 1
# Q1확인
    elif x > 0 and y > 0:
        q1 = q1 + 1
# Q2확인
    elif x < 0 and y > 0:
        q2 = q2 + 1
# Q3확인
    elif x < 0 and y < 0:
        q3 = q3 + 1
# Q4확인
    elif x > 0 and y < 0:
        q4 = q4 + 1
#결과를 출력합니다. 
print("Q1:", q1)
print("Q2:", q2)
print("Q3:", q3)
print("Q4:", q4)
print("AXIS:", axis)

#문제: 2163번(초콜릿 자르기)
# 초콜릿 크기를 입력받습니다
n, m = input().split()
n = int(n)
m = int(m)
# 최소로 쪼개야 하는 방법입니다.
count = (n * m) - 1
# 결과를 프린트해줍니다. 
print(count)

#문제: 2530번(인공지능 시계)
# 몇시, 몇분, 몇초인지 입력받습니다. 
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
# 몇초동안 요리해야하는지 입력받습니다. 
d = int(input())
# 토탈이 얼마인지 계산해줍니다. 
total = a * 3600 + b * 60 + c
# 추가로 요리한 시간을 더해줍니다. 
total = total + d
# 나머지를 계산해줍니다. 
total = total % (24 * 3600)
# 시간을 변환해줍니다.
hour = total // 3600
total = total % 3600
minute = total // 60
second = total % 60
print(hour, minute, second)

#문제: 2480번(주사위 세개)
# 주사위 3를 입력받습니다.
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
# 3개의 숫자가 같을때
if a == b and b == c:
    prize = 10000 + a * 1000
# 2개의 숫자가 같을때 
elif a == b or a == c:
    prize = 1000 + a * 1000
elif b == c:
    prize = 1000 + b * 1000
#전부 다를때
else:
    max_value = a
    if b > max_value:
        max_value = b
    if c > max_value:
        max_value = c
    prize = max_value * 100
# 상금이 얼마인지 출력해줍니다. 
print(prize)

#문제: 7567번(그릇)
# 문자열을 입력받습니다. 
s = input()
# 시작높이를 지정해줍니다. 
height = 10
# 앞에 글자를 기억해줍니다. 
before = s[0]
# 2번째 글자부터 보기 시작합니다. 
for i in range(1, len(s)):
    now = s[i]
    if now == before:
        height = height + 5
    else:
        height = height + 10
    before = now  
# 높이를 출력해줍니다. 
print(height)

#문제: 11557번(Yangjojang of The Year)
# 테스트 케이스 개수를 입력받습니다. 
t = int(input())
# 테스트 케이스 만큼 반복해줍니다. 
for _ in range(t):
    n = int(input())  # 학교 수 입니다. 
    max_school = ""   # 술 제일 많이 마신 학교 이름입니다. 
    max_alcohol = 0   # 제일 많이 마신 양입니다 
# 학교 개수만큼 입력받습니다. 반복입니다. 
    for i in range(n):
        line = input().split()
        school = line[0]
        alcohol = int(line[1])
        if alcohol > max_alcohol:
            max_alcohol = alcohol
            max_school = school
# 결과를 출력합니다. 
    print(max_school)
#[2514303김민주] 11주차 과제

#9610 사분면 
AXIS = 0
Q1 = 0
Q2 = 0
Q3 = 0
Q4 = 0

n = int(input())

for i in range(n):
   x, y = [int(n) for n in input().split()]
   
   if x > 0 and y > 0:
      Q1 = Q1 + 1
   elif x < 0 and y > 0:
      Q2 = Q2 + 1
   elif x < 0 and y < 0:
      Q3 = Q3 + 1
   elif x > 0 and y <0:
      Q4 = Q4 + 1
   else:
      AXIS = AXIS + 1

print("Q1:", Q1)
print("Q2:", Q2)
print("Q3:", Q3)
print("Q4:", Q4)
print("AXIS:", AXIS)


#2163, 초콜릿 자르기
N, M = [int(n) for n in input().split()]

result = (N-1) + (M-1)*N
print(result)

#2530, 인공지능 시계

#시A, 분B, 초C, 요리시간D
A, B, C = [int(n) for n in input().split()]
D = int(input())

#모두 초(s)로 변환
T = A * 3600 + B * 60 + C + D

#하루는 86400초, 만약, 86400초를 넘어가면 24시를 넘어가는 거니깐 빼주기.
if T >= 86400:
   T = T - 86400*(T//86400)


A = T // 3600
B = (T - A * 3600) // 60
C = T - A*3600 - B*60

print(A, B, C)

#2480, 주사위 세개
a, b, c = [int(n) for n in input().split()]

if a == b == c:
    reward = 10000 + a * 1000
elif a == b or a == c:
    reward = 1000 + a * 100
elif b == c:
    reward = 1000 + b * 100
else:
    max = a #가장 큰 값 확인
    if b > max:
        max = b
    if c > max:
        max = c
    reward = max * 100

print(reward)

#7567, 그릇

# 입력 받기
brackets = input()

# 첫 번째 그릇은 항상 10cm
height = 10

# 두 번째 그릇부터 비교하면서 높이 계산
for i in range(1, len(brackets)):
    if brackets[i] == brackets[i - 1]:
        height += 5
    else:
        height += 10

print(height)

#11557 Yangjojang of The Year
T = int(input())

for _ in range(T):
    N = int(input())  # 학교 수

    max_school = ""
    max_drink = -1 

    for _ in range(N):
        entry = input().split()
        name = entry[0]
        drink = int(entry[1])

        if drink > max_drink:
            max_drink = drink
            max_school = name

    print(max_school)

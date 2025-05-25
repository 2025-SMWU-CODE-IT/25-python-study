#[2514303김민주] 11주차 과제

#9610 사분면 
AXIS = 0
Q1 = 0
Q2 = 0
Q3 = 0
Q4 = 0

n = int(input())

for i in range(n):
   x_str, y_str = input().split()
   x = int(x_str)
   y = int(y_str)
   
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
N_str, M_str = input().split()
N = int(N_str)
M = int(M_str)

result = (N-1) + (M-1)*N
print(result)

#2530, 인공지능 시계

#시A, 분B, 초C, 요리시간D
A_str, B_str, C_str = input().split()
A = int(A_str)
B = int(B_str)
C = int(C_str)
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
a_str, b_str, c_str = input().split()
a = int(a_str)
b = int(b_str)
c = int(c_str)

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
        name, drink_str = input().split()
        drink = int(drink_str)

        if drink > max_drink:
            max_drink = drink
            max_school = name

    print(max_school)

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
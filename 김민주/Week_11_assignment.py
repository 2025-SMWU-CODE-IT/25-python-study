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

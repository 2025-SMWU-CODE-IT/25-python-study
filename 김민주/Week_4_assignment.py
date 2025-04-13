#4주차 과제
#[김민주] 2025년 1학기 python study - 4주차

#2739
N = int(input())

for i in range(1, 10):
    print("{0} * {1} = {2}".format(N, i, N*i))

#25304
X = int(input())
N = int(input())
plus = 0

for i in range(N):
    a, b = input().split()
    plus = plus + int(a) * int(b) 

if plus == X:
    print("Yes")
else:
    print("No")

#2439
N = int(input())

for i in range(1, N+1):
    print("{0:>{1}}".format("*"*i, N)) 

#10807
n = int(input())
N = [int(n) for n in input().split()]
v = int(input())

print(N.count(v))

#2562
number = []
for i in range(9):
    x = input()
    number.append(int(x))

max = max(number)

print(max)
print(number.index(max)+1)
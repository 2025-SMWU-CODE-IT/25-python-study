#2739 구구단
N = int(input())
for i in range(9):
    print(N,'*',i+1,'=',N*(i+1))

#25304 영수증
X = int(input())
N = int(input())
sum = 0
for i in range(N):
    a,b = [int(n) for n in input().split()]
    sum += a*b
if sum == X:
    print('Yes')
else:
    print('No')

#2439 별찍기
N = int(input())
for i in range(N):
    print(' '*(N-(i+1)),end='')
    print('*'*(i+1),end='')
    print()

#10807 개수 세기
N = int(input())
a = [int(n) for n in input().split()]
V = int(input())
s = 0
for i in a:
    if V == i:
        s += 1
print(s)

#2562 최댓값
a = []
for i in range(9):
    b = int(input())
    a.append(b)
c = max(a)
d = a.index(c)
print(c)
print(d+1)
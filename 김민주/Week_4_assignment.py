#4주차 과제
#[김민주] 2025년 1학기 python study - 4주차

#2739
N = int(input())

for i in range(1, 10):
#구구단은 보통 0부터 시작하지 않으니, 시작 범위를 지정. 시작범위는 10과 다르게 포함됨
    print("{0} * {1} = {2}".format(N, i, N*i))
    #포맷팅을 이용한 출력

#25304
X = int(input())
N = int(input()) 
plus = 0

for i in range(N):
    a, b = input().split()
    plus = plus + int(a) * int(b) 
    #사용자가 입력한 a(상품 가격) b(상품 개수)를 곱하면 특정 상품의 액수가 나옴. 다 더하면 실질적으로 산 상품의 총 액수.

if plus == X:
#실질적으로 산 총 액수와 영수증에 나타난 총 액수를 비교해야함.
    print("Yes")
else:
    print("No")

#2439
N = int(input())

for i in range(1, N+1):
    print("{0:>{1}}".format("*"*i, N))
    #문제에서 요구한 오른쪽 정렬을 위해 format을 씀.

#10807
n = int(input()) 
#실질적으로 N안의 n에게 영향은 없음, 정수의 개수를 나타내기 위한 input
N = [int(n) for n in input().split()]
v = int(input())

print(N.count(v))
#N이란 리스트 안에 v가 나온 것을 세어주고 출력하기 위해 씀씀

#2562
number = [] 
#input받은 것을 리스트로 만들기 위한 빈 리스트

for i in range(9):
    x = input()
    number.append(int(x)) 
    #x에서 받은 input을 int 형태로 리스트 number에 추가

maxi = max(number)
#number 리스트에서 가장 최대값 반환, index를 쓰기 위해 먼저 최대값을 maxi에 저장함. 

print(maxi)
print(number.index(maxi) + 1)
#number에서 maxi와 같은 값의 위치 찾아줌. 인덱스 세기 때문에 찾아서 + 1 해서 출력
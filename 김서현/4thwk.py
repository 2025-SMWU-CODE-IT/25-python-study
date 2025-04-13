#2739번 구구단 
#n을 입력 받아 구구단 출력 
n = int(input())
for i in range(1, 10): #구구단이므로 범위를 9개만 출력되도록 설정한다.
    print(n , '*', i, '=', n*i) 

#25304번 영수증
#영수증 총 금액이 그의 합계와 맞는지 확인해 본다.
X = int(input())
N = int(input())
sum = 0 #sum을 설정해 전체 합과 비교할 합계 변수를 초기화한다.
for i in range(N): 
    price, number = [int(n) for n in input().split()] #가격과 개수를 입력받고 스플릿 해 정수로 바꾼다.
    sum += price*number #sum에 더할 숫자를 계산한다.

if X == sum : #sum과 합계를 비교해 yes 또는 no를 출력한다.
    print("Yes")
else : print("No")


#2439번 별찍기
#별을 오른쪽 정렬하여 피라미드 형태로 출력한다.
N = int(input()) 
for i in range(1,N+1): #범위를 1에서 N+1까지 해야 n개의 숫자가 출력되므로 저렇게 설정한다.
    x = str('*'*i) #문자열끼리 이어붙이는 것이므로 스트링 함수를 사용해 별을 i개 뽑는다.
    print(x.rjust(N)) #오른쪽 정렬을 이용해 x를 프린트한다. 


#10807번 개수 세기
#n개 정수 중에 정수 v의 개수 세기 
N = int(input()) 
nums = [int(n) for n in input().split()] #처음에 입력된 N으로 리스트를 만든다. 모든 숫자를 입력했기 때문에 스플릿을 쓴다.
v = int(input())
count = nums.count(v) #v를 입력했을 때 그의 수를 계산한다.
print(count)


#2562번 최댓값
#9개 수 입력 후 최댓값과 그 순서 구하기
numbers = [int(input()) for i in range(9) ] #입력된 변수를 정수로 바꾸고 9개의 숫자를 리스트로 출력한다.

a = max(numbers) #리스트 내의 가장 큰 수를 찾는다.
b = numbers.index(a)+1 #해당 숫자의 인덱스를 확인한다(순서가 0부터시작하므로 +1을 한다. )
print(a)
print(b)
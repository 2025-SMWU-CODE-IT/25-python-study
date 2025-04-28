#2739 구구단
N = int(input("N을 입력하세요(단,1<=N<=9): "))
#주어진 n에 대해서 1~9를 곱한 값을 출력해야 하므로 범위를 설정한 for문을 사용한다.
for i in range(1,10) :
    print(N,"*",i,"=",N*i)

#25304 영수증
total = int(input("영수증에 적힌 총 금액을 입력하세요 : "))
N = int(input("영수증에 적힌 구매한 물건 종류의 수를 입력하세요 : "))
i = 0
#물건의 가격과 수를 리스트로 받은 다음에 인덱스를 활용해 곱하기 위해서 빈 리스트를 만든다.
anfrjs = []
#물건 종류의 수를 입력 받으므로 해당 수만큼 입력을 반복하기 위해서 while문을 사용한다.
while i < N :
    anfrjs.extend([int(n) for n in input("각 물건의 가격과 개수를 공백을 두고 입력하세요 : ").split()])
    i = i + 1
j = 0 
sum = 0
#물건 종류의 수만큼 덧셈을 반복하기 위해서 while문을 사용한다.
while j < N*2 : #물건의 가격과 해당 물건의 수를 입력받아 리스트의 개수가 물건의 종류의 수의 2배이므로 2배보다 작을 때를 조건으로 설정한다.
    sum = sum + anfrjs[j]*anfrjs[j + 1]
    j = j + 2 #한 번에 두 개의 값을 사용하므로 겹치지 않게 하기 위해서 +2를 한다.
if total == sum :
    print('Yes')
else : print('No')
    
#2439 별 찍기
N = int(input("N의 값을 입력하세요 : "))
#1부터 입력한 값의 수까지 반복적으로 별을 출력하기 위해서 범위를 설정한 for문을 사용한다.
for i in range(1,N+1) : 
    star = str('*'*i)
    print(star.rjust(N)) #별이 오른쪽정렬이므로 rjust함수를 활용하고 마지막 수인 입력받은 값을 기준으로 오른쪽으로 정렬되어 있으므로 괄호 안에 해당 값을 넣는다.
#10807 개수 세기
N = int(input("정수의 개수를 입력하세요 : "))
wjdtn = [int(n) for n in input("공백을 두고 정수를 입력하세요 : ").split()] 
find_num = int(input("찾으려는 정수를 입력하세요: "))
print(wjdtn.count(find_num)) #리스트에서 해당 인덱스의 수를 세기 위해 count함수를 사용한다.

#2562 최댓값
#한 줄에 하나씩 받으므로 while문을 사용하여 입력받고 이를 리스트로 만든다.
chleo = []
i = 0
while i < 9 :
    chleo.extend([int(n) for n in input("자연수를 입력하세요.  : ").split()])
    i = i + 1
print(max(chleo)) #최댓값을 구해야 하므로 max함수를 사용한다.
print(chleo.index(max(chleo)) + 1) #인덱스는 0부터 시작하므로 1을 더해준다.
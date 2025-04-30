#문제:2739(구구단)
N= int(input())
for i in range(1, 10):
    print(str(N) + "*" + str(i) + "=" + str(N*i))

#문제설명
#입력받은 숫자를 정수형으로 바꾸기 위해 int()함수를 이용했습니다. 그리고 곱셈의 과정을 출력하기 위해 range함수를 이용해줬습니다. 
#1부터 9까지 곱셈을 해주기 위해 range(1,10)이라고 해줬습니다.
#곱셈 과정을 표현하기 위해 print함수 안에 문자열을 더해주는 과정을 거쳤습니다. 또한 문자열끼리 더하는것만 가능하기에 str함수를 이용해서 숫자를 문자열로 바꿨습니다.

#문제:25304(영수증)
T = int(input())
N = int(input())

for _ in range(N):
    price, count = input().split()
    price = int(price)
    count = int(count)
    T = T - (price * count)
if T == 0:
    print("YES")
else:
    print("NO")
#문제설명
#우선 총액을 Total 앞에 있는 T로 표현하였고 개수를 N으로 표현했습니다. 또한 금액과 개수를 입력할때 공백을 포함하여 출력될 수 있게 split함수를 이용했습니다.
#또한 int함수를 이용해서 정수형으로 변환해 주었습니다.
#전체 계산된 금액이 영수증에 기입된 값과 맞는지 비교하기 위해 -를 이용하여 0이면 YES가 출력되도록, 아니라면 NO가 출력되게 하였습니다.

#문제:2439(별 찍기)
N = int(input())

for i in range (1, N+1):
    space = " " * (N - i)
    star = "*" * i
    print(space + star)
#문제설명
#우선 개수를 정수형으로 변환해주기 위해 int함수를 썼습니다.
#또한 별을 만들기 위해 범위를 먼저 설정해 줍니다. 만약 4개가 입력되었다면 1부터 4까지 범위가 좁혀져야 하기 때문에N+1 로 범위를 만들어 줬습니다. 
#공백을 별 앞에다 순서대로 하나씩 추가해줘야하기 때문에 N-1을 이용해줍니다.
#별도 공백과 똑같이 코드를 짜줍니다.
#마지막으로 줄 하나씩 별이 만들어져야 하기에 space와 star을 더해주어 출력해줍니다.

#문제:10807(개수 세기)
N = int(input())
number = input().split()
v = input()

count = 0

for num in number:
    if num == v:
        count = count + 1
print(count)

#문제설명
#우선 입력된 수를 정수형으로 받기 위해 int함수를 써줍니다. 그리고 숫자를 입력받는데, 공백으로 나누기 위해 split함수를 써줍니다.
#입력받은 v가 몇번 나오는지 세기 위해 count = 0을 써줍니다. 초기값을 0으로 시작한 상태라고 할 수 있습니다.
#numbe안에 있는 숫자를 세기 위해 for문을 이용해줍니다.
#하나씩 개수를 셀때마다 count도 하나씩 올라가도록 설정을 해줍니다.
#마지막에 개수가 몇개인지 출력하기 위해 pinr(count)를 해줍니다.

#문제:2562(최댓값)
numbers = []

for _ in range(9):
    num = int(input())
    numbers.append(num)

max_value = max(numbers)
position = numbers.index(max_value) + 1

print(max_value)
print(position)
#문제설명
#우선 숫자들을 담을 리스트를 하나 만들어주기 위해 []를 이용해줍니다.
#9개 숫자를 입력받기 위해 for문을 써줬고 _는 비워줍니다.
#append함수를 이용해서 숫자가 비어있는 리스트에 차례대로 추가될 수 있도록 해줍니다.
#가장 큰 수가 무엇인지 찾을 수 있는 함수 max를 이용합니다. 그럼 어떤 수가 가장 큰지 자동으로 찾을 수 있습니다.
#가장 큰 수가 나온 위치를 알기 위해 index를 써줍니다. 이때 위치를 셀때 0부터 시작하는것을 고려하여 1을 더해줍니다.

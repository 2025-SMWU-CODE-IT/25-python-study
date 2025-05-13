#5597번 과제 안 내신 분..?
#과제 안 낸 사람 출석 번호 찾기

nums = [] #nums랑 nonnums란 리스트를 만들어 숫자를 넣을 리스트와 숫자가 제거된 목록을 넣을 리스트를 만든다.
nonnums = []
for i in range(28): #28개만 하면 되므로 범위를 이와 같이 설정한다. 
    x = int(input())
    nums.append(x) #정수형으로 변환된 입력된 숫자를 nums란 리스트에 더한다.
for i in range(1,31): #0번이 없기 때문에 1,31로 범위를 뒀다.
    if i not in nums : #nums란 리스트에 없을 때
        nonnums.append(i) #nonnums란 리스트에 추가했다.
print(nonnums.list[0]) #리스트의 처음 숫자를 출력했다.
print(nonnums.list[1]) #리스트의 그 다음 숫자를 출력했다.

#간단하게 수정한 코드 
nums = [i for i in range(1,31)]
for i in range(28):
    x = int(input())
    nums.remove(x)
print(min(nums)) #리스트의 min을 출력으로 바꿈
print(max(nums)) #리스트의 max를 출력으로 바꿈

#1546번 평균
#평균 점수 조작하기

sub = int(input()) #입력된 시험 점수를 정수형으로 바꾼다.
test = [] #test란 리스트를 만들어 점수 리스트를 만든다.

num = input().split() #문자열로 입력받았기 때문에 공백 기준으로 나눈다.
for i in range(sub): #시험 점수의 범위 안에서
    test.append(int(num[i])) #문자열을 정수로 바꿔서 리스트에 추가한다.
M = max(test) #최고의 시험 점수를 max로 구한다.
for i in range(sub): #시험 점수의 범위에서서
    test[i] = test[i] / M * 100 #시험 점수를 가장 큰 점수를 기준으로 바꾼다.

print(sum(test) / sub) #평균을 출력한다.

#2444 별찍기
#별을 다이아몬드 모양으로 찍히게 한다.

n = int(input()) #입력될 변수를 정수형으로 바꾼다.
for i in range(1,n): #변수보다 1 작은 숫자까지의 범위에서 
    print(' '*(n-i) + '*'*(2*i-1)) #공백을 변수-i개, 별을 2*i-1개를 출력한다.
print('*'*(2*n-1)) #n번째 줄에선 공백없이 별을 2*n-1개 출력한다.
i = n-1 #아래를완성하기 위해 역으로 출력한다.
while i > 0: #0이 될 때까지지
    print(' '*(n-i) + '*'*(2*i-1)) #위에와 마찬가지로 출력한다.
    i-=1 #하나씩 줄일 때를 위한 코드다.

#2501 약수구하기
#약수 출력/개수에 따라 0 출력하기

factor = input().split() #2개가 입력되므로 split을 쓴다.
num = int(factor[0]) #첫번째로 입력된 걸 정수형으로 변환하고 num으로 둔다.
div= int(factor[1])#첫번째로 입력된 걸 정수형으로 변환하고 div으로 둔다.

for i in range (1, num+1): #첫번째에서 마지막까지의 범위 안에서
    if num% i == 0: #나머지가 0이면
        div -= 1 #숫자를 하나 줄이게 했다
        if div == 0: #만약 아랫변수 나머지지가 0이면
            print(i) #숫자를 출력하고 아래 break를 통해 루프를 멈췄다.
            break
else: 
    print(0) #이가 모두 아니면 0을 출력하게 했다.

#10773 제로
#숫자 합 구하기

k = int(input()) #입력횟수를 입력한다.
js = [] #사용할 리스트를 초기화한다. 

for i in range(k): #입력횟수의 범위 안에서
    num = int(input()) #사용자한테 정수를 입력받는다.
    if num == 0: #입력 값이 0이면 마지막 수를 제거해야하므로 조건문 시작
        js = js[:-1] #슬라이싱을 사용해서 마지막 요소를 지운다.
    else:
        js.append(num) #그게 아니면 숫자를 더한다.

print(sum(js)) #최종 남은 것만 합을 더한다.

#17256 달달함이 넘쳐흘러
#케이크 수 입력받아서 계산이 맞으면 출력 / 오류 메시지 출력 

class cakenumber: #클래스 정의 
    def __init__(self, x, y, z): #클래스를 만들 때 x,y,z 값을 받아 인스턴스 변수로 저장한다.
        self.x = x
        self.y = y
        self.z = z

    def operate(self, other): #케이크 연산을 구현한다다
        nx = self.z + other.x
        ny = self.y * other.y
        nz = self.x + other.z
        return cakenumber(nx, ny, nz) #결과적으로 새로운 케이크넘버 객체로 반환된다다

    def __str__(self):
        return f"{self.x} {self.y} {self.z}"


a_x, a_y, a_z = map(int, input().split()) #a,c를 입력받아 map을 사용해 정수형으로 바꾸고 나눈다(여러개입력이라)
c_x, c_y, c_z = map(int, input().split())


a = cakenumber(a_x, a_y, a_z) #입력받은 값으로 케이크 수 a와c 생성
c = cakenumber(c_x, c_y, c_z)


b_x = c.x - a.z #연산을 반대로 한다
b_y = c.y // a.y
b_z = c.z - a.x


if b_x < 1 or b_y < 1 or b_z < 1 or c.y % a.y != 0: #조건에 따라 케이크 계산이 유효할 때 오류가 아님이라고 뜨게 둔다.
    print("유효한 케이크 수 b가 존재하지 않습니다.")
else:
    b = cakenumber(b_x, b_y, b_z)
    print(b) #모든 조건이 맞을 때 b를 출력한다. 

#17256 고친 거

class cake:
    x = 0
    y = 0
    z = 0

    def cakexyz(self): #self를 사용하여 정의를 내려준다. 
        nums = input().split()
        self.x = int(nums[0])
        self.y = int(nums[1])
        self.z = int(nums[2])

a = cake()
b = cake()
c = cake()

a.cakexyz()
c.cakexyz()

b.x = c.x - a.z
b.y = c.y // a.y
b.z = c.z - a.x

print(b.x, b.y, b.z)
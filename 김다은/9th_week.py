#9주차 과제

#문제번호:5597
nums = []
while True:
    i = int(input())  # -1이 아닌 값을 계속 입력받음.
    if i == -1 :  # -1을 입력하면 프로그램이 종료됨.
        break
    nums.append(i) # 입력받은 값을 리스트에 저장함.


absent = []  # 1부터 30 중 없는 숫자가 이 리스트에 저장됨.
for i in range(1, 31):
    if i in nums:
        pass
    else:
        absent.append(i)
print(absent[0])
print(absent[1])



#문제번호:1546
num = int(input("과목의 개수"))

# 입력 받은 점수를 정수형으로 바꿔서 리스트에 저장.
grade = [int(n) for n in input().split()]
max_grade = max(grade) # 점수 중 최댓값을 고름.
sum = 0

# 모든 점수를 점수/(최댓값)*100으로 고침.
for i in grade:
    sum += i/max_grade*100

print(sum/num)



#문제번호:2444
N = int(input())
for i in range (1, 2*N):

    # N번째 줄까지는 별의 개수가 점점 커지면서 출력됨.
    if i<=N:
        print(" "*(N-i), "*"*(2*i-1))

    # N번째 줄이 넘어가면 별의 개수가 점점 줄어들면서 출력됨.
    else:
        print(" "*(i-N), "*"*(4*N-2*i-1))



#문제번호:2501
num = input().split()
N = int(num[0])
K = int(num[1])

array = []
# N을 1부터 N까지의 숫자로 나누었을 때 나머지가 0 인 수들은 약수임을 이용.
for i in range(1, N+1):
    if N % i == 0:
        array.append(i)

# 약수의 개수가 K보다 작은 경우 0을 출력함. 
if len(array) < K:
    print(0)

else:
    print(array[K-1])



#문제번호:10773
total = [] # 재민이가 적은 수를 저장하는 리스트.
count = int(input("정수 입력"))
for i in range(1, count+1):
    num = int(input())
    if num != 0:
        total.append(num)
    else: 
        del total[-1]  # 재민이가 0을 외치면 리스트의 가장 마지막 값을 지움.

print(sum(total))



#문제번호:17256
# class는 아직 익숙치 않아서 좀 더 고민해보고 추가로 제출하겠습니다.
class CakeNumber:
    def __init__(self ,x , y, z):
        self.x = x
        self.y = y
        self.z = z

a = CakeNumber()

#def calc(self, other):
    #return CakeNumber(self.z + other.x, self.y*other.y, self.x + other.z)


# class 이용 안 한 코드
# 케이크 수 a를 구성하는 자연수를 입력받아 리스트로 저장함.
a = [int(n) for n in input().split()] 

# 케이크 수 c를 구성하는 자연수를 입력받아 리스트로 저장함.
c = [int(n) for n in input().split()]

# 케이크 수의 특이한 연산을 이용하여 a와 c를 통해 b를 구함. 
b = [c[0]-a[2], c[1]/a[1], c[2]-a[0]]

# 케이크 수 b를 구성하는 자연수들을 하나의 공백을 사이에 두고 차례대로 출력함.
for i in b:
    print(i, end=" ")

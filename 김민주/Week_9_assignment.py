#9주차 과제
#[김민주] 2025년 1학기 python study - 9주차

#5597번 과제 안 내신 분...?
student = []

for i in range(1, 31):
    student.append(i)

for i in range(28):
    attendance = int(input())
    student.remove(attendance)

print(student[0])
print(student[1])

#1546 평균
N = int(input())
score = [int(n) for n in input().split()]
M = max(score)

rescore = [] 
for s in score:
    new_score = (s / M) * 100
    rescore.append(new_score)

print(sum(rescore) / N)

#2444 별 찍기
N = int(input())

# 위쪽 삼각형, 1 ~ N번째 줄까지.
for i in range(1, N + 1):
    spaces = ' ' * (N - i) #공백
    stars = '*' * (2 * i - 1) #별 찍기
    print(spaces + stars) #공백, 별 합치기.

# 아래쪽 삼각형, N-1 부터 내려감.
for i in range(N - 1, 0, -1):
    spaces = ' ' * (N - i)
    stars = '*' * (2 * i - 1)
    print(spaces + stars)

#2501, 약수구하기
N, K = [int(n) for n in input().split()]

divisor = [] #약수를 저장

for i in range(1, N+1): #1부터 N까지 약수 확인인
    if N % i ==0: #i가 N의 약수인지 판별하는 식식
        divisor.append(i) #맞다면 리스트에 추가함

#[조건:N의 약수의 개수가 K개보다 적어서 K번째 약수가 존재하지 않을 경우에는 0을 출력하시오.]
if len(divisor) >= K: #divisor의 길이와 K비교.
    print(divisor[K - 1])
else: #divisor의 길이가 K보다 짧다면 0을 출력함.
    print(0)

#10773, 제로
K = int(input())
nums = [] #숫자를 정리하기 위한 리스트.

for i in range(K):
    num = int(input())
    if num == 0:
        if nums: #리스트가 비어 있지 않으면 마지막 값 삭제
            nums.pop() #리스트의 마지막 값을 지우는 pop() 사용
    else:
        nums.append(num) #새로운 값 추가가

total = sum(nums)# 남아있는 숫자들의 합

print(total)# 최종합합

#17256, 달달함이 넘쳐흘러

class CakeNumber:
    def init(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def str(self):
        return f"{self.x} {self.y} {self.z}"

    def calculate_b(self, a, c):
        # a (케이크) b = c에서 b를 구하기 위한 수식들
        b_x = c.x - a.z 
        b_y = c.y // a.y 
        b_z = c.z - a.x 
        return CakeNumber(b_x, b_y, b_z)

# 입력 받기
a_x, a_y, a_z = [int(n) for n in input().split()]
c_x, c_y, c_z = [int(n) for n in input().split()]

# CakeNumber 객체 생성
a = CakeNumber(a_x, a_y, a_z)
c = CakeNumber(c_x, c_y, c_z)

# b 계산
b = a.calculate_b(a, c)

# 결과 출력
print(b)



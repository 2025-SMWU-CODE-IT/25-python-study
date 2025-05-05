#5597 과제 안 내신 분..?
a = [int(n) for n in range(1,31)]#1부터 30까지 학생 출석부 생성
#과제를 제출 한 학생 번호 받고, 그 번호가 출석부에 있다면 지움
for i in range(28):
    b = int(input())
    if b in a:
        a.remove(b)
#과제를 제출하지 않은 번호만 출석부에 남았으므로 출력함
print(a[0])
print(a[1])

#1546 평균
N = int(input())#시험 본 과목의 개수
S = [int(n) for n in input().split()]#세준이의 현재 성적
M = max(S)#자기 점수 중에 최댓값
a = []#세로운 성적을 넣을 빈 리스트 생성
for i in S:
    b = i/M*100
    a.append(b)
j = 0
for k in a:
    j += k
print(j/N)#평균값 출력

#2444 별 찍기 -7
N = int(input())#숫자 입력
for i in range(N):#피라미드 모양 생성
    print(' '*(N-(i+1)),end='')
    print('*'*((i+1)*2-1))
for j in range(N-1):#역피라미드 모양 생성
    print(' '*(j+1),end='')
    print('*'*((N*2-1)-((j+1)*2)))

#2501 약수 구하기
N, K = [int(n) for n in input().split()]
a = []#약수들을 넣어줄 빈 리스트 생성
j = 1#1부터 나눠가며 약수 확인
while j <= N:
    if N % j == 0:#나머지가 0이라면 리스트에 추가
        a.append(j)
    j += 1
#K번째 약수를 출력하되, 존재하지 않으면 0을 출력
try:
    print(a[K-1])
except:#예외 처리
    print(0)

#10773 제로
K = int(input())#부를 돈의 수
a = []#돈을 적을 빈 리스트 생성
#K번만큼 돈을 받음
for i in range(K):
    b = int(input())
    if b == 0:#0이 입력되면 마지막 돈을 삭제
        a.pop()
    else:
        a.append(b)
c = 0
#돈의 합
for j in a:
    c += j
print(c)

#17256 달달함이 넘쳐흘러
class Cake:#클래스 선언
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
#입력 받음
ax, ay, az = [int(n) for n in input().split()]
cx, cy, cz = [int(n) for n in input().split()]
#객체로 선언
a = Cake(ax, ay, az)
c = Cake(cx, cy, cz)
#b를 계산함
bx = cx - az
by = cy // ay
bz = cz - ax
print(bx, by, bz)
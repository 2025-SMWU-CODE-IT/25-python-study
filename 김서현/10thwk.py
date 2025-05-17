#9610 사분면
# 점의 위치가 사분면 어디에 있는지 구하는 문제이다.
n =int(input())
q1 = q2 = q3 = q4 = graph = 0 #좌표마다 더할곳을 초기화한다.

for i in range(n): #n의 범위 안에서 
    nums = input().split() #2개가 입력되므로 split을 사용한다. 
    a = int(nums[0])
    b = int(nums[1])

    if a==0 or b ==0: #선에 있을 때 axis에 넣을 거 하나 추가한다.
        graph += 1
    elif a>0 and b>0 : #1사분면 조건이다.
        q1 += 1
    elif a<0 and b>0 : #2사분면 조건이다.
        q2 += 1
    elif a<0 and b<0 : #3사분면 조건이다.
        q3 += 1
    elif a>0 and b<0 : #4사분면 조건이다.
        q4 += 1

#마지막으로 다 프린트한다.
print("Q1: %d" %q1)
print("Q2: %d" %q2)
print("Q3: %d" %q3)
print("Q4: %d" %q4)
print("AXIS: %d" %graph)


#2163 초콜릿 자르기 
#초콜릿 자르면 나오는 개수 구하기다. 

n, m = input().split() #2개 입력하므로 스플릿 쓴다. 
N = int(n)
M = int(m)
#정수형으로 바꿔준다.
print(N-1+(M-1)*N) #개수 출력

#2530 인공지능 시계
#시간 표시하고 계산한다. 

h, m, s = input().split() #시분초를 출력한다.
H = int(h) #정수형으로 바꾼다. 
M = int(m)
S = int(s)
Dsec = int(input()) #초 더할 것 설정. 

S += Dsec%60 #초를 60으로 나눴을 때 남은 것을 기준으로 더한다. 
Dsec = Dsec//60
if S >= 60:
    S-= 60
    M += 1

M += Dsec % 60
Dsec = Dsec //60
if M >= 60:
    M -= 60
    H += 1

H += Dsec % 24
if H >= 24:
    H -= 24

print(H,M,S) #초가 몇 분인지에 따라 시,분,초를 조정한다. 마지막에 시 분 초를 프린트한다. 


#2480 주사위 세개 
#주사위 눈에 따라 숫자 출력하기 

a, b, c = input().split() #3번 던졌을 때 눈을 출력하기 위해서 a,b,c를 설정한다. 
A= int(a)
B = int(b)
C =int(c)

if A == B == C: #모두 같을 때의 출력이다.
    print(10000+A*1000)
elif A == B: #C가 다를 때의 출력이다.
    print(1000+A*100)
elif A == C: #B가 다를 때의 출력이다.
    print(1000+A*100)
elif B == C: #A가 다를 때의 출력이다. 
    print(1000+B*100)
else: #다 다를 때의 출력이다. 
    print(100 * max(A,B,C))


#7567 그릇
#그릇 방향에 따라 그릇 길이 측정하는 코드다. 

plate = list(str(input())) #접시에 대해 리스트를 설정한다. 
sum = 0 #sum을 두고 길이를 더하는 곳을 만든다.

for i in range(len(plate)): #조건에 따라 접시 길이를 더한다. 
    if i == 0:
        sum += 10
    elif plate[i] == plate[i-1]:
        sum += 5
    else:
        sum += 10

print(sum) #합을 더한 것을 출력한다.

#11557 Yangjojang of The Year 
#누가 술 많이 마셨는지 구하는 프로그램.

T = int(input()) #입력 
for i in range(T):
    school = [] #리스트를 만들어 각 학교와 음주량에 대해 계산을 한다.
    booze = []
    N = int(input())
    for _ in range(N):
        a, b =input().split()
        school.append(a)
        booze.append(int(b))
    M = booze.index(max(booze)) #가장 많이 마신 학교, 음주량 출력 
    print(school[M])

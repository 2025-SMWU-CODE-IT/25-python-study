#9610 사분면
n  = int(input())
a = []#좌표를 넣을 빈 리스트 형성
for i in range(n):
    b = [int(n) for n in input().split()]
    a.append(b)#리스트 형태로 a에 추가
#사분면과 축의 개수
Q1 = 0
Q2 = 0
Q3 = 0
Q4 = 0
AXIS = 0
for j in range(n):#n만큼 실행
    if a[j][0] > 0 and a[j][1] > 0:#사분면 판단
        Q1 += 1
    elif a[j][0] < 0 and a[j][1] > 0:
        Q2 += 1
    elif a[j][0] < 0 and a[j][1] < 0:
        Q3 += 1
    elif a[j][0] > 0 and a[j][1] < 0:
        Q4 += 1
    elif a[j][0] == 0 or a[j][1] == 0:#축 판단
        AXIS += 1
print('Q1:',Q1)
print('Q2:',Q2)
print('Q3:',Q3)
print('Q4:',Q4)
print('AXIS:',AXIS)

#2163 초콜릿 자르기
N, M = [int(n) for n in input().split()]#입력받음
print(N*M-1)#결과값들의 규칙을 이해한 후 출력

#2530 인공지능 시계
A, B, C = [int(n) for n in input().split()]
D = int(input())
n = A*3600 + B*60 + C + D#입력받은 시간을 몽땅 초로 바꿈
A = n // 3600 % 24#시간으로 바꿈 #24의 나머지로 하여 24시간이 넘어가는 것도 처리
B = (n % 3600) // 60#분으로 바꿈
C = n % 60#초로 바꿈
print(A, B, C)

#2480 주사위 세개
a = [int(n) for n in input().split()]#세개의 주사위 수
if a[0] == a[1] == a[2]:#전부 같은 경우
    print(10000 + a[0] * 1000)
elif a[0] == a[1] != a[2]:#두개가 같은 경우
    print(1000 + a[0] * 100)
elif a[0] == a[2] != a[1]:
    print(1000 + a[0] * 100)
elif a[2] == a[1] != a[0]:
    print(1000 + a[1] * 100)
else:#전부 다른 경우
    print(max(a) * 100)

#7567 그릇
a = input()
b = list(a)#리스트로 바꿈
n = len(b)#리스트 길이를 잼
c = 10#첫 그릇
for i in range(n-1):
    if b[i] == b[i+1]:#같을 때
        c += 5
    else:#다를 때
        c += 10
print(c)

#11557 Yangjojang of The Year
def shull(s):#함수 정의
    a = []#학교 이름과 술 숫자를 넣을 리스트
    for i in range(s):
        b = input().split()
        a.append(b)#학교 이름과 술 수를 리스트 형태로 추가
    c = []#술 숫자를 정수 형태로 변환한 후 넣을 빈 리스트 생성 
    for k in range(s):
        d = int(a[k][1])
        c.append(d)
    e = c.index(max(c))#가장 큰 수의 인덱스 확인 
    print(a[e][0])#학교 출력 

T = int(input())
for i in range(T):#T만큼 반복 
    N = int(input())#판단할 학교 수 
    shull(N)
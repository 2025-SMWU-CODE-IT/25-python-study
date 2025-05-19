#9610 사분면
Q1 = Q2 = Q3 = Q4 = 0 
#함수 설정: x, y받고 사분면 판단
def main(x, y):
    x = int(x)
    y = int(y) 

    global Q1, Q2, Q3, Q4
#좌표 확인 후, 각 사분면 개수에 +1
    if x > 0: 
        if y > 0: 
            Q1 += 1
        if y < 0: 
            Q2 += 1 
    if x < 0: 
        if y > 0: 
            Q3 += 1
        if y < 0: 
            Q4 += 1

num = int(input(" "))
S = []
M = []
for i in range(num):
    S.append(input(" ").split(" ", 2))

for i in range(num):
    main(S[i][0], S[i][1] )

print("Q1: ", Q1)
print("Q2: ", Q2)
print("Q3: ", Q3)
print("Q4: ", Q4)

#2163 초콜릿 자르기 
n = input("").split(" ", 2)
g = int(n[0])
s = int(n[1])

#큰 값, 작은 값일 경우로 나누어 계산
if g > s: 
    print((s-1) + s * (g-1))

if g < s: 
    print((g-1) + g * (s-1))

if g == s: 
    print((s-1) + s * (s-1))

#2530 인공지능 시계 
n = input("").split(" ", 3)
s = int(input(""))

H = int(n[0])
M = int(n[1])
S = int(n[2])
#전체 시간을 초로 바꾸어서 계산
T = 3600*H + 60*M + S
T = T + s 
#만약 시간이 24시가 넘는 경우를 고려하여 전체 시간이 1시간으로 나눈 몫이 24가 넘을 경우 24시간을 빼서 시간 리셋
if T//3600 >= 24: 
    print(T//3600-24, (T%3600)//60, (T%60))
else: 
    print(T//3600, (T%3600)//60, (T%60))

#2480 주사위 세 개 
n = input("").split(" ", 3)
n1 = int(n[0])
n2 = int(n[1])
n3 = int(n[2])
#입력받은 주사위 값이 모두 다를 경우, 같을 경우, 두 개가 같을 경우로 나누어서 계산
if n1 != n2 != n3:
    print(int(max(n))*100)
elif n1 == n2 == n3: 
    print(10000+ n1*1000)
else: 
    #n1과 n2, n2와 n3, n1와 n3가 같을 경우로 나누어서 계산
    if n1 == n2: 
        print(1000 + int(n1)*100)
    if n1 == n3: 
        print(1000 + int(n1)*100)
    if n2 == n3: 
        print(1000 + int(n2)*100)

#7567 그릇 
bowl = input("")
list = [] 
length = 10

#입력받은 값을 리스트로 저장
for i in bowl:
    list.append(i)

#입력받은 그릇이 같을 경우와 아닐 경우로 나누어서 전체 길이 계산
for k in range(len(list)-1):
    if list[k] == list[k+1]:
        length +=5
    else: 
        length += 10 

print(length)

#11557 Yangjojang of The Year

case = int(input(""))
list_s = []
list_d = []

#테스트 케이스동안 반복 
for i in range(case):
    sch = int(input(""))
    #학교 입력만큼 반복
    for k in range(sch): 
        #입력받은 각 값들을 list에 저장
        dri = input("").split(" ", 2)
        list_s.append(dri[0])
        list_d.append(dri[1])
    #가장 큰 값 가지는 인덱스로 해당 학교를 출력
    maxx = list_d.index(max(list_d))
    print(list_s[maxx])

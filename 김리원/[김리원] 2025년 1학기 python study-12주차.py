#13909 창문닫기 

num = int(input())
win =[]
NumOfWin = 0
for i in range(num):
    win.append(1)

#열고 닫히는 작용을 할 때마다 해당 리스트 값에 +1
for i in range(2, num+1):
    for k in range(1, num//i +1):
        win[(i*k)-1] += 1

#각 리스트 값을 2로 나눈 나머지로 다시 저장하여 열고 닫힘을 구분함.
for i in range(len(win)): 
    win[i] = win[i] % 2
    if win[i] == 1: 
        NumOfWin += 1

print(NumOfWin)

#7785 회사에 있는 사람 
num = int(input())
person = []
EnterP = []
LeaveP = [] 
#enter일 경우 EnterP로 저장, leave할 경우 LeaveP 리스트에 각 이름을 저장함.
for i in range(num):
    person = input().split(" ", 2)
    if person[1] == "enter": 
        EnterP.append(person[0])
    if person[1] == "leave": 
        LeaveP.append(person[0])
#EnterP와 LeaveP 리스트에 저장된 값이 같을 경우, 해당 값을 EnterP에서 지움
dele = 0
for q in range(len(EnterP)):
    for k in range(len(LeaveP)):
        if EnterP[q - dele] == LeaveP[k]:
            del EnterP[q-dele]
            dele += 1

print(EnterP)

#1269 대칭 차집합 
#해당 값을 입력받음
num = input().split(" ", 2)
numA = int(num[0])
numB = int(num[1])

A = input().split(" ", numA)
B = input().split(" ", numB)
#공통으로 가지는 값을 리스트에 저장함.
Common = []
for i in range(len(A)):
    for k in range(len(B)):
        if A[i] == B[k]:
            Common.append(A[i])
print(Common)
#전체 합집합을 저장함
AplusB = A + B
print(AplusB)
#합집합과 교집합의 차이를 리스트로 저장함
Want = []
for Q in AplusB: 
    if (Q in Common) != True: 
        Want.append(Q)

print(Want)

#27433 팩토리얼2

#팩토리얼 값을 구할 해당 값을 입력받는다.
num = int(input())
result = 1

#해당 값까지의 곱(팩토리얼 값을 구하고 출력한다)
for i in range(1, num+1):
    result = result * i
print(result)

#2559 수열
K = input().split(" ", 2)
day = int(K[0])
array = int(K[1])
plus = []

seq= input().split(" ", day)
for i in range(day-array+1):
    plus_A = 0
    for k in range(array):
        plus_A += int(seq[i + k])
    plus.append(plus_A)

print(max(plus))

#20920 영단어암기는 괴로워
first_list = input().split(" ", 2)

num = int(first_list[0])
stan = int(first_list[1])
voca = []

for i in range(num):
    voca.append(input())

#길이 기준에 맞는 단어만 들어가는 리스트 지정
new_voca = []
for k in voca: 
    len = 0
    for q in k:
        len += 1
    if len >= stan :
        new_voca.append(k)

new_new_voca = []
count_ = []
for k in new_voca:
    count_.append(count(new_voca[k]))
new_voca.finc(max(count))

    
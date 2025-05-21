# 문제번호:9610
num = int(input("점의 개수 입력"))
# 초기값을 0으로 설정하고 좌표를 읽을 때마다 해당 좌표평면의 개수 추가
Q1 = 0
Q2 = 0
Q3 = 0
Q4 = 0
axis = 0

for i in range(1, num+1):
    # 좌표값을 리스트에 저장
    coor = [int(n) for n in input().split()]

    if coor[0] > 0:
        if coor[1] > 0:
            Q1 += 1
        elif coor[1] == 0:
            axis += 1
        else:
            Q4 += 1

    elif coor[0] == 0:
        axis += 1

    else:
        if coor[1] > 0:
            Q2 += 1
        elif coor[1] == 0:
            axis += 1
        else:
            Q3 += 1

print("Q1: ", Q1)
print("Q2: ", Q2)
print("Q3: ", Q3)
print("Q4: ", Q4)
print("axis: ", axis)



# 문제번호:2163
num = input().split()
N = int(num[0])
M = int(num[1])

# 자르기 횟수는 잘리는 조각의 개수 -1 임을 이용
print(N*M-1)



# 문제번호:2530
# 시, 분, 초 값을 리스트에 저장
time = [int(n) for n in input().split()]
A = time[0]
B = time[1]
C = time[2]
D = int(input())

min = D//60
sec = D % 60

if C + sec > 60:
    C = 0

    # 초에서 분으로 넘어옴.
    B = B + min + (C + sec - 60)
    if B > 60:
        # 분에서 시로 넘어옴.
        A = A + (B - 60)
        B = 0
        

else:
    C = C+sec
    if B + min > 60:
        # 분에서 시로 넘어옴.
        A = A + (B + min - 60)
        B = 0
        
print(A, B, C)


# 문제번호:2480
result = [int(n) for n in input().split()]

# 주사위 눈의 개수를 변수 a, b, c에 저장.
a = result[0]
b = result[1]
c = result[2]

# 세번의 결과가 같음.
if a == b == c:
    print(10000 + a*1000)

# 세번 중 두번의 결과가 같음
elif a == b:
    print(1000 + a*100)
elif a == c:
    print(1000 + a*100)
elif b == c:
    print(1000 + b*100)

# 세번의 결과가 다 다름.
else:
    print(100*max(result))


# 문제번호:7567
# 입력받은 문자열의 문자들을 요소로 하는 리스트 생성
str = list(input())

# 문자열의 문자의 개수를 구함.
num = len(str) 
height = 10

for i in range (1, num):
    # 같은 문자가 연속으로 나오는 경우.
    if str[i] == str[i-1]:
        height += 5

    # 이전 문자와는 다른 문자가 나오는 경우.
    else:
        height += 10

print(height)


# 문제번호:11557
T = int(input("테스트 케이스 숫자"))

# 테스트케이스별로 구하기
for i in range(1, T+1):
    N = int(input("학교의 숫자")) 
    maxAmount = 0
    maxUniv = ""
    for n in range(1, N+1) :
        values = input().split()
        amount = int(values[1])

        # 새로 입력받은 양이 이전 양보다 크다면 값을 대체함.
        if maxAmount == 0 or maxAmount < amount:
            maxUniv = values[0]
            maxAmount = amount
        
    print(maxUniv)







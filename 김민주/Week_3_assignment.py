#3주차 과제
#[김민주] 2025년 1학기 python study - 3주차

#27866
S = input("단어길이 최대 100 : ")
i = int(input("위치 : "))

print(S[i-1])

#2743
S1 = input()
print(len(S1))

#11654
A = input()
print(ord(A))

#2908
sang, geun = input("상근 : ").split()
if sang >= geun :
    print(sang[2]+sang[1]+sang[0])
else :
    print(geun[2]+geun[1]+geun[0])

#1330
A, B = input().split()
if int(A) > int(B) :
    print(">")
elif int (A) == int(B) : 
    print("==")
else : 
    print("<")

#9498
T = int(input())
if 100>=T>=90 :
    print("A")
elif 90>T>=80 :
    print("B")
elif 80>T>=70 :
    print("C")
elif 70>T>=60 :
    print("D")
else:
    print("F")

#2884
H = int(input("시간 : "))
M = int(input("분 : "))
while H > 24 or M > 60: #처음 받은 시간을 판정하기 위함.
    print("다시 설정 해주세요")
    H = int(input("시간 : "))
    M = int(input("분 : "))
    continue #만약, 범위 내의 숫자가 아니면 반복문 다시 실행.
alarm = H*60 + M - 45 #시간도 분으로 바꾼 후, 45분 빼줌.
H = alarm // 60
M = str(alarm - H*60) #아래의 프린트 문에서 :를 출력하기 위해 자료형을 문자열로 변환해줌.
H = str(H)

print(H + ":" + M)

#10988
B = input()
i = 0

if B[0+i] == B[-1-i]: #맨 앞, 맨 뒤부터 하나씩 비교하며 진행됨.
    while True:
        i+=1
        print(1)
        if i == i: #만약 자릿수가 같아질때, 반복문을 탈출.
            break  
else:
    print(0)

#2주차 과제
#[김민주] 2025년 1학기 python study - 3주차

#27866
S = input("단어길이 최대 100 : ")
i = int(input("위치 : "))

print(S[i-1])

#2743
S1 = input("알파벳으로만 이루어진 단어를 입력해주세요 : ")
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
A = int(input("A<=10,000인 수를 입력하세요 : "))
B = int(input("B<=10,000인 수를 입력하세요 : "))
if A>B :
    print(">")
elif A==B : 
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
while H > 24 or M > 60:
    print("다시 설정 해주세요")
    continue
alarm = H*60 + M - 45
H = alarm // 60
M = str(alarm - H*60)
H = str(H)

print(H + ":" + M)

#10988
B = input()
i = 0

if B[0+i] == B[-1-i]:
    while True:
        i+=1
        print(1)
        if i == i:
            break  
else:
    print(0)

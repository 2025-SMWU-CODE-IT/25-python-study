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
sang, geun = input().split()

s1 = sang[2] + sang[1] + sang[0]
g1 = geun[2] + geun[1] + geun[0]

if int(s1) > int(g1):
    print(s1)
else:
    print(g1)

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
if T >= 90:
    print("A")
elif T >= 80:
    print("B")
elif T >= 70:
    print("C")
elif T >= 60:
    print("D")
else:
    print("F")


#2884
H, M = input().split()
H = int(H)
M = int(M)
if M < 45:
    H = (H - 1) % 24
    M += 15
else:
    M -= 45
print(H, M)

#10988
B = input()
length = len(B)
i = 0
pelin = 0

for i in range(length//2): #추가, 문자 길이의 절반만 연산하면 앞뒤에서 비교할때 모두 비교가 됨
    if B[0+i] == B[-1-i]: #맨 앞, 맨 뒤부터 하나씩 비교하며 진행됨. 
        pelin = True #추가, for 안에 있으면 어떻게든 반복되니깐, 그냥 참 거짓을 판별하여, 마지막에 프린트.
    else:
        pelin = False
    
if pelin:
    print(1)
else:
    print(0)

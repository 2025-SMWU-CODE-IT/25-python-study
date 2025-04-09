#27866번 문자와 문자열

S = input()
i = int(input())
print(S[i-1])

#2743번 단어 길이 재기
a = input()
print(len(a))

#11654번 아스키 코드
a = input()
print(ord(a))

#2908번 상수
a , b = input().split()
x = int(a[2]+a[1]+a[0])
y = int(b[2]+b[1]+b[0])

if x > y :
    print (x)
else :
    print (y)

#1330번 두 수 비교하기
a , b = input().split()
A = int(a)
B = int(b)
if A > B :
    print ('>')
elif A < B :
    print ('<')
else : 
    print ('==')

#9498번 시험 성적 
a = input()
A = int(a)
if 90 <= A <= 100 :
    print("A")
elif 80<= A <=89 :
    print("B")
elif 70<= A <=79 :
    print("C")
elif 60<= A <=69 :
    print("D")
else :
    print("F")

#2884번 알람 시계
h, m = input().split()
H = int(h)
M = int(m)
if M >= 45 :
    print ( H , M-45)
else :
    if H==0 :
        print (23, 15 + M)
    else :
        print (H-1, 15 + M)

#10988번 팰린드롬인지 확인하기기
a = list(input())
b = list(reversed(a))
if a == b :
    print(1)
else : 
    print(0)
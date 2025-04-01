#27866번 문자열
a = input()
b = int(input())
print(a[b-1])

#2743 단어 길이 재기
a = input()
print(len(a))

#11654 아스키 코드
a = input()
print(ord(a))

#2908 상수
a = int(input())
b = int(input())
c = (a%10)*100+((a%100)//10)*10+(a//100)
d = (b%10)*100+((b%100)//10)*10+(b//100)
if c > d :
    print(c)
else :
    print(d)
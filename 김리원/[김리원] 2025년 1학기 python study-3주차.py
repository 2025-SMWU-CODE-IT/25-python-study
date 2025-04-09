#27866 문자와 문자열

word = input("문자열을 입력하세요")
number = int(input("숫자를 입력하세요")) -1

print(word[number])

#2743 단어 재기
word = input("문자열을 입력하세요")
print(len(word))

#11654 아스키코드
word = input("입력")
print(ord(word))

# 2908 상수
a, b = input("숫자 두 개를 입력하세요").split(" ", 2)
a = int(a)
b = int(b)

new_a = a//100 + ((a%100)//10)*10 + ((a%100)%10)*100
new_b = b//100 + ((b%100)//10)*10 + ((b%100)%10)*100

print(new_a)
print(new_b)

if new_a > new_b :
    print("상수 :  더 큰 수는:", new_a)
else: 
    print("상수 :  더 큰 수는:", new_b)

#1330 두 수 비교하기 
a, b = input("입력 >>").split(" ", 2)
a = int(a)
b = int(b)

if a > b: 
    print(">")
elif a == b: 
    print("==")
elif a < b:
    print("<")

#9498 시험 성적
score = int(input("성적 입력 >>"))
if score >= 90: 
    print("A")
elif score >= 80: 
    print("B")
elif score >= 70: 
    print("C")
elif score >= 60: 
    print("D")
else: 
    print("E")

#2884 알람 시계 
hour, min = input("시간을 입력하세요").split(" ", 2)

hour = int(hour)
min = int(min)

if min < 45: 
    hour -= 1
    min = min + 60 

print(hour, min-45)

#10988 팰린드롬인지 확인하기 
word = input("문자 입력 >> ")
correct = 0

len1 = len(word)//2 
for i in range (len1): 
    if word[i] ==  word[len(word)-i-1]: 
        correct += 1

if correct*2 >= len1: 
    print("1")
else: 
    print("0")

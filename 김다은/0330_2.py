#2주차 과제 - 

#문제번호:27866
print("단어를 입력하세요.")
a = input()
print("정수를 입력하세요.")
i = int(input())
print(a[i])


#문제번호:2743
print("단어를 입력하세요.")
a = input()
print(len(a))


#문제번호:9086



#문제번호:11654



#문제번호:11720
print("숫자의 개수를 입력하세요.")
a = int(input())
print("숫자를 입력하세요")
b = input()
##?????????

#문제번호:10809
print("단어를 입력하세요.")
S = input()



#문제번호:2675
print("테스트케이스 개수를 입력하세요.")
numberOfTestcase = int(input())
cases = []
for x in range(numberOfTestcase):
    print("테스트케이스를 입력하세요.")
    cases.append(input())

for case in cases:
    tokens = case.split()
    count = int(tokens[0])
    for i in tokens[1]:
        for p in range(count):
            print(i, end = "")
    print()



#문제번호:1152
print("문장을 입력하세요.")
a = input().split()
print(len(a))


#문제번호:2908
print("두 수 A와 B를 입력하세요.")
p = input().split()
A = p[0]
B = p[1]
number1 = ""
number2 = ""
for i in A:
    number1 = i + number1

for i in B:
    number2 = i + number2

if int(number1)>int(number2):
    print(int(number1))
else:
    print(int(number2))




#문제번호:5622
print("단어를 입력하세요.")



#문제번호:11718
print("입력하세요.")
print(input())

print("숫자를 입력하세요.")
a = input()
print("숫자를 입력하세요.")
b = str(input())
split_b = list(b)
print(int(a)*int(split_b[2]))
print(int(a)*int(split_b[1]))
print(int(a)*int(split_b[0]))
number2 = str(int(a)*int(split_b[1])) + "0"
number3 = str(int(a)*int(split_b[0])) + "00"
print(int(a)*int(split_b[2]) + int(number2) + int(number3))
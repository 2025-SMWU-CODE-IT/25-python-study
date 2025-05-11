#문제번호: 2739
n = int(input("숫자를 입력하세요."))
for i in range(1, 10):
    print(n, " * ", i, "=", n*i)


#문제번호: 25304
totalprice = int(input("총 금액을 입력하세요"))
number = int(input("구매한 물건의 종류의 수를 입력하세요"))

price = 0
for i in range(1, number+1):
    a = input().split()
    price += int(a[0]) * int(a[1])

if price == totalprice:
    print("Yes")

else: print("No")



#문제번호: 2439
num = int(input("숫자를 입력하세요"))
for i in range(1, num + 1):
    print(("*" * i).rjust(num))



#문제번호: 10807
num = int(input("정수의 개수를 입력하세요"))
a = [int(n) for n in input("정수들을 입력하세요").split()]
target = int(input("찾으려고 하는 정수를 입력하세요"))
print(a.count(target))


#문제번호: 2562
array = [int(n) for n in input("자연수를 입력하세요").split()]
max_val = max(array)
max_index = array.index(max_val)
print(max_val)
print(max_index)



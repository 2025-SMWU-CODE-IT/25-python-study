#2739 구구단 

number = int(input("1과 9사이 숫자를 입력하세요"))

for i in range(10):
    print("%d * %d =%d"%(number, i, number*i))

#25304 영수증 
total = int(input("영수증 총 가격을 입력하세요"))
total_count = int(input("구매하신 물품의 종류 개수를 입력하세요"))
total_c = 0

for i in range(total_count):
    a, b = input("가격과 개수를 입력하세요").split(" ")
    a = int(a)
    b = int(b)

    total_c += a * b

if total_c == total: 
    print("Yes")
else: 
    print("No")

#2439 별 찍기 
number = int(input("숫자 입력>> "))
for i in range(number+1): 
    print(" "*(number-i)+"*"*i)


#10807 개수 세기 
total = int(input("총 정수의 개수를 입력하세요>> "))
list_number = list(input("정수를 입력하세요").split(" ", total+1))
find_number = int(input("찾으시려는 숫자를 입력하세요"))
count = 0

for i in range(total):
    if str(find_number) == list_number[i-1]:
       count += 1
print(count)

#2562 최댓값
number = []
for i in range(9): 
    number.append(int(input("숫자 입력>>")))
print(number)

max_number = max(number)
max_index = number.index(max(number))
print(max_number)
print(max_index+1)
#2739 구구단 
#1과 9사이 숫자를 입력받음.
number = int(input())

for i in range(10):
    print("%d * %d =%d"%(number, i, number*i))

#25304 영수증 
#영수증 총가격을 입력받음 
total = int(input())
#물품의 종류 개수를 입력받음.
total_count = int(input())
total_c = 0

for i in range(total_count):
    a, b = input().split(" ")
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
#정수의 개수를 입력받음.
total = int(input())
list_number = list(input().split(" ", total+1))
find_number = int(input())
count = 0

for i in range(total):
    if str(find_number) == list_number[i-1]:
       count += 1
print(count)

#2562 최댓값
number = []
for i in range(9): 
    number.append(int(input()))
print(number)

max_number = max(number)
max_index = number.index(max(number))
print(max_number)
print(max_index+1)
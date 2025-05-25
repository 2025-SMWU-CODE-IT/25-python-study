# 문제번호: 13909
num = int(input())

# 창문의 열고 닫혀있는 상태를 나타내기 위한 리스트 생성.
array = [0] * num 

# 1의 배수번째 창문부터 해서 num의 배수의 창문까지 상태를 반대로 바꿔줌.
for i in range(1, num + 1):
    for n in range (1, num+1):
        if i*n <= num:
            if array[i * n-1] == 0:
                array[i * n-1] = 1
            else:
                array[i * n-1] = 0
        
print(array.count(1))



# 문제번호: 7785
n = int(input())

# 현재 회사에 있는 사람들의 이름을 저장할 리스트 생성.
array = []

# 이름과 출입기록을 읽을 때마다 이를 고려하여 array 리스트 수정.
for i in range(1, n+1):
    name, state = input().split()
    state = str(state)

    # 출입 기록이 "enter"이면 array리스트에 추가
    if state == "enter":
        array.append(name)

    # 출입 기록이 "leave"이고 이름이 리스트에 있다면 리스트에서 삭제.
    if state == "leave" and name in array:
        array.remove(name)

array.sort()

# 리스트의 요소들을 사전 순의 역순으로 출력.
for i in range (1, len(array)+1):
    print(array[-i])




# 문제번호: 1269
x, y = input().split()
a = [int(n) for n in input().split()]
b = [int(n) for n in input().split()]

A_B = []
B_A = []

# 집합 A-B 구하기
for i in a:
    if i not in b:
        A_B.append(i)

# 집합 B-A 구하기
for i in b:
    if i not in a:
        B_A.append(i)

# 집합 A-B와 B-A의 합집합 구하기
result = list(set(A_B + B_A))
print(len(result))



# 문제번호: 27433
n = int(input())
num = 1

# 루프를 돌면서 1부터 n까지의 수를 차례로 곱한다.
for i in range(1, n+1):
    num = num*i

print(num)



# 문제번호: 2559
N, K = input().split()
N = int(N)
K = int(K)

# N일간의 온도를 저장하는 리스트.
temp = [int(n) for n in input().split()]

array = []
for i in range(1, N-K+2):
    num = 0

    # 연속 K일간의 온도합 구하기
    for n in range(1, K+1):
        num += temp[n-i]
        array.append(num)

print(max(array))


# 문제번호: 20920
N, M = input().split()
N = int(N)
M = int(M)

# key값으로 단어를 가지고 value값으로 단어의 빈도수를 가지는 딕셔너리 생성.
storage = dict()

for i in range(1, N+1):
    word = input()

    # 단어의 길이가 M이상인 단어만 취급.
    if len(word)>=M:

        # 단어가 이미 딕셔너리에 저장되어 있다면 빈도수에 1을 더함
        if word in storage:
            storage[word] += 1
        
        # 처음 등장한 단어의 경우, 새로운 key-value쌍이 딕셔너리에 추가됨.
        else:
            storage[word] = 1
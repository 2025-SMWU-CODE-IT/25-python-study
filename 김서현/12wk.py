#13909번 창문닫기
#열려 있는 창문 구하기 
#창문이 열려있으려면 약수의 개수가 홀수여야 하므로, 약수의 개수가 홀수인 수는 제곱수 밖에 없어서 이를 기반으로 푼다.

n = int(input())
count = 0 #열려 있는 창문의 개수를 세기 위한 변수다.

i = 1 #1부터 시작해서 제곱수를 본다.
while i * i <= n: #n보다 제곱수가 같거나 작을 때까지만 반복한다.
    count += 1 #열려 있는 창문이 하나 있을 때 카운트의 개수를 하나 증가시킨다.
    i += 1 #다음 제곱수 확인용

print(count) #최종 개수 출력


#7785번 회사에 있는 사람 
#현재 회사 남아 있는 사람들의 이름 사전 역순으로 출력

n = int(input())
comp = set() #사람들 이름 저장할 집합을 만든다 

for _ in range(n): 
    name, action = input().split() #이름과 행동을 공백 기준으로 나눠 변수에 저장한다.
    if action == "enter": #action이 enter이면 
        comp.add(name) #set에 이름을 더한다 
    else:
        comp.remove(name) #아니면 이름 지운다

for name in sorted(comp, reverse=True): #이에 남은 사람들을 사전 역순으로 정렬하고 sorted를 써서 리스트를 확인
    print(name)

#1269번 대칭 차집합 
#대칭 차집합의 원소 개수를 구한다.

a, b = input().split() #원소 개수를 확인한다.
A = input().split() #a원소 확인
B= input().split() #b원소 확인

a_set = set([int(x) for x in A]) #a를 집합으로
b_set = set([int(x) for x in B]) #b를 집합으로로

diff = a_set ^ b_set #두 집합의 대칭 차집합에 관련해
print(len(diff)) #길이 출력 


#27433번 팩토리얼2
#팩토리얼 계산 프로그램 

n = int(input())
result = 1 #어떤 수의 0팩토리얼은 1이니까 1로 시작 

for i in range(1, n + 1): #1부터 n까지 반복하면서 각 수를 result에 곱함 
    result *= i

print(result) #결과 출력


#2559번 수열 
#연속된 k일 동안 온도 합 중에 가장 큰 값을 계산하고 출력한다.

n, k = input().split()
n = int(n)
k = int(k)

temp = [int(x) for x in input().split()]
#온도 리스트를 문자열로 받아서 정수로 바꿔서 리스트로 저장함

win = sum(temp[:k]) #k일의 합 구해서 이에 저장
ma = win #초기값으로 설정 

for i in range(k, n):
    win = win - temp[i - k] + temp[i]
    if win > ma:
        ma = win
#합을 계속 확인하면서 최댓값 비교하고 변화가 있을 경우 바꾼다.
print(ma) #가장 큰 k일 간 합 출력 


#20920번 영단어 암기는 괴로워


n_m = input().split()
n = int(n_m[0])
m = int(n_m[1])

words = []
for _ in range(n):
    words.append(input().rstrip())

W = {}
for word in words:
    if len(word) < m:
        continue
    if word in W:
        W[word] += 1
    else:
        W[word] = 1

def sort_key(item):
    word = item[0]
    count = item[1]
    return (-count, -len(word), word)

sw = sorted(W.items(), key=sort_key)

for word, _ in sw:
    print(word)
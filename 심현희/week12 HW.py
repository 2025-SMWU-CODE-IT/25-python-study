#13909 창문 닫기
n = int(input())
if n == 1 : print(1) #밑의 for문에서 1은 판별할 수 없으므로 if문와 else문을 사용하여 따로 처리한다.
else :
    for i in range(n) : 
        if i**2 <= n < (i+1)**2 : #창문이 열려있는 수는 제곱수마다 하나씩 늘어나므로 제곱수 사이일 때 같거나 작은 제곱수의 제곱 전의 값을 출력한다.
            print(i)
            break #출력한 뒤에는 for문을 빠져나온다.

#7785 회사에 있는 사람
n = int(input())
people = {}
for i in range(n) : #n의 수만큼 반복한다.
    name, work = input().split()
    people[name] = work #이름을 key로, 출근여부를 value로 하는 쌍을 추가한다.
    if people[name] == 'leave' : #value값이 'leave'이면 해당 쌍을 삭제한다.
        del people[name]
P = list(people.keys())#key값만을 리스트로 만든다.
P.sort()#알파벳 순서대로 정렬한 후
P.reverse()#리스트를 뒤집는다.
for k in P :#for문을 사용하여 리스트를 반복하며 요소를 차례대로 출력한다.
    print(k)

#1269 대칭 차집합
a, b = input().split()
a = int(a)
b = int(b)
#집합을 리스트로 입력받은 후 set()을 사용하여 집합으로 바꾼다.
A = set([int(n) for n in input().split()])
B = set([int(n) for n in input().split()])
#집합의 합집합, 교집합 기호를 이용하여 대칭차집합을 구한다.
result = (A - B) | (B - A)
print(len(result))

#27433 팩토리얼2
N = int(input())
sum = 1 #곱하기이므로 처음 값을 1로 설정한다.
if N == 0 : print(1) #N의 값이 0이면 1을 출력한다.
else : 
    for i in range(N) : #N의 수만큼 반복하며 sum에 수를 1씩 늘려가며 곱한다.
        sum = sum * (i + 1) #i는 0으로 시작하므로 (i + 1)을 곱한다.
    print(sum)

#2559 수열
n, k = map(int, input().split())
temp = [int(i) for i in input().split()]
temp_list = []
sum = 0
for i in range(k) : #k번 반복하며 기본 sum을 만든다.
    sum = sum + temp[i]
temp_list.append(sum)
for q in range(n-k) : #기본 sum에 맨 앞을 빼고 맨 뒤의 +1 인덱스의 값을 더한 후 이를 temp_list에 추가한다.
    sum = sum - temp[q] + temp[q+k]
    temp_list.append(sum)
print(max(temp_list)) #temp_list 중 최댓값을 출력한다.

#20920 영단어 암기는 괴로워
N, M = input().split()
N = int(N)
M = int(M)
wordlist = []
for i in range(N) :
    word = input()
    if len(word) >= M :
        wordlist.append(word)
wordset = list(set(wordlist))
wordset_num = []
for j in range(len(wordset)) :
    wordset_num.append(wordlist.count(wordset[j]))
wordset_num.sort()
for n in range(len(wordset)) :
    for k in range(len(wordset)) :
        if wordlist.count(wordset[n]) == wordset_num[k] :
            wordset[k] = wordset[n]
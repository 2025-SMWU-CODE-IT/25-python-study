#문제: 13909(창문닫기)
n = int(input())
#창문이 어떤지 리스트 생성
window = [0] * (n + 1)
for person in range(1, n + 1):
    # 창문확인하기
    i = person
    while i <= n:
        if window[i] == 0:
            window[i] = 1
        else:
            window[i] = 0
        i = i + person  # 배수이므로 증가
# 창문이 몇개가 열려있는지 확인
result = 0
for i in range(1, n + 1):
    if window[i] == 1:
        result = result + 1
print(result)

#문제: 7785(회사에 있는 사람)
n = int(input())
#회사에 누가 있는지 입력
company = set()
#이름과 그 사람의 행동 입력
for _ in range(n):
    name, action = input().split()
#회사에 들어왔으니까 추가
    if action == "enter":
        company.add(name)
#회사에 나가면 제거
    else:
        company.remove(name)
people = list(company)
people.sort() #오름차순으로 정리
for p in people:
    print(p)

#문제: 1269(대칭 차집합)
# 각각 집합의 원소가 몇개인지 입력
a_b_input = input()
a_b_list = a_b_input.split()
a = int(a_b_list[0])
b = int(a_b_list[1])
# 집합 A 원소 
a_input = input()
a_str_list = a_input.split()
a_list = []
for i in a_str_list:
    a_list.append(int(i))
# 집합 B 원소
b_input = input()
b_str_list = b_input.split()
b_list = []
for i in b_str_list:
    b_list.append(int(i))
#차집합 계산하기
a_set = set(a_list)
b_set = set(b_list)
# A에만 있는 원소
only_a = a_set - b_set
# B에만 있는 원소
only_b = b_set - a_set
result = len(only_a) + len(only_b)
print(result)

#27433(팩토리얼2)
# 숫자 입력
n = int(input())
# 변수 만들기
result = 1
# 1부터 n까지 곱해주기(팩토리얼)
for i in range(1, n + 1):
    result = result * i
print(result)

#2559(수열)
# 날짜수, 일수 입력
n, k = input().split()
n = int(n)
k = int(k)
# 온도를 리스트로 만들기
temp = input().split()
for i in range(len(temp)):
    temp[i] = int(temp[i])
# 맥시멈 합을 저장해줌
max_sum = -999999
# k일동안 합 구하고 최댓값도 찾기
for i in range(n - k + 1):  
    now = 0  # 합을 저장하는 변수
    for j in range(i, i + k):  
        now = now + temp[j]
    if now > max_sum:  # 최댓값보다 값이 크면 변환하기
        max_sum = now
print(max_sum)

#문제: 20920(영단어 암기는 어려워)
# 단어개수와 외울 길이
n, m = input().split()
n = int(n)
m = int(m)
# 딕셔너리 생성하기
words = {}
# 단어들을 저장하기
for _ in range(n):
    w = input()
    if len(w) < m:
        continue
    if w in words:
        words[w] += 1
    else:
        words[w] = 1

# 단어 정렬하기
result = sorted(words, key=lambda w: (-words[w], -len(w), w))
for w in result:
    print(w)
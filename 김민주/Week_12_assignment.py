#13909, 창문 닫기

#문제는 n 이하의 수 중에서 제곱수가 몇개인지 아는게 핵심. 특히 제곱수의 최대값 찾는게 핵심!
def sqrt(n):
    i = 1
    while i ** 2 <= n:
        i += 1
    # i가 조건을 넘긴 순간은 i**2 > N이 되는 시점이므로,
    # 그 직전의 i - 1이 N 이하인 가장 큰 제곱수의 근이 됨
    return i - 1

N = int(input())
print(sqrt(N))

#7785, 회사에 있는 사람
n = int(input())  # 출입 기록의 수
company = set()   # 회사에 있는 사람들을 저장할 집합

for _ in range(n):
    record = input().split()
    name = record[0]
    action = record[1]

    if action == "enter":
        company.add(name)     # 출근한 사람은 회사 명단에 추가
    else: 
        company.remove(name)  # 퇴근한 사람은 명단에서 제거

# 문제 조건에 따라, 사전 역순으로 이름을 정렬해 출력
# sorted()는 기본적으로 오름차순이므로, reverse=True로 내림차순 정렬함
for name in sorted(company, reverse=True):
    print(name)


#1269, 대칭 차집합
a, b = input().split()
a = int(a)
b = int(b)

# 입력받은 문자열을 공백 기준으로 나누고 int로 변환해서 집합합으로 만듦
A = set(int(n) for n in input().split())
B = set(int(n) for n in input().split())

# 대칭 차집합은 (A - B)와 (B - A)의 합집합임
result = (A - B) | (B - A)

# 원소 개수 출력
print(len(result))


#27433
N = int(input())

result = 1  # 곱셈의 항등원으로 초기값 설정 (0! = 1이니까)

# 1부터 N까지 차례대로 곱해주면 N!이 됨
i = 1
while i <= N:
    result = result * i
    i = i + 1

print(result)  # 최종 결과 출력

#2559
N, K = [int(n) for n in input().split()]
temps = [int(n) for n in input().split()]

# 처음 K일 동안의 온도 합을 구한다
current = 0
for i in range(K):
    current += temps[i]

max = current

# i번째 구간 합 = 이전 구간 합 - 구간 앞  + 새로 들어온 
for i in range(K, N):
    current = current - temps[i - K] + temps[i]
    # 최대 합보다 크면 갱신
    if current > max:
        max = current

print(max)

#20920
import sys

input = sys.stdin.readline  # 기본 input() 대신에 빠른 입력 함수로 변경

n, m = input().split() # 단어 개수 n과 외울 단어 최소 길이 m 입력받기
n = int(n)
m = int(m)

freq = {} # 단어 빈도수를 저장할 딕셔너리 생성

for _ in range(n):
    word = input().rstrip() # 단어 입력받고 오른쪽 공백 제거
    if len(word) < m: # 단어 길이가 기준 미만이면 무시
        continue
    freq[word] = freq.get(word, 0) + 1# 딕셔너리에 단어 출현 횟수 누적

# 단어장 정렬: (1) 빈도수 내림차순, (2) 길이 내림차순, (3) 사전 오름차순
result = sorted(freq.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

# 결과를 한꺼번에 출력: 단어만 출력, 각 단어는 한 줄에 하나씩
print('\n'.join(word for word, _ in result))


#13909 창문 닫기
#방법1(메모리 초과)
N = int(input())
a = []
for i in range(N):#1번째 사람이 모두 창문을 연다
    a.append(1)
for j in range(2,N+1):
    for k in range(N//j):
        b = j * (k + 1)#몇번째 자리수의 사람의 배수를 구해 그 자리의 문 여닫기를 한다
        if a[b-1] == 1:
            a[b-1] = 0
        else:
            a[b-1] = 1
print(a.count(1))
#방법2
N = int(input())
print(int(N**0.5))#결과를 보고 규칙을 찾아 구하는 방법

#7785 회사에 있는 사람
N = int(input())
a = {}#딕셔너리 생성성
for i in range(N):
    name, log = input().split()
    if log == 'enter':#로그가 출입이면 딕셔너리에 추가가
        a[name] = log
    elif log == 'leave':#퇴근이면 삭제제
        del a[name]
for name in sorted(a.keys(), reverse=True):#딕셔너리의 사람 이름을 가져와서, 알파벳 역순으로 정렬렬
    print(name)

#1269 대칭 차집합
#방법1(시간 초과)
num_A, num_B = [int(n) for n in input().split()]
A = [int(n) for n in input().split()]
B = [int(n) for n in input().split()]
a = []#대칭 차집합을 넣을 빈 리스트 생성성
for i in A:
    if i not in B and i not in a:
        a.append(i)
for j in B:
    if j not in A and i not in a:
        a.append(j)
print(len(a))
#방법2
num_A, num_B = [int(n) for n in input().split()]
A = set(int(n) for n in input().split())#set함수를 이용하여 중복을 제거하고 빠르게 연산한다다
B = set(int(n) for n in input().split())
print(len(A-B)+len(B-A))

#27433 팩토리얼2
N = int(input())
a = 1#곱할 수
if N == 0:
    print(1)
else:
    for i in range(1, N+1):
        a *= i#1씩 늘려가며 곱한다다
    print(a)

#2559 수열
N, K = [int(n) for n in input().split()]
T = [int(n) for n in input().split()]
a = []#합한 값을 넣을 빈 리스트트
for i in range(N+1-K):
    b = 0#b초기화
    for j in range(K):
        b += T[i+j]#더함함
    a.append(b)
print(max(a))

#20920 영단어 암기는 괴로워
N, M = [int(n) for n in input().split()]
a = {}#키:단어, 값:빈도수수
for i in range(N):
    b = input()#단어를 입력받음
    if len(b) < M:
        continue
    if b in a:#입력받은 단어가 키에 있다면 값 변경경
        a[b] += 1
    else:#없다면 딕셔너리 추가가
        a[b] = 1
#정렬(딕셔너리를 튜플 리스트화한 후 빈도수 내림차순, 단어 길이 내림차순, 알파벳 오름차순 순으로 정렬렬)
c = sorted(a.items(), key = lambda x : (-x[1], -len(x[0]), x[0]))
#정렬된 단어 튜플 리스트에서 단어만 출력력
for word, j in c:
    print(word)
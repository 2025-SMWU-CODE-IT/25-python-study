#5597 과제 안 내신 분..?

#number리스트에 30명 리스트 추가
number = []
for i in range(1, 31):
    number.append(i)

#숫자 입력받고 해당 숫자 리스트에서 삭제
for p in range(28):
    q = int(input())
    number.remove(q)
#결과 출력   
print(number[0])
print(number[1])


#1546 평균 
#점수와 과목 수 입력
Count= int(input())
Score = input().split(' ', Count)

#점수 리스트 int 전환
for i in range(Count): 
    Score[i] = int(Score[i])

#가장 잘 본 성적 추출
M = max(Score)
total = 0

#새로운 평균 계산 
for i in range(Count):
    Score[i] = int(Score[i]) / M * 100
    total += Score[i]

print(total/Count)

#2444 별 찍기-7
#별 개수 입력
N = int(input())

for i in range(N):
    print(' ' * (N-i-1), '*'*(2*i+1))

for i in range(N-1):
    print(' ' * (i+1), '*'*(2*(N-i)-3))

#2501 약수 구하기 
Q =  input().split(' ', 2)
N = int(Q[0])
S = int(Q[1])

P = []
for i in range(1, N+1): 
    if N % i == 0: 
        P.append(i)

print(P[S-1])


#10773 제로 
#숫자 입력 및 리스트 요소 추가
K = int(input())
S = []

for i in range(K):
    S.append(int(input()))

#0의 인덱스를 받고 리스트 내에서 0과 앞 숫자를 제거
while True:
    try: 
        T = int(S.index(0))
        del S[T]
        del S[T-2]
        
#index는 0이라는 값이 없으면 오류 발생시키기 때문에 예외처리로 반복문 탈출     
    except ValueError: 
        break
#합 계산 및 출력
total = 0
for i in S: 
    total += i
print(total)    


#17256 달달함이 흘러넘쳐
#숫자 입력
A = input().split(' ', 3)
C = input().split(' ', 3)
B = [0,0,0]

#b의 각 요소 계산
B[0] = int(C[0])-int(A[2])
B[1] = int(C[1])//int(A[1])
B[2] = int(C[2])-int(A[0])
#출력
print(B[0], B[1], B[2])
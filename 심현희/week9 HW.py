#5597 과제 안 내신 분...?
people = []
people_list = [int(n) for n in range(1,31)] #모든 학생의 출석번호가 담긴 리스트를 만든다.
j = 0
while j < 28 :
    people.append(int(input())) #제출자의 출석번호를 people리스트에 추가한다.
    j = j + 1
k = 0
while k < 28 :
    people_list.remove(people[k]) #모든 학생의 출석번호가 담긴 리스트에서 people리스트의 각 요소에 해당하는 출석번호를 제거한다.
    k = k + 1
print(people_list[0])
print(people_list[1])
#1546 평균
test_num = int(input())
grade = [int(n) for n in input().split()]
M = max(grade) #점수 중에 최댓값을 구한다.
sum = 0
i = 0
while i < test_num: #점수를 수정한 후 모든 점수를 더한다.
    grade[i] = grade[i]/M*100 
    sum = sum + grade[i]
    i = i + 1
average = sum/test_num #점수를 시험 본 과목의 개수로 나눈다.
print(average)
#2444 별 찍기-7
N = int(input())
i = 1
while i < N*2 : #별의 수를 2씩 늘리면서 출력한다.
    star = str('*'*i)
    print(star.center(N*2-1).rstrip())#별을 최대값을 기준으로 가운데 정렬한 후 오른쪽 공백을 제거한다.
    i = i + 2
    if i == N*2 - 1 : #별이 최댓값이 되었을 때 2씩 줄인다.
        while i > 0:
            star = str('*'*i)
            print(star.center(N*2-1).rstrip())
            i = i - 2
        break #별이 계속 출력되지 않도록 break를 사용하낟.
#2501 약수 구하기
N, k = input().split()
N = int(N)
k = int(k)
factor= []
i = 1
while i <= N :
    if N%i == 0 : # 약수이면 factor리스트에 추가한다.
        factor.append(i)
    i = i + 1
num = len(factor)
if k <= num : #k가 factor리스트의 개수보다 작을 때 출력하고 그렇지 않으면 0이 출력되도록 한다.
    print(factor[k-1])
else : print(0)
#10773 제로
k = int(input())
writelist= []
for i in range(k):
    i = int(input())
    if i != 0 : #0이 아니라면 writelist리스트에 추가한다.
        writelist.append(i)
    if i == 0 : #0이라면 writelist리스트의 개수를 센 후 가장 끝의 요요소와 같은 수를 지운다. 합을 구하는 문제이므로 같은 수를 가진진 요소 아무거나 지워도 상관없다.
        n = len(writelist)
        writelist.remove(writelist[n-1])
q = len(writelist)
sum = 0
for w in range(q) :
    sum = sum + writelist[w]
print(sum)
#17256 달달함이넘쳐흘러

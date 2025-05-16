#5597 과제 안 내신 분...?
people_list = [int(n) for n in range(1,31)] #모든 학생의 출석번호가 담긴 리스트를 만든다.
for j in range(28) : #제출자의 출석번호를 입력받은 후 해당 번호를 모든 학생의 출석번호가 담긴 리스트에서 제거한다.
    k = int(input()) 
    if k in people_list :
        people_list.remove(k)
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
    print(star.center(N*2-1).rstrip())#별을 최대값을 기준으로 center()함수를 사용하여 가운데 정렬한 후 오른쪽 공백을 제거한다.
    i = i + 2
    if i == N*2 - 1 : #별이 최댓값이 되었을 때 2씩 줄인다.
        while i > 0:
            star = str('*'*i)
            print(star.center(N*2-1).rstrip())
            i = i - 2
        break #별이 계속 출력되지 않도록 break를 사용한다.
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
for j in range(k): #수를 하나씩 입력받는다. 
    j = int(input())
    if i != 0 : #0이 아니라면 writelist리스트에 추가한다.
        writelist.append(j)
    else : #0이라면 pop함수를 사용하여 writelist리스트의 가장 끝의 요소를 지운다.
        writelist.pop()
q = len(writelist)
sum = 0
for w in range(q) : #리스트의 개수만큼 반복하면서 합을 구한다.
    sum = sum + writelist[w]
print(sum)
#17256 달달함이넘쳐흘러
a,b,c = input().split()
d,e,f = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)
e = int(e)
f = int(f)
class Cake:
    def __init__(self, a, b, c, d, e, f) : #__init__를 사용하여 초기값을 받는다.
        self.b1 = d - c # 각 연산에 맞는 값을 지정해준다.
        self.b2 = e // b
        self.b3 = f - a
        print(self.b1,self.b2,self.b3)
yummy = Cake(a,b,c,d,e,f) #클래스Cake의 인스턴스yummy를 만들어서 프로그램을 실행한다.
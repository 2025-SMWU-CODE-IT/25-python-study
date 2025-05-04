#문제5597(과제 안 내신 분..?)
#1~30번 까지의 학생을 리스트로 만듭니다. 
student = list(range(1,31))
#제출한 학생 수가 28명이므로 28명의 번호를 입력받게 합니다.
for i in range (28):
    n = int(input("제출한 사람의 출석번호를 입력"))
    #제출한 28명을 리스트에서 제외하도록 합니다.
    student.remove(n)
student.sort() #제출하지 않은 사람들의 번호를 오름차순으로 정리합니다.
print("제출 안 한 사람 학생의 번호를 써주세요")
print(student[0])
print(student[1])

#문제1546(평균)
#시험 본 과목의 개수를 입력합니다
n = int(input("과목 개수 입력"))
score_input = input("과목의 점수를 입력")
score_list = score_input.split() #입력받은 과목의 점수를 띄어쓰기를 기준으로 리스트로 구분해줍니다.
scores = [] 
for i in score_list:
    scores.append(int(i)) #입력된 점수를 정수형으로 바꿔주고 리스트에 추가해줍니다.
max_score = max(scores)
total = 0 #총점의 초기값을 0으로 맞춰줍니다.
for i in scores:
    total += i / max_score * 100
average = total / n #과목들의 평균을 계산해줍니다.
print(average)

#문제2444(별찍기)
n = int(input("숫자를 입력해주세요"))
#위에 그려진 별
#for 문을 사용해서 공백과 별을 이용해서 위에 있는 별을 표현해줍니다.
for i in range(1, n+1):
    print(" " * (n-1) + "*" * (2 * i -1))
#아래쪽에 그려진 별
#위와 마찬가지로 for문을 사용해서 공백과 별을 이용해서 아래에 있는 별을 표현해줍니다.
for i in range(n-1, 0, -1):
    print(" " * (n-1) + "*" * (2 * i-1))

#문제2501(약수구하기)
n, k= input("숫자를 입력하세요").split() #입력된 숫자를 구분해줍니다
#n과 k를 정수형으로 받아줍니다.
n = int(n)
k = int(k)
#약수개수를 0이라고 둡니다.
measure = 0
#약수를 확인해주는데, 이때 1씩 증가하면서 확인해줍니다.
for i in range(1, n+1):
    if n % i: #약수가 아니면 계속 계산해줍니다.
        continue
    measure += 1 #약수라는 뜻이므로 1씩 증가해줍니다.
    if measure == k: #약수가 k번째이면 종료합니다. 
        print(i)
        break
if measure < k: #약수가 k보다 작으면 0을 출력해줍니다.
    print(0)

#문제10773(제로)
k = int(input("수를 입력하세요"))
number = [] #빈 리스트를 만들어줍니다.
index = 0 #인덱스를 0으로 초기에 설정해줍니다. 
for i in range(k): #k번만큼 반복하도록 for문을 만들어줍니다.
    n = int(input())
    if n == 0: #0이 입력되었을때는 가장 최근에 입력된 수를 지웁니다.
        index -= 1
    else :  #0이 아닌 숫자가 입력되었다면 저장해줍니다.
        if index < len(number): #인덱스가 리스트보다 적으면 이미 값이 있다는 말입니다.
            number[index] = n
        else : #리스트에 아직 없으면 새 숫자를 리스트에 추가해줍니다.
            number.append(n)
        index += 1 #리스트에 1 더해주어 다음으로 넘어가줍니다.
total = 0 #초기 총합을 0으로 지정해줍니다. 
for i in range(index):
    total += number[i] #total에 각각의 숫자를 더해줍니다.
print(total)

#문제17256(달달함이 넘쳐흘러)
class cake: #클래스 생성
    def __init__(self, x, y, z): #생성된 클래스에 케이크 위치를 저장할 수 있습니다.
        self.x = x #각각 입력받은 수를 x,y,z에 저장합니다.
        self.y = y
        self.z = z
a_input = input("a의 x y z를 입력하세요")
a_split = a_input.split() #입력받으면 공백으로 수를 나눕니다. 
ax = int(a_split[0]) #입력받은 수를 정수로 변환하고 저장해줍니다.
ay = int(a_split[1])
az = int(a_split[2])
c_input = input("c의 x y z를 입력하세요: ") #a와 마찬가지로 c도 해줍니다. 
c_split = c_input.split()
cx = int(c_split[0])
cy = int(c_split[1])
cz = int(c_split[2])
a = cake(ax, ay, az) #각각 a,c,를 만들어서 입력받은 값을 저장해줍니다. 
c = cake(cx, cy, cz)
for bx in range(1, 101): #1부터 100까지 b의 좌표가 설정되며 값을 찾습니다.
    for by in range(1, 101):
        for bz in range(1, 101):
            x_result = a.z + bx #케이크 공식을 이용해줍니다. 
            y_result = a.y * by
            z_result = a.x + bz
            if x_result == c.x and y_result == c.y and z_result == c.z:
                print(bx, by, bz) #c의 결과와 동일하다면 정답임을 인지합니다. 
                break
        else:
            continue
        break
    else:
        continue
    break



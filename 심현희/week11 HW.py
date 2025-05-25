#9610 사분면
n = int(input())
fourlist = [0,0,0,0,0] #AXIS, Q1, Q2, Q3, Q4의 개수를 0으로 설정한 리스트를 만든다
for i in range(n) :
    xi, yi = input().split()
    xi = int(xi)
    yi = int(yi)
    #각 사분면, 축의 조건에 맞으면 리스트의 해당 요소의 값을 +1한다.
    if xi == 0 or yi == 0:
        fourlist[0] = fourlist[0] + 1
    elif xi > 0 and yi > 0 :
        fourlist[1] = fourlist[1] + 1
    elif xi < 0 and yi > 0 :
        fourlist[2] = fourlist[2] + 1
    elif xi < 0 and yi < 0 :
        fourlist[3] = fourlist[3] + 1
    else :
        fourlist[4] = fourlist[4] + 1
print('Q1:',fourlist[1])
print('Q2:',fourlist[2])
print('Q3:',fourlist[3])
print('Q4:',fourlist[4])
print('AXIS:',fourlist[0])

#2163 초콜릿 자르기
N, M = input().split()
N = int(N)
M = int(M)
print(N*M-1) #최소 쪼개기 횟수는 N*M-1이다

#2530 인공지능 시계
hms = [int(n) for n in input().split()]
time = int(input())
total = hms[0]*3600 + hms[1]*60 + hms[2] + time #모든 시, 분, 초를 초단위로 바꾼 후 더한다.
hms[0] = total // 3600 #h는 전체 시간을 3600으로 나눈 몫이다.
total = total%3600 #전체 시간은 전체 시간을 3600으로 나눈 나머지이다.
hms[1] = total // 60 #m은 전체 시간을 60으로 나눈 몫이다.
hms[2] = total%60 #s는 전체 시간을 60으로 나눈 나머지이다.
if hms[0] >= 24 : print(hms[0]%24, hms[1], hms[2]) #시가 24이상이면 하루가 지났으므로 시를 24로 나눈 나머지를 출력하도록 한다.
else : print(hms[0], hms[1], hms[2])

#2480 주사위 세개
dice = [int (n) for n in input().split()] #주사위를 던져 나온 눈을을 리스트로 만든다.
n = len(set(dice)) #집합으로 만든 후 개수를 세 같은 눈을 가진 눈의 개수를 얻는다.
if n == 1 :
    print(10000 + 1000*dice[0])
elif n == 3 :
    print(100*max(dice))
else :
    for i in range(2) : #다른 주사위 눈의 수가 2개이므로 두 번 반복하도록 설정한다.
        if dice.count(dice[i]) == 2: #주사위 눈의 개수가 리스트에 2이면 해당 수가 같은 눈이다.
            print(1000 + 100*dice[i])
            break #같은 눈은 2개이므로 두 번 출력되지 않도록 break문을 사용하여 for문에서 빠져나온다.
        else : continue #같은 눈이 아니라면 for문을 계속진행한다.
        
#7567 그릇
dish = list(input())
height = 0
for i in range(len(dish) - 1) : #dish 리스트의 앞 요소와 뒷 요소를 앞 요소를 기준으로 비교하므로 개수보다 -1 만큼 반복한다.
    if dish[i] == dish[i+1] : #dish 리스트의 앞 요소와 뒷요소가 같으면 +5를, 다르면 +10을 한다.
        height = height + 5
    else : height = height + 10
print(10 + height) #처음 그릇의 높이 10을 더한다.

#11557 Yangjojang of The Year
T = int(input())
schol_dic = {} #학교와 술 소비량을 저장할 딕셔너리를 정의한다.
alco_list = [] #술 소비량의 최댓값을 구하기 위해 술 소비량만을 요소로 한 리스트를 정의한다.
for i in range(T): #케이스의 수만큼 반복한다.
    N = int(input())
    for j in range(N): #학교의 수만큼 반복한다.
        school, alcohol = input().split()
        alcohol = int(alcohol)
        schol_dic[alcohol] = school #술 소비량으로 학교를 알 수 있도록 술 소비량을 key로, 학교를 value로 지정하여 딕셔너리에 추가한다.
        alco_list.append(alcohol) #술 소비량을 리스트에 추가한다.
    print(schol_dic[max(alco_list)]) #술 소비량 리스트의 최댓값의 key의 value를 출력한다.
    
        





#2884
H = int(input("시간 : "))
M = int(input("분 : "))
while H > 24 or M > 60: 
    print("다시 설정 해주세요")
    H = int(input("시간 : "))
    M = int(input("분 : "))
    continue
alarm = H*60 + M - 45 #시간도 분으로 바꾼 후, 45분 빼줌.
H = alarm // 60
M = str(alarm - H*60) #아래의 프린트 문에서 :를 출력하기 위해 자료형을 문자열로 변환해줌.
H = str(H)

print(H + ":" + M)
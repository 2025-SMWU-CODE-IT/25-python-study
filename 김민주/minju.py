#2884
H = int(input("시간 : "))
M = int(input("분 : "))
while H > 24 or M > 60:
    print("다시 설정 해주세요")
    continue
alarm = H*60 + M - 45
H = alarm // 60
M = str(alarm - H*60)
H = str(H)

print(H + ":" + M)


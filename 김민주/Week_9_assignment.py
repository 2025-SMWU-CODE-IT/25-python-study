#9주차 과제
#[김민주] 2025년 1학기 python study - 9주차

#5597번 과제 안 내신 분...?
student = []

for i in range(1, 31):
    student.append(i)

for i in range(28):
    attendance = int(input())
    student.remove(attendance)

print(student[0])
print(student[1])

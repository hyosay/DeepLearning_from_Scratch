STUDENTS = 3
LESSONS = 3

grades = [[None] * LESSONS for i in range(STUDENTS)]
for i in range(STUDENTS):
    print("학생번호", (i + 1))
    for j in range(LESSONS):
        grades[i][j] = int(input(str(j + 1) + "번쨰 교과목의 점수를 입력하여라 :"))

average = [None] * STUDENTS
for i in range(STUDENTS):
    average[i] = 0
    for j in range(LESSONS):
        average[i] += grades[i][j]
    average[i] /= LESSONS

for i in range(STUDENTS):
    if average[i] > 89:
        print(average[i])
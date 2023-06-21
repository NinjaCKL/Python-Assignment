student_marks = []

for i in range(5):
    mark = float(input("Enter student mark : "))
    student_marks.append(mark)
average_mark = sum(student_marks)/len(student_marks)

if average_mark >= 50:
    print('Your Average mark is ', average_mark)
    print('PASS')
else:
    print('Your Average mark is ', average_mark)
    print("FAIL")
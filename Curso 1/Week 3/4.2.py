quantity_students = int(input("Number of students in MAC2166:"))
student_failed = 0
student_repeat = 0
student_passed = 0
student_performance = 0

for i in range(0,quantity_students):
    grade = float(input("Grade:"))
    if grade < 3:
        student_failed = student_failed + 1
    if 3 <= grade < 5:
        student_repeat = student_repeat + 1
    if 5 <= grade <= 8:
        student_passed = student_passed + 1
    if 8 < grade:
        student_passed = student_passed + 1
        student_performance = student_performance + 1

print("Total de alunos:",quantity_students)
print("Número de alunos reprovados:",student_failed)
print("Número de alunos de recuperação:",student_repeat)
print("Número de alunos aprovados:",student_passed)
print("Número de alunos com desempenho muito bom:",student_performance)

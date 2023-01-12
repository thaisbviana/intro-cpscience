quantity_students = int(input("Number of students(MAC2166):"))
all_grades = 0

for i in range(0,quantity_students):
    grade = float(input("Grade"))
    all_grades = all_grades + grade

mean = all_grades // quantity_students
print(mean)
    

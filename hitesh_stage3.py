# Stage 3 Student Grade Calculator

name = input("Enter student name: ")

marks1 = float(input("Enter marks 1: "))
marks2 = float(input("Enter marks 2: "))
marks3 = float(input("Enter marks 3: "))

total = marks1 + marks2 + marks3

percentage = (total / 300) * 100

if percentage >= 75:
    grade = "A"

elif percentage >= 60:
    grade = "B"

elif percentage >= 40:
    grade = "C"

else:
    grade = "F"

print("Name:", name)
print("Total:", total, "/300")
print("Percentage:", percentage, "%")
print("Grade:", grade)
marks1 = float(input("Enter marks of Subject 1: "))
marks2 = float(input("Enter marks of Subject 2: "))
marks3 = float(input("Enter marks of Subject 3: "))

average = (marks1 + marks2 + marks3) / 3

print("Average Marks:", average)

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
else:
    grade = "D"

print("Grade:", grade)
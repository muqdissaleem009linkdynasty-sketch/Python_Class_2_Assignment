name = input("Enter your name: ")
age = int(input("Enter your age: "))
university = input("Enter your university: ")
semester = int(input("Enter your semester: "))
cgpa = float(input("Enter your CGPA: "))

print()
print("==============================")
print("       STUDENT PROFILE")
print("==============================")

print()
print("Name:", name)
print("Age:", age)
print("University:", university)
print("Semester:", semester)
print("CGPA:", cgpa)

print()

# Age Check
if age >= 18:
    age_status = "Adult"
else:
    age_status = "Minor"

# Academic Status
if cgpa >= 3.5:
    academic_status = "Excellent"
elif cgpa >= 3.0:
    academic_status = "Good"
elif cgpa >= 2.5:
    academic_status = "Satisfactory"
else:
    academic_status = "Needs Improvement"

print("Age Status:", age_status)
print("Academic Status:", academic_status)

print()
print("AI Engineering Program:")

# Program Eligibility
if age >= 18 and semester >= 3 and cgpa >= 2.5:
    print("Eligible ✓")
else:
    print("Not Eligible ✗")

print("==============================")
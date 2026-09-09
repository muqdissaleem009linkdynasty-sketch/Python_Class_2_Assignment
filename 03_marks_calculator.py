# Student Marks Calculator

mathematics = float(input("Enter Mathematics marks: "))
programming = float(input("Enter Programming marks: "))
english = float(input("Enter English marks: "))
data_science = float(input("Enter Data Science marks: "))

total = mathematics + programming + english + data_science
average = total / 4

print("Total Marks:", total)
print("Average:", average)
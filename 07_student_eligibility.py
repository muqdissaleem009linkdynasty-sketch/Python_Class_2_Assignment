name = input("Enter your name: ")
age = int(input("Enter your age: "))
semester = int(input("Enter your semester: "))
cgpa = float(input("Enter your CGPA: "))

if age >= 18 and semester >= 3 and cgpa >= 2.5:
    print(f"Congratulations, {name}!")
    print("You are eligible for the AI Engineering program.")
else:
    print(f"Sorry, {name}.")
    print("You are not eligible for the AI Engineering program.")
age = int(input("Enter your age: "))

if age <= 12:
    print("Category: Child")
elif age <= 17:
    print("Category: Teenager")
elif age <= 59:
    print("Category: Adult")
else:
    print("Category: Senior")
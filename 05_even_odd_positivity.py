number = int(input("Enter a number: "))

if number > 0:
    print("Number is positive.")
elif number < 0:
    print("Number is negative.")
else:
    print("Number is zero.")

if number % 2 == 0:
    print("Number is even.")
else:
    print("Number is odd.")
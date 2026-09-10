# Final Challenge - Shopping Discount with Student Discount

purchase = float(input("Enter purchase amount: "))
student = input("Are you a student? (yes/no): ").lower()

if purchase < 5000:
    discount_percentage = 0
elif purchase < 10000:
    discount_percentage = 10
elif purchase < 20000:
    discount_percentage = 15
else:
    discount_percentage = 20

if student == "yes":
    discount_percentage += 5

discount_amount = purchase * discount_percentage / 100
final_amount = purchase - discount_amount

print("Original Amount:", purchase)
print("Discount:", discount_percentage, "%")
print("Discount Amount:", discount_amount)
print("Final Amount:", final_amount)
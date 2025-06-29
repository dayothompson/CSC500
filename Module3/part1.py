# This program finds the addition and subtraction of two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

addition = num1 + num2
subtraction = num1 - num2

print(f"Addition: {num1} + {num2} = {addition}")
print(f"Subtraction: {num1} - {num2} = {subtraction}")

# Ask the user for the charge of the food
food_charge = float(input("Enter the charge for the food: $"))

# Calculate tip and tax
tip_rate = 0.18
sales_tax_rate = 0.07

tip = food_charge * tip_rate
sales_tax = food_charge * sales_tax_rate

total = food_charge + tip + sales_tax

# Display the results
print(f"\nFood Charge:   ${food_charge:.2f}")
print(f"Tip (18%):    ${tip:.2f}")
print(f"Sales Tax (7%): ${sales_tax:.2f}")
print(f"-------------------------")
print(f"Total Price:   ${total:.2f}") 
print(f"-------------------------")

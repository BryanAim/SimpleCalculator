print("My Basic Calculator")

# Created from the knowledge of conditional statements

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input("Enter the operator: ")

if operator == "+":
    print("The sum is ", num1 + num2)

elif operator == "-":
    print("The difference is ", num1 - num2)

elif operator == "/":
    print("The division result is ", num1 / num2)

elif operator == "*":
    print("The multiplication result is ", num1 * num2)

else:
    print("Please enter a valid operator")

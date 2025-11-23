# match_case_calculator.py

# Step 1: Ask for the first number
num1 = float(input("Enter the first number: "))

# Step 2: Ask for the second number
num2 = float(input("Enter the second number: "))

# Step 3: Ask for the operation
operation = input("Choose the operation (+, -, *, /): ")

# Step 4: Use match case to do the math
match operation:
    case "+":
        result = num1 + num2
        print(f"The result is {result}.")

    case "-":
        result = num1 - num2
        print(f"The result is {result}.")

    case "*":
        result = num1 * num2
        print(f"The result is {result}.")

    case "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"The result is {result}.")

    case _:
        print("Invalid operation selected.")

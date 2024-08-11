# TASK-1) CALCULATOR --->

# Prompt the user to input two numbers and an operation choice.
num1 = int(input("Enter the number 1 = "))
num2 = int(input("Enter the number 2 = "))
operation = input("Enter the operation(+,-,*,/) = ")
# Perform the calculation and display the result.
match operation:
    case "+":
        print("Result =",num1+num2)
    case "-":
        print("Result =",num1-num2)
    case "*":
        print("Result =",num1*num2)
    case "/":
        print("Result =",num1/num2)
    case _:
        print("Invalid operation!")

#Lecture Activity 15 - 20min
# Simple Calculator Exercise
# We will share our code when done
# In your breakout rooms, create a basic calculator. The calculator should accept three parameters:
#
# Two numbers.
# One operator (e.g., +, -, *, /).
# Use a series of if statements to perform the appropriate operation based on the operator provided.

num1 = float(input("Enter number 1:"))
num2 = float(input("Enter number 2:"))
operator = input("Enter an operator (+, -, *, /, ^, Root):")
def calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '^':
        return num1 ** num2
    elif operator == 'Root':
        if num2 != 0:
            return num1 ** (1/num2)
        else:
            return "Error! Root of zero is undefined"
    elif operator == '/':
        if num2 == 0:
            return "Error division by zero"
        else:
            return num1 / num2
    else:
        return "Invalid operator"

result = calculator(num1, num2, operator)
print(f"The result is: {result}")


#Create a simple Python program that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).
#Perform the operation based on the user's input and print the result.
#Example: If a user inputs 10, 5, and +, your program should display 10 + 5 = 15.
number_1 = int(input("Enter your first number: "))
number_2 = int(input("Enter your second number: "))
sign = input("Enter the operator you wish to use (+,-,/,* etc): ")
if sign == "*":
    result = number_1 * number_2
    print(f"{number_1} * {number_2} = {result}")
elif sign == "+":
    result = number_1 + number_2
    print(f"{number_1} + {number_2} = {result}")
elif sign == "-":
    result = number_1 - number_2
    print(f"{number_1} - {number_2} = {result}")
elif sign == "/":
    if number_2 != 0:
        result = number_1 / number_2
        print(f"{number_1} / {number_2} = {result}")
    else:
        print("division by 0 is not allowed")
else:
    print("Invalid operation. Please use one of +, -, *, or /.")
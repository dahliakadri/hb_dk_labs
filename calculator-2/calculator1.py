"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# read-evaluate-print-loop

print("Welcome to the caluculate app")
print("Please type in your data with infix notation")
print("As an example please input + 1 2, to evaluate 1 + 2")
print("Thank you!")

while True:

    user_input = input("Enter evaluation > ")
    user_tokens = user_input.split(" ")

    operator = user_tokens[0]


    if operator == "q":
        print("Exiting program")
        break

    if len(user_tokens) == 2:

        num1 = float(user_tokens[1])

        if operator == "square":
            print(square(num1))
            continue

        elif operator == "cube":
            print(cube(num1))
            continue

    elif len(user_tokens) == 3:
    
        num2 = float(user_tokens[2])

        if operator == "+":
            print(add(num1,num2))
            
        elif operator == "-":
            print(subtract(num1,num2))
            
        elif operator == "*":
            print(multiply(num1,num2))

        elif operator == "/":
            print(divide(num1,num2))

        elif operator == "pow":
            print(power(num1,num2))

        elif operator == "mod":
            print(mod(num1,num2))

    else:
        print("please input correct form")





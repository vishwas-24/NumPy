# PYTHON CALCULATOR
operator = input("Enter operator (+ - * /) : ")
num1 = float(input("Enter first number : "))
num2 = float(input("Enter second number : "))
if operator == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {round(result, 2)}")
elif operator == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {round(result, 2)}")
elif operator == "*":
    result = num1 * num2
    print(f"{num1} X {num2} = {round(result, 2)}")
elif operator == "/":
    result = num1 / num2
    print(f"{num1} / {num2} = {round(result, 2)}")
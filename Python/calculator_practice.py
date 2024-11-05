#Variable declarations
operator = input("Enter an operator (+ - * /):")
num1 = float(input("Enter the 1st number:  "))
num2 = float(input("Enter the 2nd number:  "))

#If else statements for conducting math operation, rounded to 3 decimal places
if operator == "+":
    result = num1 + num2
    print(round(result, 3))
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
elif operator == "*":
    result = num1 * num2
    print(round(result, 3))
elif operator == "/":
    result = num1 / num2
    print(round(result, 3))
#Invalid data types for operator
else:
    print(f"{operator} is not a valid operator")
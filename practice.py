try:
    num1 = float(input("Enter 1st number:"))
    operatot =input("Enter operator (+, -, *, /):")
    if operatot not in ['+', '-', '*', '/']:
        raise ValueError("Invalid operator. Please enter one of +, -, *, /.")
    else:
        num2 = float(input("Enter 2nd number:"))
    
    if operatot == '+':
        result = num1 + num2
    elif operatot == '-':
        result = num1 - num2
    elif operatot == '*':
        result = num1 * num2
    elif operatot == '/':
        if num2 == 0:
            raise ValueError("Cannot divide by zero.")
        result = num1 / num2
    print(f"Result: {result}")
    
except ValueError:
    print("Invalid input. Please enter a number.")
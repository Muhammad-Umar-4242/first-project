try:
    num1 = float(input(" Enter first number: "))
    operator = input(" Choose mathematical operator ( + , - , * , / , % ): ")

    if operator not in ["+","-","*","/","%"]:
        print("You have chosen an invalid operator:", operator)
    else:
        num2 = float(input(" Enter second number: "))

        if operator == "+":
            print("Sum of 1st & 2nd number is:", num1 + num2)

        elif operator == "-":
            print("Subtraction of 2nd number from 1st number is:", num1 - num2)

        elif operator == "/":
            if num2 != 0:
                print("Division of 1st & 2nd number is:", num1 / num2)
            else:
                print("Error, cannot divide by 0")

        elif operator == "*":
            print("Multiplication of 1st & 2nd number is:", num1 * num2)

        elif operator == "%":
            print("Remainder is:", num1 % num2)

except ValueError:
    print("You have entered invalid number!")

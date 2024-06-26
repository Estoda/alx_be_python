num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
oper = input("Choose the operation (+, -, *, /): ")

match oper:
    case '+':
        print("The result is", str(num1 + num2) + '.')
    case '-':
        print("The result is", str(num1 - num2) + '.')
    case '*':
        print("The result is", str(num1 * num2) + '.')
    case '/':
        if num2 == 0:
            print("Cannot dividde by zero.")
        else:
            print("The result is", str(num1 / num2) + '.')
    case _:
        print("Wrong input.")



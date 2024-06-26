num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
oper = input("Choose the operation (+, -, *, /): ")
result = 0
end = True

match oper:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        if num2 == 0:
            print("Cannot dividde by zero.")
            end = False
        else:
            result = num1 / num2
    case _:
        print("Wrong input.")

if(end):
    print(f"The result is {result}")


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
oper = input("Choose the operation (+, -, *, /): ")
result = ""
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
        else:
            result = num1 / num2
            end = False
    case _:
        print("Wrong input.")
        
if(not end):
    print(f"The result is {result}")


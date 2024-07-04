FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    global celsius
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{fahrenheit}°F is {celsius}°C")

def conver_to_fahrenheit(celsius):
    global fahrenheit
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    print(f"{celsius}°C is {fahrenheit}°F")

def main():
    temperature = float(input("Enter the temperature to convert: "))
    type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
    if type == "C":
        conver_to_fahrenheit(temperature)
    elif type == "F":
        convert_to_celsius(temperature)
    else:
        print("Invalid type. Try again")

if __name__ == "__main__":
    main()

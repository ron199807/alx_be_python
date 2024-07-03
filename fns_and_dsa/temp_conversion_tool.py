#TEMP_CONVERSION_TOOL.PY

#GLOBAL CONVERSION FACTORS
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    #convert temp from fahrenheit to celsius
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR 

def convert_to_fahrenheit(celsius):
    #convert temp from celsius to fahrenheit
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def main():
    try:

        temperature = float(input("Enter the temperature to convert: "))
        scale = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().lower()

        if scale == 'c':
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp:.2f}°F")
        elif scale == "f":
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp:.2f}°C")
        else:
            print("Invalid scale. please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")



if __name__ == "__main__":
    main()


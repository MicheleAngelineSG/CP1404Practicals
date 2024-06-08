"""
FUNCTION celsius_to_fahrenheit(celsius)
    RETURN celsius * 9 / 5 + 32

FUNCTION fahrenheit_to_celsius(fahrenheit)
    RETURN (fahrenheit - 32) * 5 / 9

FUNCTION main()
    PROMPT user to enter temperature in Celsius
    READ temperature_celsius from user
    SET temperature_fahrenheit to celsius_to_fahrenheit(temperature_celsius)
    DISPLAY temperature_fahrenheit

    PROMPT user to enter temperature in Fahrenheit
    READ temperature_fahrenheit from user
    SET temperature_celsius to fahrenheit_to_celsius(temperature_fahrenheit)
    DISPLAY temperature_celsius

IF __name__ EQUALS "__main__" THEN
    CALL main()
"""
def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def main():
    temperature_celsius = float(input("Enter temperature in Celsius: "))
    temperature_fahrenheit = celsius_to_fahrenheit(temperature_celsius)
    print("Temperature in Fahrenheit:", temperature_fahrenheit)

    temperature_fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    temperature_celsius = fahrenheit_to_celsius(temperature_fahrenheit)
    print("Temperature in Celsius:", temperature_celsius)

if __name__ == "__main__":
    main()

# Get the unit from the user
given_unit = input("What unit are you trying to convert right now?\nGive the answers in the following (C/K/F)\n").upper()

# Check if the unit is valid
while given_unit not in ['C', 'K', 'F']:
    print("Invalid unit. Please enter C, K, or F.")
    given_unit = input("What unit are you trying to convert right now?\nGive the answers in the following (C/K/F)\n").upper()

# Get the temperature from the user
temp = float(input("Enter the temperature\n"))

# Define a function to convert Celsius to other units
def convert_from_celsius(temp):
    kelvin = temp + 273.15
    fahrenheit = (temp * 9/5) + 32
    return kelvin, fahrenheit

# Define a function to convert Kelvin to other units
def convert_from_kelvin(temp):
    celsius = temp - 273.15
    fahrenheit = (celsius * 9/5) + 32
    return celsius, fahrenheit

# Define a function to convert Fahrenheit to other units
def convert_from_fahrenheit(temp):
    celsius = (temp - 32) * 5/9
    kelvin = celsius + 273.15
    return celsius, kelvin

# Convert the temperature to all other units
if given_unit == 'C':
    kelvin, fahrenheit = convert_from_celsius(temp)
    print(f"{temp} degrees Celsius is equal to:")
    print(f"{kelvin} Kelvin")
    print(f"{fahrenheit} degrees Fahrenheit")
elif given_unit == 'K':
    celsius, fahrenheit = convert_from_kelvin(temp)
    print(f"{temp} Kelvin is equal to:")
    print(f"{celsius} degrees Celsius")
    print(f"{fahrenheit} degrees Fahrenheit")
elif given_unit == 'F':
    celsius, kelvin = convert_from_fahrenheit(temp)
    print(f"{temp} degrees Fahrenheit is equal to:")
    print(f"{celsius} degrees Celsius")
    print(f"{kelvin} Kelvin")

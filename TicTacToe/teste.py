def celsius_to_fahrenheit(temperature):
    if temperature < -273.15:
        return "Incorrect value!"
    return temperature * 9.0/5.0 + 32.0


print(celsius_to_fahrenheit(-274))

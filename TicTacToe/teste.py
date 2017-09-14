def celsius_to_fahrenheit(temperature):
    if temperature < -273.15:
        return "That temperature doesn't make sense!"
    return temperature * 9.0/5.0 + 32.0


temperatures = [10,-20,-289,100]
for temperature in temperatures:
    print(celsius_to_fahrenheit(temperature))

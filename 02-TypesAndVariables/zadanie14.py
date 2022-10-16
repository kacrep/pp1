#Write a program that reads the temperature in degrees Celsius from the keyboard. The program then calculates and displays the temperature in Kelvin and Fahrenheit.

celsius=float(input("Podaj temperature w C:"))
kelvin = celsius + 273.15
fahrenheit = celsius * 1.8 + 32

print(f"{celsius}C = {kelvin}K = {fahrenheit}F")
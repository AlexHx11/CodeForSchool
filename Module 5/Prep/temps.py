# Alex Ha
# 2543681
# COP1000

"""
Psuedocode

Define a function that converts the temperature from Fah to Cel and takes Fah as a parameter
    Take Fah, subtract (-) 32 then multiply it by 5 and divide it by 9 and save it as cel 
    display fah converted to cel rounded to one decimal point



Define a function taht converts the temperature from Cel to Fah and takes Cel as a parameter
    Take Cel, multiply it by 9, divide by 5, then add 32 and save it as Fah
    Return Fah

    
"""

# Functions 

# Fahrenheit to Celsius 
def f_to_c(fah):
    cel = (fah-32) * 5 / 9
    print(f'{fah} Fahrenheit equals {cel:.1f} Celsius')

# Celsius to Fahrenheit 
def c_to_f(cel):
    fah = cel * 9 / 5 + 32
    return fah
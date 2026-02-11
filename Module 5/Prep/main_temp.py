# Alex Ha
# 2543681
# COP1000

# Collaborator: none

"""
Psuedocode

Import functions from temp

ask for input for the temperature as an integer
ask for the tempertature type (f or c)

if the temperature type is f
    use the function for fah to cel which immediately displays the conversion
if the temperature type is c
    use the function for cel to fah and save it as new fah
    display the conversion using new fah

Check that the function ISN'T imported by seeing if the name of the program is main

"""

import temps

# Main Function
def main():
    # Takes inputs
    temp = int(input("Enter a temperature? "))
    type_temp = input("Was that input Fahrenheit or Celsius c/f? ")

    # Check which conversion to use
    if type_temp == 'f' :
        temps.f_to_c(temp)
    elif type_temp == 'c' :
        new_fah = temps.c_to_f(temp)
        print(f'{temp} Celsius is {new_fah:.1f} Fahrenheit')

# Check main
if __name__ == '__main__' :
    main()
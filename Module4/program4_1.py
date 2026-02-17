# Alex Ha
# 2543681
# COP1000

# collaborator: none

"""
Psuedocode 

Loop and ask the user for the starting value until the user provides a valid value (positive integer, greater to 0)
    If input isn't valid, prompt the user that the input isn't valid
Loop and ask the user for the ending value until the user provides a valid value (positive integer, greater to 0)
    If input isn't valid, prompt the user that the input isn't valid
Loop and ask the user for the increment value until the user provides a valid value (positive integer, greater to 0)
    If input isn't valid, prompt the user that the input isn't valid

Display a heading with labels for US tons and Imperial tons

Define the short to long tons conversion factor
For each US Ton value between the start and end value, incremented by the increment value, 
    Multiply (*) the US ton value by the conversion factor to get the imperial ton value
    Display US tons and imperial tons under the respective headings
"""

# Program

# Get Start value
while (start := int(input("Enter the start for US tons "))) <= 0:
    print("Start value for US tons cannot be negative or zero")

# Get Stop value | +1 ensures the loop reaches the stop value
while (stop := int(input("Enter the stop for US tons "))) <= 0:
    print("Stop value for US tons cannot be negative or zero")
stop += 1

# Get Step Value
while (step := int(input("Enter the step for US tons "))) <= 0:
    print("step value for US tons cannot be negative or zero")

# Heading
print(f'{"US Tons":^10}{"Imperial Tons":>13}')

# Conversion Factor and loop
US_TO_IMPERIAL_TONS = 0.892857143
for us_ton_value in range(start, stop, step):
    imperial_ton_value = us_ton_value * US_TO_IMPERIAL_TONS
    print(f'{us_ton_value:^10}{imperial_ton_value:>13.3f}') 
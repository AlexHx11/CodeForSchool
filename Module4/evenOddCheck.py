# Alex Ha
# 2543681
# COP1000

# collaborator: none

"""
Psuedocode 

while a number (inputted from the user) isn't 0 then
    Get the remainder (%) when dividing the number by 2
    If the remainder is equal to 1
        display that the number is odd
    If the remainder is equal to 0
        display that the number is even
    If the number displayed is equal to zero then the loop will end (tested each iteration of the loop)

display that the program is done

"""

# Even Odd Loop
while (number := int(input("Enter an integer or 0 to quit "))) != 0 :
    remainder = number % 2
    if remainder == 1:
        print(f"{number} is an odd number")
    elif remainder == 0:
        print(f"{number} is an even number")

# Prints the finish after the loop ends
print("All done!")
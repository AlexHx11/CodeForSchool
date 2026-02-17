# Alex Ha
# 2543681
# COP1000

# collaborator: none

"""
Pseudocode 

Loop 4 times
    Loop 9 times
        if iteration is the 1st or 9th
            Loop 9 times
                print each number in the same line
            start a new line
        else
            loop 9 times
                if the number is 0 or 1
                    print that number inline
                else
                    leave a space inline
            start a new line

"""

# Program 

# Loops 4 shapes
for num_of_shapes in range(0,4):
    # Checks if printing top and bottom or empty middle rows
    for iteration in range(0,10):
        # Prints top and bottom
        if iteration == 0 or iteration == 9:
            for i in range(0,10):
                print(i, end='')
            print('\n', end='')
        # Prints middle section
        else:
            for i in range(0,10):
                if i == 0 or i == 9:
                    print(i, end='')
                else:
                    print(' ',end='')
            print('\n', end='')

                
# Alex Ha
# 2543681
# COP1000

# collaborator: none

""" 
Psuedocode

Print a heading with the following text "INIT SQUARES CUBES"
Declare a for loop that increments by 5 starting from 5 going up to 50 saving the value to as 'number'
In each loop:
    Square (** 2) 'number' and save it as 'square'
    Cube (** 3) 'number' and save it as 'cube'
    print the number square and cube under their appropriate heading
    Right align squares and cubes and center the number with appropriate spacing

"""

# Print the heading
print(f"{"INIT":^7}{"SQUARES":>8}{"CUBES":>12}")

# Loop and print each number, square, and cube
for number in range(5,51,5) :
    square = number ** 2
    cube = number ** 3
    print(f"{number:^7,}{square:>8,}{cube:>12,}")
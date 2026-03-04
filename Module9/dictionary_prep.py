# Alex Ha
# 2543681
# COP1000

# Collaborator: none

# Psuedocode 

# Create a dictionary with 4 states and capitals
# Display the count of pairs in the dictionary

# Loop to add more
#     Take input for state abbreviation from user
#     if the input was blank then exit the loop
#     if the input is already found in the dictionary, return back its capital
#     take input from the user for the capital
#     add the values into the dictionary

# Loop through the items in the list and display all the items

# Create a dictionary assigning numbers to their cubed version and display it.

# Program

def main():

    # Initial States
    states_and_capitals = {
        'FL':'Tallahassee',
        'AZ':'Phoenix',
        'CO':'Denver',
        'TX':'Austin'
    }

    print(f'{len(states_and_capitals)} states are in the dictionary')

    # Get input and add each input to the dictioanry
    print("Let's add a few more")
          
    while True:
        state_abbreviation = input('Enter state abbrev. or Enter to quit ')
        # Checks for exit
        if state_abbreviation == '':
            break
        # Checks for repeat state
        if state_abbreviation in states_and_capitals.keys():
            print(f"The capital of {state_abbreviation} is {states_and_capitals[state_abbreviation]}")
            continue

        # Gets the capital and adds entry to the dictionary
        state_capital = input(f"Enter capital of {state_abbreviation} ")
        states_and_capitals[state_abbreviation] = state_capital

    # Displays the dictionary
    print(f"\nGot {len(states_and_capitals)} states now. Here they are...")
    for abbrev, capital in states_and_capitals.items() :
        print(f"The capital of {abbrev} is {capital}")

    # --------------------Cubes---------------------
    # Cubes with a dictionary comprehension
    cubes = {num : num**3 for num in range(1,10) if num % 2 == 1}

    # Displays the cubes
    print(f"\nSome cubes made with a dictionary comprehension...")
    for num in cubes.keys() :
        print(f"{num} cubed is {cubes[num]}")

if __name__ == '__main__':
    main()

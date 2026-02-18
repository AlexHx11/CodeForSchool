# Alex Ha
# 2543681
# COP1000

# Collaborator: none

"""
Psuedocode 

define the total age as 0
define the total friends as 0
open the friends.txt file in a read mode
Loop until broken
    read the name and save it
    if the name is blank
        break out the loop
    read the age and save it
    if the age is blank
        break out the loop

    display the age and name in one sentence
    add the age to the total age
    add 1 to the total friends

calculate the average age for the friends (total age divided by total friends)
    
"""

def main():

    # Opens the File
    with open("friends.txt", "r") as file:

        # Defines accumalative variables
        total_age = 0
        total_friends = 0

        while True:
            # Saves the name and age
            if (name := file.readline().rstrip()) == '':
                break
            if (age := int(file.readline())) == '':
                break

            # Displays the name and age and accumulates the age and friends
            print(f'My friend {name} is {age}')
            total_age += age
            total_friends += 1

        # Average and display the age of friends
        avg_age = total_age / total_friends
        print(f"Average age of friends is {avg_age:.1f}")

if __name__ == '__main__':
    main()




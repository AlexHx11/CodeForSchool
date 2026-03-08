# Alex Ha
# 2543681
# COP1000

# Collaborator: none

# Psuedocode

# Define an empty dictionary to host games and the developers
# Display the menu and its 8 options

# Request for a choice of choice of action

# if the user chose the first choice
#     Ask input for the title of a game
#     Verify the input to make sure its in the dictionary
#     return the developer of the game using the title as a key
# if the user chose the second choice
#     Ask input for the title of the game
#     Ask input for the developers of the game
#     Add the inputs into the dictionary
# if the user chose the third choice
#     Ask input for the title of the game
#     Verify the input to make sure its in the dictionary
#     Ask for the updated developers for the game
#     Update the developers for the entry for the title
#     Notify the user that its been updated
# if the user chose the fourth choice
#     Ask input for the title of the game
#     Verify the input to make sure its in the dictionary
#     Delete the title
#     Notify the user its been deleted
# if the user chose the fifth choice
#     Display the length of the dictionary as the number of games
# if the user chose the sixth choice
#     For each title and developer in the dictionary
#         Display the title and developer
# if the user chose the seventh choice
#     For each title in the dictionary
#         Display the title
# if the user chose the eighth choice
#     Terminate the program (Break the loop)

def main():
    games_w_devs = {}

    while True:
        print(f"Menu:\n1. Look up a game by title\n2. Add a new title and its developers\n3. Change the existing developer(s) for a title\n4. Delete an existing title and its developers\n5. Print the number of titles\n6. Print all titles and developers\n7. Print all titles\n8. Quit\n")

        choice = input("Enter your choice: ")

        # Look up a game
        if choice == '1':
            title = input("Enter the title of the game: ")

            if (title not in games_w_devs) :
                print("The specified title was not found.")
                print("")
                continue
            
            print(f"The developer(s) of '{title}' is/are: {games_w_devs[title]}")

            print("")
            continue

        # Add a new title with devs
        elif choice == '2':
            title = input("Enter the title of the game: ")
            devs = input("Enter the developer(s) of the game: ")

            games_w_devs[title] = devs

            print("")
            continue

        # Update devs of a game
        elif choice == '3':
            title = input("Enter the title of the game: ")

            if (title not in games_w_devs) :
                print("The specified title was not found.")
                print("")
                continue

            new_devs = input("Enter the new developer(s) of the game: ")
            games_w_devs[title] = new_devs

            print("")
            continue

        # Deletes a game with its devs
        elif choice == '4':
            title = input("Enter the title of the game: ")

            if (title not in games_w_devs) :
                print("The specified title was not found.")
                print("")
                continue

            del games_w_devs[title]
            print(f"The title '{title}' and its developer(s) have been deleted.")

            print("")
            continue

        # Print the amount of games in the dictionary
        elif choice == '5':
            print(f"The number of titles is: {len(games_w_devs)}")

            print("")
            continue

        # Print each game with devs
        elif choice == '6':
            for title, dev in games_w_devs.items() :
                print(f"'{title}' by {dev}")

            print("")
            continue

        # Print each game without devs
        elif choice == '7':
            for title in games_w_devs.keys() :
                print(f"'{title}'")

            print("")
            continue

        # Exit
        elif choice == '8':
            print("Goodbye!")
            break

if __name__ == '__main__':
    main()
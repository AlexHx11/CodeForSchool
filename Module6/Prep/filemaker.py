# Alex Ha
# 2543681
# COP1000

# Collaborator: none

"""
Psuedocode 

Open the file in write mode
While the name entered isn't blank
    write the name into the file
    prompt the user for the age of the person
    write the age into the file

Close the file
Notify the user that the file was created

"""

def main():
    with open("friends.txt", "w") as friends:
        # Prompts the user for input and writes it in
        while (name := input("Enter first name of friend or Enter to quit ")) != '':
            age = input("Enter age (integer) of this friend ")
            friends.write(f"{name}\n")
            friends.write(f"{age}\n")

    # Confirms the file is created
    print("File was created")

if __name__ == "__main__":
    main()




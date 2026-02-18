# Alex Ha
# 2543681
# COP1000

# Collaborator: none

"""
Psuedocode 

Open the file in write mode
While the title entered isn't blank
    
    prompt the user for the artists
    prompt the user for the regular price
    prompt the user for the discount percent

    write the title into the file
    write the age into the file
    write the regular price into the file
    write the discount percent into the file

Close the file
Notify the user that the file was created

"""

def main():
    with open("lpsale.txt", "w") as albums:
        # Prompts the user for input 
        while (title := input("Enter the album's title: ")) != '':
            artists = input("Enter the artist(s) name(s): ")
            reg_price = input("Enter the regular price: ")
            discount_prct = input("Enter the discount in percent: ")

            # Writes the values in
            albums.write(f"{title}\n")
            albums.write(f"{artists}\n")
            albums.write(f"{reg_price}\n")
            albums.write(f"{discount_prct}\n")

    # Confirms the file is created
    print("The LP sale data has been successfully stored in lpsale.txt.")

if __name__ == "__main__":
    main()
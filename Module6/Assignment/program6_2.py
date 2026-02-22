# Alex Ha
# 2543681
# COP1000

# Collaborator: none

"""
Psuedocode 

Display the heading with column titles for each category

Open the file as lpsales
While the title line isn't blank
    Read lines for the artist, price, and discount and save them

    Calculate the discount amount by multiplying the price by the discount percent (divided by 100 to turn a percent into a decimal)
    Calculate the discounted price by subtracting the discount amount from the original price

    Display the title, artists, discount amount, and discounted price under the respective columns.

"""

def main():
    # Create Heading
    print(f"{"Album Title":<33}{"Artist(s) Name(s)":<23}{"Discounts ($)":<18}{"Total Price After Discount ($)":<18}")
    print("-----------------------------------------------------------------------------------------------------")

    with open("lpsale.txt", "r") as lpsales:

        # Takes inputs and saves them
        while True:
            title = lpsales.readline().rstrip() 
            # Check for a blank line
            if title == '':
                break
            artist = lpsales.readline().rstrip()
            price = float(lpsales.readline())
            discount = int(lpsales.readline())

            # Calculates Discounts
            discount_amt = price * (discount / 100) # Converts percent to decimal
            discount_price = price - discount_amt

            print(f"{title:<33}{artist:<23}{discount_amt:<18.2f}{discount_price:<18.2f}")


if __name__ == '__main__':
    main()
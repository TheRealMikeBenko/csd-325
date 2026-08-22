# Michael Benko
# 2026-08-22
# CSD325-302E Advanced Python (2267-DD)
# Module 2.2 Assignment

# Original program written for Module 4.2 Assignment - CSD205-302E Introduction to Programming with Python.
# Original submission on 2026-06-20

# This program prompts the user for miles driven, validates the input,
# converts miles to kilometers using a function, and displays the result.

def convert_miles_to_kilometers(miles):
    """Return the kilometer equivalent of the given miles."""
    return miles * 1.60934

def main():
    # Prompt for miles and validate input
    valid = False
    while not valid:
        try:
            miles = float(input("Enter the number of miles driven: "))
            if miles > 0:
                valid = True
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    # Convert miles to kilometers
    kilometers = convert_miles_to_kilometers(miles)

    # Display the result
    print(f"{miles} miles is equal to {kilometers:.2f} kilometers.")

main()
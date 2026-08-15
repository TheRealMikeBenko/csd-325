# Michael Benko
# 2026-08-14
# CSD325-302E Advanced Python (2267-DD)
# Module 1.3 Assignment

# This program prompts the user for a number (of bottles of beer).
# Then the program will count down until the program reaches zero.

def countdown_bottles(bottles):
    while bottles > 1:
        print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
        bottles -= 1
        # If statement to determine if the next line should be plural or singular
        if bottles > 1:
            print(f"Take one down and pass it around, {bottles} bottles of beer on the wall.\n")
        else:
            print(f"Take one down and pass it around, {bottles} bottle of beer on the wall.\n")

    # When there is only one bottle, change the lyrics
    print(f"{bottles} bottle of beer on the wall, {bottles} bottle of beer.")
    print("Take one down and pass it around, no more bottles of beer on the wall.\n")

def main():
    # Validation loop to ensure the user enters a positive integer
    while True:
        try:
            user_input = input("How many bottles of beer are on the wall?\n")
            bottles = int(user_input)

            # Checks if number is possitive and greater than zero
            if bottles < 1:
                print("Please enter a positive integer greater than zero.\n")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.\n")
    print()

    countdown_bottles(bottles)

    print ("Time to buy more beer.\n")

# Call the main function to start the program.
if __name__ == "__main__":
    main()

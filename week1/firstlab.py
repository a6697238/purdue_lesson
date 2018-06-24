#
# CS 177 Lab Introduction
# This is my first Python program – labintro.py
# <NICK YUNING CUI>
#
def main():
    print()
    print("This program prompts the user for their name")
    print(" and their age, then displays a poem and")
    print(" calculates the number of days they've lived.")
    print()

    # Prompt the user for name and age
    name = input("Please enter your name: ")
    age = eval(input("Enter your current age: "))
    print()

    # Display the poem
    print("Happy Birthday to you! Happy Birthday to you!")
    print("Happy Birthday, dear", name)
    print("Happy Birthday to you!")
    print()

    # Calculate and display the number of days lived
    days = int(age * 365.25)
    print("You have lived at least", days, "days already!")


main()

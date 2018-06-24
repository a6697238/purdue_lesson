#
# CS 177 – labprep3.py
# {NICK YUNING CUI}
# Following Coding Standards and Guidelines
# This program calculates the distance traveled by a
# tennis ball in space at a time specified by the user

# main() function
import re


def main():
    # Initialize any necessary variables
    print("This program displays variations and statistics for the String provided")
    print(" ")

    # Prompt the user for the String to display and evaluate
    input_str = str(input('Enter a String: '))
    print(" ")
    print("Variations on: "+input_str)
    print("===================")
    # Call the twist() function
    twist(input_str)
    print(" ")
    print("Statistics for: "+input_str)
    print("===================")
    # Call the stats() function
    stats(input_str)




# twist() function displays the required variations of a String
def twist(input_str):
    input_str = re.sub(" +", " ", input_str)
    # Only the first letter of the first word CAP
    print("First word Capitalized: "+input_str[0].upper() + input_str[1:].lower())

    # The string with the first letter of each word CAP
    str_temp = input_str.split(" ")
    str_list = []
    for old_str in str_temp:
        new_str = old_str[0].upper()+old_str[1:].lower()
        str_list.append(new_str)
    print("Words Capitalized: "+" ".join(str_list))

    # The string in all lower and reversed
    str_list = []
    for char_item in input_str:
        str_list.insert(0,char_item.lower())
    print("All Lowercase and Reversed: "+"".join(str_list))

    # The first Letter of every word CAP, spaces replaces with #
    print("First Word Capitalize,Spaces Replaced: "+input_str[0].upper() + input_str[1:].lower().replace(" ","#"))





# stats() function displays statics about String
def stats(input_str):
    vowels = ['a','e','i','o','u']
    # Count and display the number of spaces
    # Count and display the number of words
    # Count and display the number of vowels(a,e,i,o,u,A,E,I,O,U)
    space_num = 0
    vowel_num=0
    word_num=1
    for char_item in input_str:
        if(char_item.lower()==' '):
            space_num +=1
        if(char_item.lower() in vowels):
            vowel_num +=1

    input_str = re.sub(" +", " ", input_str)
    for char_item in input_str:
        if (char_item.lower() == ' '):
            word_num += 1
    print("Number of spaces: "+str(space_num))
    print("Number of Words: "+str(word_num))
    print("Number of Vowels: "+str(vowel_num))


# Call the main() function to start the program
# test_str:My AP goin' psycho, lil' mama bad like Michael
# test_str:WhatevER  IT  TAkes
# test_str:DONT GO BREAKING MY HEART
main()

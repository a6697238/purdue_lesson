#
# CS 177 – lab4.py
# {NICK YUNING CUI}
# This is a demonstration of the basic Python file function
# The program combines data from two separate files and displays a table with the results from this combination
# the data comes from the BOOYA observations in the Purdue Pulsar Lab


import re

def read(file_name_1,file_name_2):
    print ("")
    print ("")
    file_1 = open(file_name_1)
    print ("Reading data file: " + file_name_1)
    file_2 = open(file_name_2)
    print ("Reading data file: " + file_name_2)
    print ("Combining data to a single list " + file_name_1 + ".temp" )
    line_list = []
    line_1 = file_1.readline().strip()  # 调用文件的 readline()方法
    line_2 = file_2.readline()
    line_list.append(line_1.strip() + line_2.strip())
    while line_1:
        line_1 = file_1.readline()
        line_2 = file_2.readline()
        line_list.append(line_1.strip()+line_2.strip())
    file_1.close()
    file_2.close()
    return line_list


def main():
    print ("This program combines and evaluates the data from two")
    print ("separate files containing Pulsar signal strengths")
    file_name_1 = str(input('"Enter the Pulsar name file: '))
    file_name_2 = str(input('"Enter the Signal strength file: '))
    file_list = read(file_name_1,file_name_2)
    print ("")
    print ("Displaying the first 10 entries in the combined dataset :")
    for combine in range(0,10):
        if(combine==9):
            print(file_list[combine] , end='')
        else:
            print(file_list[combine]+",", end='')

main()

#
# def main():
#     # Initialize any necessary variables
#     print("This program displays variations and statistics for the String provided")
#     print(" ")
#
#     # Prompt the user for the String to display and evaluate
#     input_str = str(input('Enter a String: '))
#     print(" ")
#     print("Variations on: "+input_str)
#     print("===================")
#     # Call the twist() function
#     twist(input_str)
#     print(" ")
#     print("Statistics for: "+input_str)
#     print("===================")
#     # Call the stats() function
#     stats(input_str)
#
#
#
#
# # twist() function displays the required variations of a String
# def twist(input_str):
#     input_str = re.sub(" +", " ", input_str)
#     # Only the first letter of the first word CAP
#     print("First word Capitalized: "+input_str[0].upper() + input_str[1:].lower())
#
#     # The string with the first letter of each word CAP
#     str_temp = input_str.split(" ")
#     str_list = []
#     for old_str in str_temp:
#         new_str = old_str[0].upper()+old_str[1:].lower()
#         str_list.append(new_str)
#     print("Words Capitalized: "+" ".join(str_list))
#
#     # The string in all lower and reversed
#     str_list = []
#     for char_item in input_str:
#         str_list.insert(0,char_item.lower())
#     print("All Lowercase and Reversed: "+"".join(str_list))
#
#     # The first Letter of every word CAP, spaces replaces with #
#     print("First Word Capitalize,Spaces Replaced: "+input_str[0].upper() + input_str[1:].lower().replace(" ","#"))
#



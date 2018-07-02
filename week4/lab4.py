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

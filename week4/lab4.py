#
# CS 177 – lab4.py
# {NICK YUNING CUI}
# This is a demonstration of the basic Python file function
# The program combines data from two separate files and displays a table with the results from this combination
# the data comes from the BOOYA observations in the Purdue Pulsar Lab



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
    line_2 = file_2.readline().strip()  # 调用文件的 readline()方法
    line_list.append(line_1.strip() + line_2.strip())
    while line_1:
        line_1 = file_1.readline()
        line_2 = file_2.readline()
        lint_str = line_1.strip()+line_2.strip()
        if(len(lint_str)>0):
            line_list.append(lint_str)
    file_1.close()
    file_2.close()
    return line_list

def report(file_list):
    count_map = {}
    row_list = ['M','A','K','E','R','S'];
    for row in row_list:
        for column in [1,2,3,4,5]:
             count_map[row+str(column)]=0
    for data in file_list:
        count_map[data] = count_map[data] +1
    val_list = []
    for (k, v) in count_map.items():
        val_list.append(v)
    print ("           1            2            3            4              5")
    print ("           =======================================================")
    for i in range(0,30):
        if ((i>1)&(i%5==0)):
            print ("%s           %s          %s           %s           %s            %s"%(row_list[int((i-1)/5)],val_list[i-5],val_list[i-4],val_list[i-3],val_list[i-2],val_list[i-1]))





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
    print("")
    report(file_list)

main()


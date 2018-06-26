#
# CS 177 – project1.py
# {NICK YUNING CUI}
# Following Coding Standards and Guidelines
# This program calculates the distance traveled by a
# tennis ball in space at a time specified by the user
import math


def main():
    # Initialize any necessary variables
    print("This program creates a vertical plot based ont the function : y = A * sin(B*x + C) + D")
    print("where : Amplitude = A")
    print("        Frequency = B / (2 * pi)")
    print("        Phase = -C/B")
    print("        offset = D")
    print("==============================")
    # Prompt the user for the String to display and evaluate
    param_map = {}
    print("Please enter the values for :")
    param_map['A'] = float(input('A: '))
    param_map['B'] = float(input('B: '))
    param_map['C'] = float(input('C: '))
    param_map['D'] = float(input('D: '))
    caculate_header(param_map)
    display_wave(param_map)

# caculate_header() function display a vertical plot header
def caculate_header(param_map):

    param_map['Amplitude']= param_map['A']
    param_map['Range']= 2*param_map['A']
    param_map['Frequency']= param_map['B']/6.28
    param_map['Phase']= -param_map['C']/param_map['B']
    param_map['Offset']= param_map['D']

    param_map['Low']= param_map['Offset']-param_map['Amplitude']
    param_map['Mid']= param_map['Offset']
    param_map['High']= param_map['Offset']+param_map['Amplitude']
    param_map['offset_str'] = " "*int(param_map['Offset'])
    param_map['half_str'] = " "*(int(param_map['Offset']/2))
    param_map['border_str'] = " ="*int(param_map['Range'])


    print("Amplitude: " + str(param_map['Amplitude']))
    print("Range: " + str(param_map['Range']))
    print("Frequency: " + str(param_map['Frequency']))
    print("Phase: " + str(param_map['Phase']))
    print("Offset: " + str(param_map['Offset']))

    # print(" %s Low: Mid: %s       High: %s"%(str(param_map['offset_str']),str(param_map['Low']),str(param_map['Mid']),str(param_map['High'])))
    print(" %sLow:%sMid:%sHigh:"%(str(param_map['offset_str']), param_map['half_str'], param_map['half_str']))
    print(" %s %s"%(str(param_map['offset_str']),param_map['border_str']))
    return param_map

def display_wave(param_map):
    len = param_map['High'] - param_map['Low']
    for x_step in range(0,46):
        display = False
        print(x_step, end='')
        print(str(param_map['offset_str']),end='')
        for y_step in range(int(param_map['Low']),int(param_map['High']+1)):
            y_value = param_map['Amplitude'] * math.sin(param_map['B']*x_step/45.0 + param_map['C']) + param_map['D']
            if((~display)&(abs(y_value-y_step)<1)):
                print("*",end='')
                display = True
            else:
                print(" ",end='')
        print("\t")


main()

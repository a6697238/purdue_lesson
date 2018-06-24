#
# CS 177 – labprep1.py
# {NICK YUNING CUI}
# Following Coding Standards and Guidelines
# This program calculates the distance traveled by a
# tennis ball in space at a time specified by the user



# Display a message describing the functionality of the program

# Prompt the user for the initial velocity of the ball

# Prompt the user for the time in seconds

# Calculate the distance traveled using the formula:

# distance = velocity * time

# Display the results of the calculation



# Function: Calculate the distance traveled
# # v: velocity
# # t: time
# # return
# # distance = velocity * time
def calc_distance(v, t):
    return v * t


# Display a message describing the functionality of the program
print('This program simulates the movement of a tennis ball in space', end='\n')
print('=============================================================', end='\n')
print('It prompts the user for two values:', end='\n')
print('the initial speed of the ball, and a travel time,', end='\n')
print('then computes the position of the ball after that time,', end='\n')
print('=============================================================', end='\n')
print('', end='\n')

# Prompt the user for the initial velocity of the ball
velocity = float(input('Please enter the velocity of the ball (meters per second): '))

# Prompt the user for the time in seconds
time = float(input('Please enter the travel time (seconds): '))

# Calculate the distance traveled using the formula:
# distance = velocity * time
distance = calc_distance(velocity, time)

# Display the results of the calculation
print('', end='\n')
print('After {} seconds the ball is {} meters from the starting point'.format(time, distance))
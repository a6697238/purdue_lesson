#
# CS 177 – project2.py
# {YUNING CUI, PUID0028050054}
# Problem Description:
# Simulating Generations of Living Organisms
#
from graphics import *
import random
import copy


# Part 1
# Create the Control Panel
# Return all the Graphics elements necessary to interact
# with the Graphics window
def makeControl():
    # Create a 300 x 250 Graphics window with a light-grey background titled Control Panel
    control_panel = GraphWin("Control Panel", 300, 250)
    control_panel.setBackground('lightgrey')

    # The GENERATIONS title text is bold and white on a black banner
    banner_rectangle = Rectangle(Point(0, 20), Point(320, 40))
    banner_rectangle.setFill('black')
    banner_rectangle.draw(control_panel)

    title_string = Text(Point(150, 30), 'GENERATIONS')
    title_string.setFill('white')
    title_string.setStyle('bold')
    title_string.draw(control_panel)

    # The controls are 100x30 Rectangles
    # START (green), PAUSE (orange), RESET (light blue), QUIT (red)
    # Green
    green_rectangle = Rectangle(Point(30, 55), Point(130, 85))
    green_rectangle.setFill('green')
    green_rectangle.draw(control_panel)

    start_string = Text(Point(82, 70), 'START')
    start_string.draw(control_panel)

    # Orange
    orange_rectangle = Rectangle(Point(170, 55), Point(270, 85))
    orange_rectangle.setFill('orange')
    orange_rectangle.draw(control_panel)

    pause_string = Text(Point(222, 70), 'PAUSE')
    pause_string.draw(control_panel)

    # Lightblue
    lightblue_rectangle = Rectangle(Point(30, 105), Point(130, 135))
    lightblue_rectangle.setFill('lightblue')
    lightblue_rectangle.draw(control_panel)

    reset_string = Text(Point(82, 120), 'RESET')
    reset_string.draw(control_panel)

    # Red
    red_rectangle = Rectangle(Point(170, 105), Point(270, 135))
    red_rectangle.setFill('red')
    red_rectangle.draw(control_panel)

    quit_string = Text(Point(222, 120), 'QUIT')
    quit_string.draw(control_panel)

    # Living Cells
    living_cell_label = Text(Point(95, 170), 'Living Cells:')
    living_cell_label.setStyle('bold')
    living_cell_label.draw(control_panel)

    # Cell count
    living_cell_count = Text(Point(205, 170), '0')
    living_cell_count.setStyle('bold')
    living_cell_count.draw(control_panel)

    # Generation Num
    generation_num_label = Text(Point(80, 210), 'Generation Num:')
    generation_num_label.setStyle('bold')
    generation_num_label.draw(control_panel)

    generation_num = Text(Point(205, 210), '0')
    generation_num.setStyle('bold')
    generation_num.draw(control_panel)

    return control_panel, living_cell_count, generation_num


# Part 2
# Create the Generations Grid
def makeGrid():
    # Create a 400 x 400 Graphics window titled Generations Grid
    grid_panel = GraphWin("Generations Grid", 400, 400)

    # Create a List of 10x10 Rectangles(40 rows/columns)
    rec_array = []
    flag_array = []
    for row in range(40):
        rec_array.append([])
        flag_array.append([])
        for column in range(40):
            rectangle = Rectangle(Point(row * 10, column * 10), Point((row + 1) * 10, (column + 1) * 10))
            rectangle.draw(grid_panel)
            # The outer-most border of Rectangles black fill with a black outline
            if row == 0 or row == 39 or column == 0 or column == 39:
                rectangle.setFill('black')
                rectangle.setOutline('black')
            else:
                # All other Rectangles have a white fill / black outline
                rectangle.setFill('white')
                rectangle.setOutline('black')

            rec_array[row].append(rectangle)
            flag_array[row].append(0)

    return grid_panel, rec_array, flag_array


# Part 3
def life(rec_array, flag_array):
    # Use loops to determine the initial alive or dead status of each of the cells in the Grid.
    for row in range(1, 39):
        for column in range(1, 39):
            # Each cell in the Generations Grid has an 18% chance of starting the simulation ‘alive’.
            if random.randint(0, 100) <= 18:
                flag_array[row][column] = 1
                rec_array[row][column].setFill('red')
            else:
                flag_array[row][column] = 0
                rec_array[row][column].setFill('white')


# Part 4
def cycle(rec_array, flag_array):
    new_flag_array = copy.deepcopy(flag_array)
    for row in range(1, 39):
        for col in range(1, 39):
            neighbor = 0
            # Check up-left
            if row - 1 >= 1 and col - 1 >= 1:
                if flag_array[row-1][col-1] == 1:
                    neighbor += 1
            # Check up
            if row - 1 >= 1:
                if flag_array[row-1][col] == 1:
                    neighbor += 1
            # Check up-right
            if row - 1 >= 1 and col + 1 <= 39:
                if flag_array[row-1][col+1] == 1:
                    neighbor += 1
            # Check left
            if col - 1 >= 1:
                if flag_array[row][col-1] == 1:
                    neighbor += 1
            # Check right
            if col + 1 <= 39:
                if flag_array[row][col+1] == 1:
                    neighbor += 1
            # Check down-left
            if row + 1 <= 39 and col - 1 >= 1:
                if flag_array[row+1][col-1] == 1:
                    neighbor += 1
            # Check down
            if row + 1 <= 39:
                if flag_array[row+1][col] == 1:
                    neighbor += 1
            # Check down-right
            if row + 1 <= 39 and col + 1 <= 39:
                if flag_array[row+1][col+1] == 1:
                    neighbor += 1

            if flag_array[row][col] == 1:
                if neighbor < 2:
                    # Under Population: A living cell with less than
                    # two living neighbor cells should die
                    new_flag_array[row][col] = 0
                elif neighbor > 3:
                    # A living cell with more than three living neighbors dies
                    new_flag_array[row][col] = 0
            else:
                if neighbor == 3:
                    # A dead cell with exactly three living neighbors comes to life
                    new_flag_array[row][col] = 1

    # Apply the change to each cell’s status only after fully analyzing the entire grid
    for row in range(1, 39):
        for col in range(1, 39):
            flag_array[row][col] = new_flag_array[row][col]
            if flag_array[row][col] == 0:
                rec_array[row][col].setFill('white')
            else:
                rec_array[row][col].setFill('red')


# Part 5: Bring the simulation together with the main() function
if __name__ == '__main__':
    # Call makeControl() to create the Control Panel Graphics window
    control_panel, living_cell_count, generation_num_label = makeControl()

    # Call makeGrid() to create the Generations Grid Graphics window
    grid_panel, rec_array, flag_array = makeGrid()

    generation_num = 0

    is_running = False
    while True:
        click_point = control_panel.checkMouse()
        if click_point is not None:
            x = click_point.x
            y = click_point.y
            if 270 >= x >= 170 and 105 <= y <= 135:
                # Click QUIT
                break
            elif 130 >= x >= 30 and 55 <= y <= 85:
                # Click START
                is_running = True
            elif 270 >= x >= 170 and 55 <= y <= 85:
                # Click PAUSE
                is_running = False
            elif 130 >= x >= 30 and 105 <= y <= 135:
                # Click RESET
                generation_num = 0
                life(rec_array, flag_array)

        if is_running:
            cycle(rec_array, flag_array)
            generation_num += 1

        # Update the Text objects indicating quantity of living cells and current generation number
        generation_num_label.setText(str(generation_num))
        live_cell_count = 0
        for row in range(1, 39):
            for col in range(1, 39):
                if flag_array[row][col] == 1:
                    live_cell_count += 1
        living_cell_count.setText(live_cell_count)

        control_panel.update()

    # When the loop ends, close both Graphics windows
    grid_panel.close()
    control_panel.close()

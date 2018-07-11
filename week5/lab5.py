#
# CS 177 – lab5.py
# {NICK YUNING CUI}
# This is a shooting game
# The user can play multiple games without closing the
# graphics window, however anytime the user clicks on the red QUIT box, the graphics window should be closed
# and the Python program ends
#
#

from graphics import *


def main():
    dartGame()


def dartGame():
    win = drawDartboard()
    msg = Text(Point(180, 40), "")
    while (True):
        user_circle = []
        score = 0
        for i in range(0,3):
            point = win.getMouse()
            draw_circle_list(win,point,5,'white',user_circle)
            score = getScore(point) + score
            msg.undraw()
            msg.setText(score)
            msg.setSize(20)
            msg.setTextColor('white')
            msg.draw(win)
            if (checkIfQuit(point)):
                win.close()
        for c in user_circle:
            c.undraw()

# draw() function to judge if quit
def checkIfQuit(point):
    if ((point.getX() < 290)
            & (point.getX() > 240)
            & (point.getY() < 290)
            & (point.getY() > 240)):
        return True

# draw() function to get user shoot score
def getScore(point):
    radius_list = [10,30,70,100]
    point_v = {}
    point_v[0] = 100
    point_v[1] = 80
    point_v[2] = 50
    point_v[3] = 20
    point_v[-1] = 0
    idx = -1
    for radius_idx in range(0,4):
        out_line = radius_list[radius_idx] * radius_list[radius_idx]
        result = (point.getX()-150)*(point.getX()-150) + (point.getY()-150)*(point.getY()-150)
        if(result<out_line):
            idx = radius_idx
            break
    return point_v[idx]

# draw() function draw a drawDartboard
def drawDartboard():
    win = GraphWin("Dartboard", 300, 300)
    win.setBackground("grey")
    draw_circle(win, Point(150, 150), 100, 'black')
    draw_circle(win, Point(150, 150), 70, 'yellow')
    draw_circle(win, Point(150, 150), 30, 'black')
    draw_circle(win, Point(150, 150), 10, 'red')
    draw_rectangle(win, Point(290, 290), Point(240, 240), 'red')
    draw_msg(win, Point(265, 265))
    msg = Text(Point(130, 40), "Score : ")
    msg.setSize(20)
    msg.setTextColor('white')
    msg.draw(win)
    return win


# draw() function draw a circle
def draw_circle(win, point, radius, color):
    c = Circle(point, radius)
    c.setFill(color)
    c.draw(win)

# draw() function draw a circle_list to save uer shoot
def draw_circle_list(win, point, radius, color,circle_list):
    c = Circle(point, radius)
    c.setFill(color)
    c.draw(win)
    circle_list.append(c)

# draw() function draw a rectangle
def draw_rectangle(win, point1, point2, color):
    r = Rectangle(point1, point2)
    r.setFill(color)
    r.draw(win)


# draw() function draw a msg
def draw_msg(win, point):
    msg = Text(point, "QUIT")
    msg.draw(win)


main()

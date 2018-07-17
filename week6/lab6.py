#
# CS 177 – lab6.py
# {NICK YUNING CUI}
# this program is a game
# Once a click is detected, the Circle is animated, bouncing off of the borders and staying inside the Graphics window
# The object of the game is to click on the Circle, which causes it to split into two (2) smaller Circles with half the
# radius of the Circle that was clicked. The user continues to click the smaller Circles which divide again. Circles
# with a radius less than 20 are removed from the Graphics window. The game is over when all the Circles are
# removed.
#
from random import choice

from graphics import *


def main():
    circles = []
    win = GraphWin("Pop-em", 500, 500)
    win.setBackground("light grey")
    msg = Text(Point(240, 40), "Click anywhere to start")
    msg.draw(win)
    circles.append(create(Point(250, 250), 80, win))
    while (True):
        if (len(circles) == 0):
            break
        point = win.getMouse()
        for circleItem in circles:
            if (isinCircle(point, circleItem[0], circleItem[1], circleItem[2])):
                handleCircle(win,circleItem,circles)
    msg.setText("Game over")
    win.getMouse()
    win.close()

# handleCircle() function handle the event if user click in circle
def handleCircle(win,circleItem, circles):
    circles.remove(circleItem)
    objC = circleItem[0]
    objC.undraw()
    if (objC.getRadius() >= 19):
        dx = 1.2 * circleItem[1]
        dy =  circleItem[2]
        radius = objC.getRadius()/2
        newItem = create(Point(dx,dy),radius,win)
        circles.append(newItem)
        dx = circleItem[1]
        dy = 1.2 * circleItem[2]
        radius = objC.getRadius() / 2
        newItem = create(Point(dx,dy),radius,win)
        circles.append(newItem)


# isinCircle() function judge if point is in circle
def isinCircle(point, circle, x, y):
    out_line = circle.getRadius() * circle.getRadius()
    result = (point.getX() - x) * (point.getX() - x) + (point.getY() - y) * (point.getY() - y)
    if (out_line > result):
        return True
    else:
        return False

# create()  function draw a circle and return it position
def create(point, radius, win):
    colors = ['red', 'blue', 'green', 'orange']
    c = Circle(point, radius)
    c.setFill(choice(colors))
    c.draw(win)
    return [c, point.getX(), point.getY()]


main()

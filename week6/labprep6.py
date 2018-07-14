#
# CS 177 – labprep6.py
# {NICK YUNING CUI}
# this program make circle move smooth with mouse click
#
#

from graphics import *


def main():
    win = GraphWin("Shapes", 400, 400)
    win.setBackground("light grey")
    oldPoint = Point(200, 200)
    c = Circle(oldPoint, 30)
    c.setFill('blue')
    c.draw(win)
    for time in range(0, 5):
        newPoint = win.getMouse()  # pause for click in window
        movCircle(c, oldPoint, newPoint)
        oldPoint = newPoint


# move the circle to new place smooth
def movCircle(c, start, des):
    moveX = des.getX() - start.getX()
    moveY = des.getY() - start.getY()
    stepX = moveX / 20.0
    stepY = moveY / 20.0

    for x in range(0, 20):
        c.move(stepX, stepY)


main()

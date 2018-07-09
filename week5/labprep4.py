#
# CS 177 – labprep5.py
# {NICK YUNING CUI}
# This is a demonstration of basic Graphics module functions
# Full documentation of the Graphics module can be found in
# the Zelle Python textbook Ch.4 and at:
# http://mcsp.wartburg.edu/zelle/python/graphics/graphics.pdf
#
#
# This program creates a 400 x 300 Graphics window an a Text
#  object prompting the user to click in the window.A circle is drawn
#  wherever a mouse click is detected with a random radius(5-20) and
#  a random color (red,blue,green or purple ) After 5 mouse clicks , the text object is changed to
# prompt the user to click one more time,then closes the window.
#
#

from graphics import *
from random import *

def main():
    win = GraphWin("Shapes", 400, 300)
    msg = Text(Point(200, 150), "Click to draw a Circle")
    msg.draw(win)
    for i in range(0,5):
        draw(win,win.getMouse())
    msg.setText("Click again to close window")
    win.getMouse()  # pause for click in window
    win.close()

# draw() function draw a circle  by random
def draw(win,point):
    colors = ['red', 'blue', 'green','purple']
    radius = randint(5,20)
    c = Circle(point, radius)
    c.setFill(choice(colors))
    c.draw(win)


main()

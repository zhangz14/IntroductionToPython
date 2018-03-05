"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Zikang Zhang.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# TODO: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow()
t95 = rg.SimpleTurtle('turtle')
t95.pen = rg.Pen('orange',5)
t95.speed = 50

for a in range(15):
    t95.draw_circle(radius=10+10*a)
    t95.pen_up()
    t95.right(90)
    t95.forward(10)
    t95.left(90)
    t95.pen_down()

t110e3 = rg.SimpleTurtle('turtle')
t110e3.pen = rg.Pen('red',3)
t110e3.speed = 20

for b in range(10):
    t110e3.draw_circle(radius=10)
    t110e3.pen_up()
    t110e3.right(45)
    t110e3.forward(20)
    t110e3.left(45)
    t95.pen_down()

window.close_on_mouse_click()
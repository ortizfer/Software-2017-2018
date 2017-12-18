from Dice import *

detected = false # global variable

targetangle1 = 0 # this is the number 5 die
targetangle2 = 0 # this is the number 6 die

targetdepth1 = 0 # this is the depth for the number 5 die
targetdepth2 = 0 # this is the depth for the number 6 die

placeholder = 1000 # change placeholder after given the correct distance

def start():

    print("Starting Mission")

# assuming that the sub will see the die at start

    while not detected:
        Movement.rotate(90)
        Movement.rotate(-180)
        Movement.rotate(90)

# end loop when Vision detects the die
# position itself to position of die and move towards it

    Movement.rotate(targetangle1)
    Movement.depth(targetdepth1)
    Movement.forward(placeholder)

# It has to push the die 10 degrees
# after it has pushed the die, go back

    Movement.backward(placeholder)

# position itself to the detected second die
    Movement.rotate(targetangle2)
    Movement.depth(targetdepth2)
    Movement.forward(placeholder)

# move backwards to continue rest of competition
    Movemet.backward(placeholder)

    print("Mission Accomplished")


# Need to consider the exact locations and dimensions of EVERY dice
# so that the sub can successfully evade the unnecessary dice and push the correct dice.





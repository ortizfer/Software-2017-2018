from Utils import Movement
detected = False  # global variable

targetdistance1 = 0  # this is the distance for the number 1 die
targetdistance2 = 0  # this is the distance for the number 2 die
targetdistance3 = 0  # this is the distance for the number 3 die
targetdistance4 = 0  # this is the distance for the number 4 die
targetdistance5 = 0  # this is the distance for the number 5 die
targetdistance6 = 0  # this is the distance for the number 6 die

targetangle1 = 0  # this is the angle for the number 1 die
targetangle2 = 0  # this is the angle for the number 2 die
targetangle3 = 0  # this is the angle for the number 3 die
targetangle4 = 0  # this is the angle for the number 4 die
targetangle5 = 0  # this is the angle for the number 5 die
targetangle6 = 0  # this is the angle for the number 6 die

targetdepth1 = 0  # this is the depth for the number 1 die
targetdepth2 = 0  # this is the depth for the number 2 die
targetdepth3 = 0  # this is the depth for the number 3 die
targetdepth4 = 0  # this is the depth for the number 4 die
targetdepth5 = 0  # this is the depth for the number 5 die
targetdepth6 = 0  # this is the depth for the number 6 die

alldistances = [targetdistance1, targetdistance2, targetdistance3, targetdistance4, targetdistance5, targetdistance6]
max_distance = max(alldistances)

alldepths = [targetdepth1, targetdepth2, targetdepth3,targetdepth4, targetdepth5, targetdepth6]
max_depth = max(alldepths)

targetdepthfinal = 2 + max_depth  # this is the depth for the final elevation (+2 highest dice depth)
targetdistancefinal = 2 + max_distance  # this is the distance for the final acceleration (+2 farthest dice distance)
initialdepth = 0 # this is the depth the submarine starts the mission in

placeholder = 0  # change placeholder after given the correct distance


def start():

    print("Starting Mission")

# assuming that the sub will see the dice at start

    while not detected:
        Movement.rotate(90)
        Movement.rotate(-180)
        Movement.rotate(90)
        Movement.depth(placeholder)

# end loop when Vision detects the dice
# position itself to position of die and move towards it

    Movement.rotate(targetangle5)
    Movement.depth(targetdepth5)
    Movement.forward(targetdistance5)

# It has to push the die 10 degrees
# after it has pushed the die, go back

    Movement.backward(targetdistance5)

# position itself to the detected second die
    Movement.rotate(targetangle6)
    Movement.depth(targetdepth6)
    Movement.forward(targetdistance6)

# move backwards to continue rest of competition
    Movement.backward(targetdistance6)

# move upwards past the highest dice, move forward and when dice passes final dice, go back down
    Movement.depth(targetdepthfinal)
    Movement.forward(targetdistancefinal)
    Movement.depth(initialdepth)

    print("Mission Accomplished")


# Need to consider the exact locations and dimensions of EVERY dice
# so that the sub can successfully evade the unnecessary dice and push the correct dice.
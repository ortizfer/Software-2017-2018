###    Import Libraries    ###
import sys
from Missions import MissionGate, QualifyingMission

###    Declare Variables    ###
# Must get data from mission controller
qualifying = sys.argv[1];
gate = sys.argv[2];
path = sys.argv[3];
dice = sys.argv[4];
fake_island = sys.argv[5];

###    Health/Protocol Check    ###
# Verify that all components are up and running and that everything is ready to send/receive

###    Missions    ###

# Qualifying Run
if qualifying == '1':
    # call Qualifying();
    print("Executing qualifying run")

# Gate
if gate == '1':
    # call Gate();
    print("Executing gate mission")

# Follow the Path
if path == '1':
    # call Path();
    print("Executing path mission")

# Dice
if dice == '1':
    # call Dice();
    print("Executing dice mission")

# Fake Island
if fake_island == '1':
    # call FakeIsland();
    print("Executing fake island mission")






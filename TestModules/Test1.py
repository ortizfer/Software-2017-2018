"""
Test Module for ROS communication between Vision/Logic/Embedded 

Author: Fernando Ortiz

"""

numView = '000'
receivedNum = 0




# call vision to receive number of dots on a screen

def check_view():

    return receivedNum


# sends the new number to embedded for display

def send_view():

    print("Sent value :"+numView)


receivedNum = check_view()

if receivedNum == 0:
    numView = '000'

if receivedNum == 1:
    numView = '001'

if receivedNum == 2:
    numView = '010'

if receivedNum == 3:
    numView = '011'

if receivedNum == 4:
    numView = '100'

if receivedNum == 5:
    numView = '101'

if receivedNum == 6:
    numView = '110'
else:
    numView = '111'


send_view()

"""
Dec. 21 1:33PM FOrtiz

Implemented the test Module for the ROS interaction 


"""
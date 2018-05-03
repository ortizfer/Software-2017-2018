#!/usr/bin/env python3

import rospy
from rumarino_package.msg import HorizontalMotors
from geometry_msgs.msg import Twist




def controller_callback(data):
    global motor_pub
    msg = HorizontalMotors()
    left_motor = data.linear.x + data.angular.z
    right_motor = data.linear.x - data.angular.z
    msg.left_motor = left_motor
    msg.right_motor = right_motor
    print("Left motor: " + left_motor + " Right motor: " + right_motor)
    motor_pub.publish(msg)






def run_code():
    global motor_pub

    rospy.init_node("phone_to_motors")

    motor_pub = rospy.Publisher("horizontal_motor", HorizontalMotors, queue_size = 10)
    controller_sub = rospy.Subscriber("cmd_vel", HorizontalMotors, controller_callback)
    
    rate = rospy.Rate(10)
    print("IT WORKS")
    rospy.spin()


if __name__ == '__main__':
    run_code()

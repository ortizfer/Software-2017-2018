#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32, Float64

CONTROLLER_GAIN = 0.5
MOTOR_CAP = 50
set_point = 60.0


def motor_publishers():
    global pub
    pub = rospy.Publisher('vertical_motor1', Int32, queue_size=10)




def run_controller(yaw):
    # error = set_point-yaw.data
    # if(error > 180):
    #     error -= 360
    #
    # elif (error < -180):
    #     error += 360
    #
    # motor_speed = error*CONTROLLER_GAIN
    #
    # if(motor_speed > MOTOR_CAP):
    #     motor_speed = MOTOR_CAP
    # elif( motor_speed < MOTOR_CAP*-1):
    #     motor_speed = -1*MOTOR_CAP


    pub.publish(int(motor_speed))



def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)
    run_controller(data)


def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    motor_publishers()
    rospy.init_node('align_controller')

    rospy.Subscriber('align_setpoint', rosmsg , callback)
    rospy.Subscriber('align_movement', rosmsg , callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()

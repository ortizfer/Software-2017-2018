#!/usr/bin/env python

import rospy
import datetime
from std_msgs.msg import String


def __datetime_to_seconds(date):
    hours = int(date.hour)*3600
    minutes = int(date.minute)*60
    seconds = int(date.second)
    return hours+minutes+seconds


start = __datetime_to_seconds(datetime.datetime.now().time())
max_time = 15*60


rospy.init_node('adaptive_timer', anonymous=True)
pub = rospy.Publisher('time_response', String, queue_size=4)

while not rospy.is_shutdown():
    current = __datetime_to_seconds(datetime.datetime.now().time())
    elapsed = current - start
    remaining = max_time - elapsed
    if remaining > 0:
        pub.publish(str(remaining))
        # print("Remaining time: " + str(remaining))

    else:
        pub.publish(str(0))
        # print("DONE")







'''
def callback(data):
    if data.data == 'a' and not rospy.is_shutdown():
        current = __datetime_to_seconds(datetime.datetime.now().time())
        elapsed = current - start
        remaining = max_time - elapsed
        if remaining > 0:
            pub.publish(str(remaining))
            print("Remaining time: " + str(remaining))

        else:
            pub.publish(str(0))
            print("DONE")

    else:
        print("Incorrect inquiry")


def listener():
    rospy.init_node('adaptive_timer', anonymous=True)
    rospy.Subscriber("time_inquiry", String, callback)
    print("Adaptive Timer ready...")
    rospy.spin()


if __name__ == '__main__':
    listener()
'''
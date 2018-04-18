import rospy
from std_msgs.msg import Float64, Float32

rospy.init_node("dummy_qualifying_mission", anonymous=True)
pub = rospy.Publisher("horizontal_controller", Float64)
angle_error = 2
while not rospy.is_shutdown():
    msg = rospy.wait_for_message("visionAngleChatter", Float64)
    aligned = False
    initial_heading = rospy.wait_for_message("align_controller_set_point", Float32)
    desired_heading = initial_heading + msg.data
    pub.publish(msg)
    while not aligned:
        current_heading = rospy.wait_for_message("align_controller_set_point", Float32)
        bot_heading = desired_heading - angle_error  # Error Margin boundary
        top_heading = desired_heading + angle_error  # Error Margin boundary
        if bot_heading < current_heading < top_heading:
            aligned = True

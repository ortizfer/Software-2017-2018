#!/bin/bash

roscore &
cd ~/Software-2017-2018/QualifyingDT/
python3 vn100.py &
python align_controller.py &
python depth_controller.py &
export ROS_IP=10.0.0.5
source ../ROS/catkin_ws/devel/setup.bash
rosrun rosserial_python serial_node.py /dev/ttyACM0 &
#python Vision_Test.py &

#!/bin/bash

roscore &
sleep 2 rosrun rosserial_python serial_node.py /dev/ttyACM0 &
cd ~/Software-2017-2018/QualifyingDT/
python3 vn100.py &
python align_controller.py &
python depth_controller.py &
export ROS_IP=192.168.43.9

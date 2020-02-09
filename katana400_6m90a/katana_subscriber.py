#!/usr/bin/env python

import rospy
import math
from std_msgs.msg import String

from std_msgs.msg import Float64
from math import sin, cos, atan2, sqrt, fabs

from sensor_msgs.msg import Range


def callback1(msg):
	rospy.loginfo("Motor 1 position = q %s", msg.data) 

def callback2(msg):
	rospy.loginfo("Motor 2 position = q %s", msg.data) 

def callback3(msg):
	rospy.loginfo("Motor 3 position = q %s", msg.data) 

def callback4(msg):
	rospy.loginfo("Motor 4 position = q %s", msg.data) 

def callback5(msg):
	rospy.loginfo("Motor 5 position = q %s", msg.data) 

def listener():
    
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('/katana_400_6m90G/katana_motor1_pan_joint_position_controller/command', Float64, callback1, queue_size=1000)
    rospy.Subscriber('/katana_400_6m90G/katana_motor2_lift_joint_position_controller/command', Float64, callback2, queue_size=1000)
    rospy.Subscriber('/katana_400_6m90G/katana_motor3_lift_joint_position_controller/command', Float64, callback3, queue_size=1000)
    rospy.Subscriber('/katana_400_6m90G/katana_motor4_lift_joint_position_controller/command', Float64, callback4, queue_size=1000)
    rospy.Subscriber('/katana_400_6m90G/katana_motor5_wrist_roll_joint_position_controller/command', Float64, callback5, queue_size=1000)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()


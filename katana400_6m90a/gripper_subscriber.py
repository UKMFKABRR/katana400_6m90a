#!/usr/bin/env python

import rospy
import math
from std_msgs.msg import String

from std_msgs.msg import Float64
from math import sin, cos, atan2, sqrt, fabs

from sensor_msgs.msg import Range


def callback1(msg):
	rospy.loginfo("Gripper left position = q %s", msg.data) 

def callback2(msg):
	rospy.loginfo("Gripper right position = q %s", msg.data) 

def listener():
    
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('/katana_400_6m90G/katana_l_finger_joint_position_controller/command', Float64, callback1, queue_size=1000)
    rospy.Subscriber('/katana_400_6m90G/katana_r_finger_joint_position_controller/command', Float64, callback2, queue_size=1000)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()

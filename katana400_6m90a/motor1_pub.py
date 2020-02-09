import rospy
import math
from std_msgs.msg import String

from std_msgs.msg import Float64

from control_msgs.msg import JointControllerState 

from std_msgs.msg import Float64
from math import sin, cos, atan2, sqrt, fabs

# Define .....

def callback1(msg):
    rospy.loginfo("Motor actual 1 position = q1 %f", msg.process_value)
 
def callback2(msg):
    rospy.loginfo("Motor actual 2 position = q2 %f", msg.process_value)
 
def callback3(msg):
    rospy.loginfo("Motor actual 3 position = q3 %f", msg.process_value)

def callback4(msg):
    rospy.loginfo("Motor actual 4 position = q4 %f", msg.process_value)

def callback5(msg):
    rospy.loginfo("Motor actual 5 position = q5 %f", msg.process_value) 

def listener():
        rospy.init_node('encoder_values')
        joint1state = rospy.Subscriber('/katana_400_6m90G/katana_motor1_pan_joint_position_controller/state', JointControllerState, callback1, queue_size=10)
	joint2state = rospy.Subscriber('/katana_400_6m90G/katana_motor2_lift_joint_position_controller/state', JointControllerState, callback2)
	joint3state = 	rospy.Subscriber('/katana_400_6m90G/katana_motor3_lift_joint_position_controller/state', JointControllerState, callback3)
	joint4state = 	rospy.Subscriber('/katana_400_6m90G/katana_motor4_lift_joint_position_controller/state', JointControllerState, callback4)
	joint5state = 	rospy.Subscriber('/katana_400_6m90G/katana_motor5_wrist_roll_joint_position_controller/state', JointControllerState, callback5)
        

	#rospy.spin()

if __name__ == '__main__':
    listener()

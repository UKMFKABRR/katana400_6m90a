import rospy
import math
from std_msgs.msg import String

from std_msgs.msg import Float64

from control_msgs.msg import JointControllerState 

# Define .....

def callback1(msg):
    rospy.loginfo("Gripper left actual position =  %f", msg.process_value)
 
def callback2(msg):
    rospy.loginfo("Gripper right actual position =  %f", msg.process_value)
 

def listener():
        rospy.init_node('encoder_values')
        katana_l_finger_state = rospy.Subscriber('/katana_400_6m90G/katana_l_finger_joint_position_controller/state', JointControllerState, callback1, queue_size=10)
	katana_r_finger_state = rospy.Subscriber('/katana_400_6m90G/katana_r_finger_joint_position_controller/state', JointControllerState, callback2, queue_size=10)
     

	rospy.spin()

if __name__ == '__main__':
    listener()

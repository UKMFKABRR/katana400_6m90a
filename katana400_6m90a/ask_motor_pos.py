import rospy
import math
from std_msgs.msg import String

from std_msgs.msg import Float64

from control_msgs.msg import JointControllerState 

from std_msgs.msg import Float64
from math import sin, cos, atan2, sqrt, fabs

joint1state = rospy.Subscriber('/katana_400_6m90G/katana_motor1_pan_joint_position_controller/state', JointControllerState, queue_size=10)
joint2state = rospy.Subscriber('/katana_400_6m90G/katana_motor2_lift_joint_position_controller/state', JointControllerState, queue_size=10)
joint3state = rospy.Subscriber('/katana_400_6m90G/katana_motor3_lift_joint_position_controller/state', JointControllerState,  queue_size=10)
joint4state = rospy.Subscriber('/katana_400_6m90G/katana_motor4_lift_joint_position_controller/state', JointControllerState, queue_size=10)
joint5state = rospy.Subscriber('/katana_400_6m90G/katana_motor5_wrist_roll_joint_position_controller/state', JointControllerState, queue_size=10)

def katana_current_joints_position():

    	print "This is current katana_position:" 
    	print "%.2f joint1 position:" 
    	listener1()
    	print "%.2f joint2 position:" 
    	listener2()
	print "%.2f joint3 position:" 
    	listener3()
	print "%.2f joint4 position:" 
  	listener4() 
	print "%.2f joint5 position:" 
	listener5()
    	rospy.sleep(2)

def callback_all(msg):
    	rospy.loginfo("Motor actual 1 position = q1 %f", msg.process_value)
	rospy.loginfo("Motor actual 2 position = q1 %f", msg.process_value)
	rospy.loginfo("Motor actual 3 position = q1 %f", msg.process_value)
	rospy.loginfo("Motor actual 4 position = q1 %f", msg.process_value)
	rospy.loginfo("Motor actual 5 position = q1 %f", msg.process_value)


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


def listener_all():
	global joint1state, joint2state, joint3state, joint4state, joint5state
 	joint1state = rospy.Subscriber('/katana_400_6m90G/katana_motor1_pan_joint_position_controller/state', JointControllerState, callback1, queue_size=10)
	joint2state = rospy.Subscriber('/katana_400_6m90G/katana_motor2_lift_joint_position_controller/state', JointControllerState, callback2, queue_size=10)
	joint3state = rospy.Subscriber('/katana_400_6m90G/katana_motor3_lift_joint_position_controller/state', JointControllerState, callback3, queue_size=10)
	joint4state = rospy.Subscriber('/katana_400_6m90G/katana_motor4_lift_joint_position_controller/state', JointControllerState, callback4,queue_size=10)
	joint5state = rospy.Subscriber('/katana_400_6m90G/katana_motor5_wrist_roll_joint_position_controller/state', JointControllerState, callback5, queue_size=10)

def listener1():
	global joint1state        
	#rospy.init_node('encoder1_values')
        joint1state = rospy.Subscriber('/katana_400_6m90G/katana_motor1_pan_joint_position_controller/state', JointControllerState, callback1, queue_size=10)
        #wait_for_message(topic, topic_type, timeout=None)
def listener2():
	global joint2state 
	joint2state = rospy.Subscriber('/katana_400_6m90G/katana_motor2_lift_joint_position_controller/state', JointControllerState, callback2, queue_size=10)

def listener3():
	global joint3state 
	joint3state = 	rospy.Subscriber('/katana_400_6m90G/katana_motor3_lift_joint_position_controller/state', JointControllerState, callback3, queue_size=10)

def listener4():
	global joint4state 
	joint4state = 	rospy.Subscriber('/katana_400_6m90G/katana_motor4_lift_joint_position_controller/state', JointControllerState, callback4,queue_size=10)

def listener5():
	global joint5state 
	joint5state = 	rospy.Subscriber('/katana_400_6m90G/katana_motor5_wrist_roll_joint_position_controller/state', JointControllerState, callback5, queue_size=10)
        

def katana_position_asking():
    motor_pos = float(input('Which motor position to check? '))
    if motor_pos == 1:
			listener1()
			print "%.2f This is joint1 current position that you ask:" 
    else: 
        if motor_pos == 2:
             		listener2()
			print "%.2f This is joint2 current position that you ask:" 
        else: 
            if motor_pos ==3:
                	listener3()
			print "%.2f This is joint3 current position that you ask:" 
            else:   
                if motor_pos == 4:
                    	listener4()
			print "%.2f This is joint4 current position that you ask" 
                else:
                   	listener5()
			print "%.2f This is joint5 current position that you ask:" 
   		
    			rospy.sleep(1)

def katana_current_positions_subscriber():
    global joint1state, joint2state, joint3state, joint4state, joint5state
    positioning = True

    # Initialization of node for controlling joint1 and joint2 positions.
    rospy.init_node('katana_positions_node', anonymous=True)

    rate = rospy.Rate(80)  # Rate 80 Hz

    while not rospy.is_shutdown() and positioning:

#read current position
	#katana_current_joints_position()
	rospy.sleep(0.5)

#step asking for current position
        print "This is to ask the current position of each motor:"
	katana_position_asking() 
        

	rospy.sleep(1)
	positioning = False
        print "This is to show all motor current position"
	listener_all()
	    
	print "End of positioning!"



if __name__ == '__main__':
    try:
        katana_current_positions_subscriber()
	#listener_all()
    except rospy.ROSInterruptException:
        pass

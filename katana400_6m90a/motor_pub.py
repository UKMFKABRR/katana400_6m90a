import rospy
import math
from std_msgs.msg import String

from std_msgs.msg import Float64

from control_msgs.msg import JointControllerState 

from std_msgs.msg import Float64
from math import sin, cos, atan2, sqrt, fabs

# Define publishers for joint1 and joint2 position controller commands.
joint1publisher = rospy.Publisher('/katana_400_6m90G/katana_motor1_pan_joint_position_controller/command', Float64, queue_size=10)
joint2publisher = rospy.Publisher('/katana_400_6m90G/katana_motor2_lift_joint_position_controller/command', Float64, queue_size=10)
joint3publisher = rospy.Publisher('/katana_400_6m90G/katana_motor3_lift_joint_position_controller/command', Float64, queue_size=10)
joint4publisher = rospy.Publisher('/katana_400_6m90G/katana_motor4_lift_joint_position_controller/command', Float64, queue_size=10)
joint5publisher = rospy.Publisher('/katana_400_6m90G/katana_motor5_wrist_roll_joint_position_controller/command', Float64, queue_size=10)


joint1state = rospy.Subscriber('/katana_400_6m90G/katana_motor1_pan_joint_position_controller/state', JointControllerState, queue_size=10)
joint2state = rospy.Subscriber('/katana_400_6m90G/katana_motor2_lift_joint_position_controller/state', JointControllerState, queue_size=10)
joint3state = rospy.Subscriber('/katana_400_6m90G/katana_motor3_lift_joint_position_controller/state', JointControllerState,  queue_size=10)
joint4state = rospy.Subscriber('/katana_400_6m90G/katana_motor4_lift_joint_position_controller/state', JointControllerState, queue_size=10)
joint5state = rospy.Subscriber('/katana_400_6m90G/katana_motor5_wrist_roll_joint_position_controller/state', JointControllerState, queue_size=10)

def katana_initial_joints_position(joint1initial_position, joint2initial_position, joint3initial_position, joint4initial_position,joint5initial_position):
    publish_joints_position(joint1initial_position, joint2initial_position, joint3initial_position, joint4initial_position, joint5initial_position)
    print "This is katana_initial position:" 
    print "%.2f joint1 position:" % (joint1initial_position)
    print "%.2f joint2 position:" % (joint2initial_position)
    print "%.2f joint3 position:" % (joint3initial_position)
    print "%.2f joint4 position:" % (joint4initial_position)
    print "%.2f joint5 position:" % (joint5initial_position)
    rospy.sleep(6)

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

def katana_zero_position(joint1initial_position, joint2initial_position, joint3initial_position, joint4initial_position, joint5initial_position):
        joint1_position = 0.0
        joint2_position = 0.0
        joint3_position = 0.0
        joint4_position = 0.0
        joint5_position = 0.0

        publish_joints_position(joint1_position, joint2_position, joint3_position, joint4_position, joint5_position)  
        print "joint1 zero position: %.2f " % (joint1_position)
        print "joint2 zero position: %.2f " % (joint2_position)
        print "joint3 zero position: %.2f " % (joint3_position)
        print "joint4 zero position: %.2f " % (joint4_position)
        print "joint5 zero position: %.2f " % (joint4_position)
        rospy.sleep(3)
        return joint1_position, joint2_position, joint3_position, joint4_position, joint5_position


def katana_standby(joint1initial_position, joint2initial_position, joint3initial_position, joint4initial_position, joint5initial_position, move_step_joint1, move_step_joint2, move_step_joint3, move_step_joint4, move_step_joint5):
    for x in range(0, 28):
        joint1_position = joint1initial_position + move_step_joint1 * x
        joint2_position = joint2initial_position + move_step_joint2 * x
        joint3_position = joint3initial_position - move_step_joint3 * x
        joint4_position = joint4initial_position - move_step_joint4 * x
        joint5_position = joint5initial_position - move_step_joint5 * x

        publish_joints_position(joint1_position, joint2_position, joint3_position, joint4_position, joint5_position)  
        print "%.2f joint1 standby position:" % (joint1_position)
        print "%.2f joint2 standby position:" % (joint2_position)
        print "%.2f joint3 standby position:" % (joint3_position)
        print "%.2f joint4 standby position:" % (joint4_position)
        print "%.2f joint5 standby position:" % (joint4_position)
    rospy.sleep(3)
    return joint1_position, joint2_position, joint3_position, joint4_position, joint5_position



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
   
    print('Try again')


    rospy.sleep(1)
    
# Define .....
def publish_joints_position(joint1_position, joint2_position, joint3_position, joint4_position, joint5_position):
    joint1publisher.publish(joint1_position)
    joint2publisher.publish(joint2_position)
    joint3publisher.publish(joint3_position)
    joint4publisher.publish(joint4_position)
    joint5publisher.publish(joint5_position)

	
def callback1(msg):
    rospy.loginfo("Motor 1 actual position = q1 %f", msg.process_value)
 
def callback2(msg):
    rospy.loginfo("Motor 2 actual position = q2 %f", msg.process_value)
 
def callback3(msg):
    rospy.loginfo("Motor 3 actual position = q3 %f", msg.process_value)

def callback4(msg):
    rospy.loginfo("Motor 4 actual position = q4 %f", msg.process_value)

def callback5(msg):
    rospy.loginfo("Motor 5 actual position = q5 %f", msg.process_value) 

def listener1():
	global joint1state        
	#rospy.init_node('encoder1_values')
        joint1state = rospy.Subscriber('/katana_400_6m90G/katana_motor1_pan_joint_position_controller/state', JointControllerState, callback1, queue_size=10)
        
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
        

	#rospy.spin()
def katana_positions_publisher():
    global joint1publisher, joint2publisher, joint3publisher, joint4publisher, joint5publisher
    positioning = True
    joint1initial_position = 0.0
    joint2initial_position = 0.0
    joint3initial_position = 0.0
    joint4initial_position = 0.0
    joint5initial_position = 0.0
    move_step_joint1 = 0.1	
    move_step_joint2 = 0.1
    move_step_joint3 = 0.1
    move_step_joint4 = 0.1
    move_step_joint5 = 0.1
    
    joint1current_position = joint1initial_position
    joint2current_position = joint2initial_position
    joint3current_position = joint3initial_position
    joint4current_position = joint4initial_position
    joint5current_position = joint5initial_position

    # Initialization of node for controlling joint1 and joint2 positions.
    rospy.init_node('joint_positions_node', anonymous=True)

    rate = rospy.Rate(80)  # Rate 80 Hz

    while not rospy.is_shutdown() and positioning:

#read current position
	#katana_current_joints_position()
	rospy.sleep(0.5)
#read initial position  
	katana_initial_joints_position(joint1initial_position, joint2initial_position,joint3initial_position,joint4initial_position,joint5initial_position) 
        rospy.sleep(3)
	katana_zero_position(joint1initial_position, joint2initial_position, joint3initial_position, joint4initial_position, joint5initial_position)
	rospy.sleep(3)
#step moving to standby
        print "This is katana_standby position:" 
        joint1current_position, joint2current_position, joint3current_position,joint4current_position,joint5current_position = katana_standby(joint1initial_position, joint2initial_position, joint3initial_position, joint4initial_position, joint5initial_position, move_step_joint1, move_step_joint2, move_step_joint3, move_step_joint4, move_step_joint5)
        print "End of katana_standby position:" 
        rospy.sleep(3)

#step asking for current position
        print "This is to ask the current position of each motor:"
	katana_position_asking() 
        

	rospy.sleep(2)
        positioning = False
    
	print "End of positioning!"



if __name__ == '__main__':
    try:
        katana_positions_publisher()
    except rospy.ROSInterruptException:
        pass

#!/usr/bin/env python

##This is program for katana400_6m90G. Adopted from 2dof rrbot.(https://github.com/srebroa/rrbot_pushing_object)

import rospy
import math

from std_msgs.msg import Float64
from math import sin, cos, atan2, sqrt, fabs
from std_msgs.msg import String

from control_msgs.msg import JointControllerState 


# Define publishers for joint1 and joint2 position controller commands.
joint1publisher = rospy.Publisher('/katana_400_6m90G/katana_motor1_pan_joint_position_controller/command', Float64, queue_size=10)
joint2publisher = rospy.Publisher('/katana_400_6m90G/katana_motor2_lift_joint_position_controller/command', Float64, queue_size=10)
joint3publisher = rospy.Publisher('/katana_400_6m90G/katana_motor3_lift_joint_position_controller/command', Float64, queue_size=10)
joint4publisher = rospy.Publisher('/katana_400_6m90G/katana_motor4_lift_joint_position_controller/command', Float64, queue_size=10)
joint5publisher = rospy.Publisher('/katana_400_6m90G/katana_motor5_wrist_roll_joint_position_controller/command', Float64, queue_size=10)

gripper_l_publisher = rospy.Publisher('/katana_400_6m90G/katana_l_finger_joint_position_controller/command', Float64, queue_size=10)
gripper_r_publisher = rospy.Publisher('/katana_400_6m90G/katana_r_finger_joint_position_controller/command', Float64, queue_size=10)

joint1state = rospy.Subscriber('/katana_400_6m90G/katana_motor1_pan_joint_position_controller/state', JointControllerState, queue_size=10)
joint2state = rospy.Subscriber('/katana_400_6m90G/katana_motor2_lift_joint_position_controller/state', JointControllerState,  queue_size=10)
joint3state = rospy.Subscriber('/katana_400_6m90G/katana_motor3_lift_joint_position_controller/state', JointControllerState,  queue_size=10)
joint4state = rospy.Subscriber('/katana_400_6m90G/katana_motor4_lift_joint_position_controller/state', JointControllerState,  queue_size=10)
joint5state = rospy.Subscriber('/katana_400_6m90G/katana_motor5_wrist_roll_joint_position_controller/state', JointControllerState,  queue_size=10)




###THIS IS GRIPPER MAIN FUNCTION ####

def gripper_positions_publisher():
    global gripper_l_publisher, gripper_r_publisher
    positioning = True
    gripper_l_initial_position = 0.0
    gripper_r_initial_position = 0.0

    move_step_joint1 = 0.1	
    move_step_joint2 = 0.1

    step_upward1 = 0.02
    step_upward2 = 0.02

    
    gripper_l_current_position = gripper_l_initial_position
    gripper_r_current_position = gripper_r_initial_position

    rate = rospy.Rate(80)  # Rate 80 Hz

    while not rospy.is_shutdown() and positioning:
#read initial position
        print "This is gripper initial position:" 
        gripper_initial_position(gripper_l_initial_position, gripper_r_initial_position) 

        rospy.sleep(3)
#step moving to standby
        print "This is gripper fully open position:" 
        gripper_l_current_position, gripper_r_current_position = gripper_full_open(gripper_l_initial_position, gripper_r_initial_position, move_step_joint1, move_step_joint2)    
        rospy.sleep(3)

#step moving to standby
        print "This is gripper half close position:" 
        gripper_l_current_position, gripper_r_current_position = gripper_half_close(gripper_l_initial_position, gripper_r_initial_position, move_step_joint1, move_step_joint2)    
        rospy.sleep(3)

#step moving to standby
        print "This is fripper fully close position:" 
        gripper_l_current_position, gripper_r_current_position = gripper_full_close(gripper_l_initial_position, gripper_r_initial_position, move_step_joint1, move_step_joint2)
        rospy.sleep(3)

        positioning = False
    
	print "End of gripper positioning program!"

###THIS IS KATANA FUNCTION ####

def katana_initial_joints_position(joint1initial_position, joint2initial_position, joint3initial_position, joint4initial_position,joint5initial_position):
    publish_joints_position(joint1initial_position, joint2initial_position, joint3initial_position, joint4initial_position, joint5initial_position)
    print "This is katana_initial position:" 
    print "%.2f joint1 position:" % (joint1initial_position)
    print "%.2f joint2 position:" % (joint2initial_position)
    print "%.2f joint3 position:" % (joint3initial_position)
    print "%.2f joint4 position:" % (joint4initial_position)
    print "%.2f joint5 position:" % (joint5initial_position)
rospy.sleep(6)

def katana_standby(joint1initial_position, joint2initial_position, joint3initial_position, joint4initial_position, joint5initial_position, move_step_joint1, move_step_joint2, move_step_joint3, move_step_joint4, move_step_joint5):
    for x in range(0, 50):
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

def katana_near_object(joint1initial_position, joint2initial_position, joint3initial_position, joint4initial_position, joint5initial_position, move_step_joint1, move_step_joint2, move_step_joint3, move_step_joint4, move_step_joint5):
    #for x in range(0, 23):
        joint1_position = 0.25
        joint2_position = -0.135
        joint3_position = -0.4
        joint4_position = 1.57
        joint5_position = 0.0

        publish_joints_position(joint1_position, joint2_position, joint3_position, joint4_position, joint5_position)
        #print "This is katana_pushing position:" 
        print "%.2f joint1 near object position:" % (joint1_position)
        print "%.2f joint2 near object position:" % (joint2_position)
        print "%.2f joint3 near object position:" % (joint3_position)
        print "%.2f joint4 near object position:" % (joint4_position)
        print "%.2f joint5 near object position:" % (joint4_position)
             

        rospy.sleep(0.5)
        return joint1_position, joint2_position, joint3_position, joint4_position, joint5_position

#step 3 Moving to above object
def katana_above_object(joint1_position, joint2_position, joint3_position, joint4_position, joint5_position, step_upward1, step_upward2, step_upward3, step_upward4, step_upward5):
    #for x in range(1, 50):
        joint1_position = 0.3  #joint1_position + step_upward1*0
        joint2_position = 0.0  #%joint2_position - step_upward2*0
        joint3_position = 0.0  #joint3_position - step_upward3*0
        joint4_position = 1.57 #joint4_position*0
        joint5_position = 0.0  # joint5_position*0-35

        publish_joints_position(joint1_position, joint2_position, joint3_position, joint4_position, joint5_position)
        rospy.sleep(0.2)
        print "%.2f joint1 position:" % (joint1_position)
        print "%.2f joint2 position:" % (joint2_position)
        print "%.2f joint3 position:" % (joint3_position)
        print "%.2f joint4 position:" % (joint4_position)
        print "%.2f joint5 position:" % (joint4_position)

        return joint1_position, joint2_position, joint3_position, joint4_position, joint5_position

#step 4 Moving to to pick object
def katana_pick_object(joint1_position, joint2_position, joint3_position, joint4_position, joint5_position, step_upward1, step_upward2, step_upward3, step_upward4, step_upward5):
    for x in range(1, 50):
        joint1_position = joint1_position + step_upward1*0
        joint2_position = joint2_position - step_upward2*0
        joint3_position = joint3_position - step_upward3*0
        joint4_position = joint4_position*0
        joint5_position = joint5_position*0-35

        publish_joints_position(joint1_position, joint2_position, joint3_position, joint4_position, joint5_position)
        rospy.sleep(0.2)
        print "%.2f joint1 position:" % (joint1_position)
        print "%.2f joint2 position:" % (joint2_position)
        print "%.2f joint3 position:" % (joint3_position)
        print "%.2f joint4 position:" % (joint4_position)
        print "%.2f joint5 position:" % (joint4_position)

    return joint1_position, joint2_position, joint3_position, joint4_position, joint5_position


def katana_lift_up(joint1_position, joint2_position, joint3_position, joint4_position, joint5_position, step_upward1, step_upward2, step_upward3, step_upward4, step_upward5):
    for x in range(1, 5):
        joint2_position = 1.5 - step_upward2 * x*0
        publish_joints_position(joint1_position, joint2_position, joint3_position, joint4_position, joint5_position)
        rospy.sleep(0.2)
        print "%.2f joint1 position:" % (joint1_position)
        print "%.2f joint2 position:" % (joint2_position)
        print "%.2f joint3 position:" % (joint3_position)
        print "%.2f joint4 position:" % (joint4_position)
        print "%.2f joint5 position:" % (joint4_position)

    return joint1_position, joint2_position, joint3_position, joint4_position, joint5_position

def katana_safe_position():
	global joint1_position, joint2_position, joint3_position, joint4_position, joint5_position, gripper_l_position, gripper_r_position
	positioning = True
	joint1_position = -0.25 
	joint2_position = 0.75
	joint3_position = 1.25
	joint4_position = 0.75 
	joint5_position = 0.0 
	gripper_l_position = 0.1
	gripper_r_position = 0.1
        publish_joint_gripper_position(joint1_position, joint2_position, joint3_position, joint4_position, joint5_position, gripper_l_position, gripper_r_position)
        print "Goint to safe position:"
	rospy.sleep(0.2) 
        print "joint1 position: %.2f " % (joint1_position)
        print "joint2 position: %.2f " % (joint2_position)
        print "joint3 position: %.2f " % (joint3_position)
        print "joint3 position: %.2f " % (joint4_position)
        print "joint5 position: %.2f " % (joint5_position)
        print "gripper left position: %.2f " % (gripper_l_position)
        print "gripper right position: %.2f " % (gripper_r_position)
 	rospy.sleep(0.2)
        return joint1_position, joint2_position, joint3_position, joint4_position, joint5_position, gripper_l_position, gripper_r_position
	positioning = False

def publish_joints_position(joint1_position, joint2_position, joint3_position, joint4_position, joint5_position):
    joint1publisher.publish(joint1_position)
    joint2publisher.publish(joint2_position)
    joint3publisher.publish(joint3_position)
    joint4publisher.publish(joint4_position)
    joint5publisher.publish(joint5_position)

def publish_joint_position(joint_position, joint_number):
    if joint_number == 1:
        joint1publisher.publish(joint_position)
    elif joint_number == 2:
        joint2publisher.publish(joint_position)
    elif joint_number == 3:
        joint3publisher.publish(joint_position)
    elif joint_number == 4:
        joint4publisher.publish(joint_position)
    elif joint_number == 5:
        joint5publisher.publish(joint_position)

def publish_joint_gripper_position(joint1_position, joint2_position, joint3_position, joint4_position, joint5_position, gripper_l_position, gripper_r_position):
    joint1publisher.publish(joint1_position)
    joint2publisher.publish(joint2_position)
    joint3publisher.publish(joint3_position)
    joint4publisher.publish(joint4_position)
    joint5publisher.publish(joint5_position)
    gripper_l_publisher.publish(gripper_l_position)
    gripper_r_publisher.publish(gripper_r_position)

#THIS IS GRIPPER FUNCTION #
def gripper_initial_position(gripper_l_initial_position, gripper_r_initial_position): 
	publish_gripper_position(gripper_l_initial_position, gripper_r_initial_position)

	print "%.2f gripper left initial position :" % (gripper_l_initial_position)
	print "%.2f gripper right initial position :" % (gripper_r_initial_position)

rospy.sleep(6)

def gripper_full_open(gripper_l_initial_position, gripper_r_initial_position, move_step_joint1, move_step_joint2):
    for x in range(0, 25):
        gripper_l_position = gripper_l_initial_position + move_step_joint1 * x
    for y in range(-25, 0):
        gripper_r_position = gripper_r_initial_position + move_step_joint2 * y


        publish_gripper_position(gripper_l_position, gripper_r_position)
        
        print "%.2f gripper left full open :" % (gripper_l_position )
        print "%.2f gripper right full open :" % (gripper_r_position )


        rospy.sleep(3)
        return gripper_l_position, gripper_r_position

def gripper_half_close(gripper_l_initial_position, gripper_r_initial_position, move_step_joint1, move_step_joint2):
    #for x in range(0, 23):
        gripper_l_position = -0.240
        gripper_r_position = 0.2


        publish_gripper_position(gripper_l_position, gripper_r_position)
        print "This is half close position:" 
        print "%.2f gripper left half close :" % (gripper_l_position )
        print "%.2f gripper right half close :" % (gripper_r_position )
              

        rospy.sleep(0.5)
        return gripper_l_position, gripper_r_position

def gripper_full_close(gripper_l_initial_position, gripper_r_initial_position, move_step_joint1, move_step_joint2):
    #for x in range(0, 23):
        gripper_l_position = -0.36
        gripper_r_position = -0.35


        publish_gripper_position(gripper_l_position, gripper_r_position)
        print "This is gripper full close:" 
        print "gripper left full close : %.2f " % (gripper_l_position )
        print "gripper right full close : %.2f " % (gripper_r_position )
              

        rospy.sleep(0.5)
        return gripper_l_position, gripper_r_position

def publish_gripper_position(gripper_l_position, gripper_r_position):
    gripper_l_publisher.publish(gripper_l_position)
    gripper_r_publisher.publish(gripper_r_position)

###THiS IS SUBSCRIBER OF CURRENT POSITION #########

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
	global joint1state, joint2state, joint3state, joint4state, joint5state
        #rospy.init_node('encoder_values')
        joint1state = rospy.Subscriber('/katana_400_6m90G/katana_motor1_pan_joint_position_controller/state', JointControllerState, callback1, queue_size=10)
	joint2state = rospy.Subscriber('/katana_400_6m90G/katana_motor2_lift_joint_position_controller/state', JointControllerState, callback2)
	joint3state = 	rospy.Subscriber('/katana_400_6m90G/katana_motor3_lift_joint_position_controller/state', JointControllerState, callback3)
	joint4state = 	rospy.Subscriber('/katana_400_6m90G/katana_motor4_lift_joint_position_controller/state', JointControllerState, callback4)
	joint5state = 	rospy.Subscriber('/katana_400_6m90G/katana_motor5_wrist_roll_joint_position_controller/state', JointControllerState, callback5)
        

	#rospy.spin()

###THIS IS KATANA MAIN FUNCTION ####
def katana_positions_publisher():
    global joint1publisher, joint2publisher, joint3publisher, joint4publisher, joint5publisher
    global joint1state, joint2state, joint3state, joint4state, joint5state
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
    step_upward1 = 0.02
    step_upward2 = 0.02
    step_upward3 = 0.02
    step_upward4 = 0.02
    step_upward5 = 0.02
    
    joint1current_position = joint1state
    joint2current_position = joint2initial_position
    joint3current_position = joint3initial_position
    joint4current_position = joint4initial_position
    joint5current_position = joint5initial_position

    # Initialization of node for controlling joint1 and joint2 positions.
    rospy.init_node('joint_positions_node', anonymous=True)

    rate = rospy.Rate(80)  # Rate 80 Hz

    while not rospy.is_shutdown() and positioning:
#read initial position
        katana_initial_joints_position(joint1initial_position, joint2initial_position,joint3initial_position,joint4initial_position,joint5initial_position) 

        rospy.sleep(3)

#read current position
	print "This is katana_current position--still no success:" 
        #katana_initial_joints_position(joint1state, joint2state,joint3state,joint4state,joint5state) 

        rospy.sleep(3)

#step moving to standby
        print "This is katana_standby position:" 
        joint1current_position, joint2current_position, joint3current_position,joint4current_position,joint5current_position = katana_standby(joint1initial_position, joint2initial_position, joint3initial_position, joint4initial_position, joint5initial_position, move_step_joint1, move_step_joint2, move_step_joint3, move_step_joint4, move_step_joint5)
        print "End of katana_standby position:" 
        rospy.sleep(3)

#step  Lift arm straight
        print "Moving katana_lift up position:"
        joint1current_position = katana_lift_up(joint1current_position, joint2current_position, joint3current_position,joint4current_position,joint5current_position, step_upward1, step_upward2, step_upward3, step_upward4, step_upward5)

        rospy.sleep(2)
#step  Moving to above object
        print "Moving katana_to_above object:"
        joint1current_position, joint2current_position, joint3current_position,joint4current_position,joint5current_position = katana_above_object(joint1current_position, joint2current_position, joint3current_position,joint4current_position,joint5current_position, step_upward1, step_upward2, step_upward3, step_upward4, step_upward5)        
        rospy.sleep(3)

#step    Moving to picking
        print "Moving katana_to object picking position:"
        joint1current_position, joint2current_position, joint3current_position,joint4current_position,joint5current_position = katana_near_object(joint1initial_position, joint2initial_position, joint3initial_position, joint4initial_position, joint5initial_position, move_step_joint1, move_step_joint2, move_step_joint3, move_step_joint4, move_step_joint5)
        
        rospy.sleep(2)
        positioning = False
    
	print "End of Katana go to pick positioning!"

# Below code that will continuously run (to stop it press CTRL+C)
if __name__ == '__main__':
    try:
        katana_positions_publisher()
        gripper_positions_publisher()
        katana_safe_position()
	#listener()
    except rospy.ROSInterruptException:
        pass

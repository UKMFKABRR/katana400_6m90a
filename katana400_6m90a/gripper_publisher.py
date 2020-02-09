#!/usr/bin/env python

##This is program for katana400_6m90G. Adopted from 2dof rrbot.(https://github.com/srebroa/rrbot_pushing_object)

import rospy
import math

from std_msgs.msg import Float64
from math import sin, cos, atan2, sqrt, fabs

# Define publishers for joint1 and joint2 position controller commands.
gripper_l_publisher = rospy.Publisher('/katana_400_6m90G/katana_l_finger_joint_position_controller/command', Float64, queue_size=10)
gripper_r_publisher = rospy.Publisher('/katana_400_6m90G/katana_r_finger_joint_position_controller/command', Float64, queue_size=10)


# katana Arm initial joint positions publisher for joint controllers.
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


    # Initialization of node for controlling joint1 and joint2 positions.
    rospy.init_node('gripper_positions_node', anonymous=True)

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
        #print "This is gripper full close:" 
        print "%.2f gripper left full close :" % (gripper_l_position )
        print "%.2f gripper right full close :" % (gripper_r_position )
              

        rospy.sleep(0.5)
        return gripper_l_position, gripper_r_position

def publish_gripper_position(gripper_l_position, gripper_r_position):
    gripper_l_publisher.publish(gripper_l_position)
    gripper_r_publisher.publish(gripper_r_position)


# Below code that will continuously run (to stop it press CTRL+C)
if __name__ == '__main__':
    try:
        gripper_positions_publisher()
    except rospy.ROSInterruptException:
        pass

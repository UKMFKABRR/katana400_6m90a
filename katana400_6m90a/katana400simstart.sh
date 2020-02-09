#!/bin/bash

gnome-terminal -x ./katana400_gazebo_launch.sh
sleep 5 &&
#gnome-terminal -x ./rrbot_ros_control.sh
#sleep 2 &&
#gnome-terminal -x ./katana400_moving_to_object.sh
#sleep 1 &&
gnome-terminal -x ./katana_publisher.sh
 sleep 1 &&
gnome-terminal -x ./katana_subscriber.sh

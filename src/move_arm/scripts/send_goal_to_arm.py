#!/usr/bin/env python3

from __future__ import print_function # Printing
import rospy 
import actionlib # ROS action library
from control_msgs.msg import FollowJointTrajectoryAction, FollowJointTrajectoryGoal 
from std_msgs.msg import Float64 
from trajectory_msgs.msg import JointTrajectoryPoint

def move_arm(
    joint_values: list
)-> None:
    
    """
    move the robot arm to a desired joint configuration

    Args:
        joint_values (list): list of joint angles of the robot
    """
    
    # Create the SimpleActionClient, passing the type of the action to the constructor
    arm_client = actionlib.SimpleActionClient('arm_controller/follow_joint_trajectory', FollowJointTrajectoryAction)

    # Wait for the server to start up and start listening for goals.
    arm_client.wait_for_server()
        
    # Create a new goal to send to the Action Server
    arm_goal = FollowJointTrajectoryGoal()

    # Store the names of each joint of the robot arm
    arm_goal.trajectory.joint_names = ['arm_base_joint', 'shoulder_joint','bottom_wrist_joint' ,'elbow_joint', 'top_wrist_joint']

    # Create a trajectory point   
    point = JointTrajectoryPoint()

    # Store the desired joint values
    point.positions = joint_values

    # Set the time it should in seconds take to move the arm to the desired joint angles
    point.time_from_start = rospy.Duration(3)

    # Add the desired joint values to the goal
    arm_goal.trajectory.points.append(point)

    # Define timeout values
    exec_timeout = rospy.Duration(10)
    prmpt_timeout = rospy.Duration(5)

    # Send a goal to the ActionServer and wait for the server to finish performing the action
    arm_client.send_goal_and_wait(arm_goal, exec_timeout, prmpt_timeout)
    
    

if __name__== "__main__":
    """
    Main method.
    """
    try:
        # Initialize a rospy node so that the SimpleActionClient can
        # publish and subscribe over ROS.
        rospy.init_node('send_goal_to_arm_py')

        # Move the joints of the robot arm to the desired angles in radians
        move_arm([-0.1, 0.5, 0.02, 0, 0])

        print("Robotic arm has successfully reached the goal!")
        
    except rospy.ROSInterruptException:
        print("Program interrupted before completion.", file=sys.stderr)

# move_arm #

- [move_arm](#move_arm)
  - [Description](#description)
  - [Strategy](#strategy)
  - [Dependencies](#dependencies)

## Description ##

send goals to a simulated robot arm.

## Strategy ##

1. Create an action client to communicate with action server.
2. Wait for the server to start up.
3. Create a new goal object to send to action server
4. Store the names of the joints.
5. Create a trajectory point object.
6. Store the desired joint values in the corresponding joint variables.
7. Set the time it should take to achieve the desired angle configuration.
8. add the desired joint configuration to the goal object.
9. Define timeout values.
10. Send the goal to the action server and wait for answer.

## Dependencies ##

- actionlib
- roscpp
- rospy
- std_msgs
- control_msgs
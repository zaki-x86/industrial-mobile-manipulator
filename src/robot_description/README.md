# robot_description #

- [robot\_description](#robot_description)
  - [Description](#description)
  - [Robot Base](#robot-base)
    - [Base specifications](#base-specifications)
    - [Base kinematics](#base-kinematics)
    - [Base software parameters](#base-software-parameters)
  - [Robot Arm](#robot-arm)
    - [Arm Specifications](#arm-specifications)
    - [Arm software parameters](#arm-software-parameters)
  - [Modeling Robot Base](#modeling-robot-base)

## Description ##

describing the physical layout of the robot

## Robot Base ##

### Base specifications ###

- Size: Somewhere within 600 x 450 x 200 (L x B x H, all in mm)
- Type: Four-wheel differential drive robot
- Speed: Up to 1 m/s
- Payload: 50 kg (excluding the robot arm)

### Base kinematics ###

Our robot base has only 2 degrees of freedom: a translation along the x axis and rotation along the z axis. Since our robot moves only on the ground, it cannot translate in the z axis as well.

### Base software parameters ###

Let's consider the mobile robot base as a blackbox: if you give it specific velocity, the robot base should move and, in turn, give the position it has moved to. In ROS terms, the mobile robot takes in information through a
topic called `/cmd_vel` (command velocity) and gives out `/odom` (odometery).

## Robot Arm ##

### Arm Specifications ###

- Type: 5 DOF (short for degrees of freedom) robot arm
- Payload: Within 3-5 kgs

### Arm software parameters ###

So, if we consider the arm a black box, the arm gives out a pose based on the commands each actuator receives. The commands may be in the form of position, force/effort, or velocity commands.

## Modeling Robot Base ##

We used open source 3D models and imported it into robot URDF as meshes. We also used xacro to avoid repition of XML tags in URDF.

**The main tags used in modeling the URDF:**

- `<xacro>` : To help define macros for reuse
- `<links>` : To contain the geometric representations of the robot and visual
information
- `<inertial>` : To contain the mass and moment of inertia of the links
- `<joints>` : To contain connections between the links with constraint definitions
- `<Gazebo>` : To contain plugins to establish a connection between Gazebo and ROS, along with simulation properties

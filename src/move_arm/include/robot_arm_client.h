#include <memory>
#include <ros/ros.h>
#include <actionlib/client/simple_action_client.h>
#include <control_msgs/FollowJointTrajectoryAction.h>
#include <control_msgs/FollowJointTrajectoryGoal.h>
#include <std_msgs/Float64.h>

#ifndef ROBOT_ARM_CLIENT_H

#define ROBOT_ARM_CLIENT_H

typedef actionlib::SimpleActionClient<control_msgs::FollowJointTrajectoryAction> TrajectoryClient;

typedef control_msgs::FollowJointTrajectoryGoal Goal;

class Robot_Arm
{
private:
    std::unique_ptr<TrajectoryClient> client;
public:
    //! Initialize the action client and wait for action server to come up
    Robot_Arm(/* args */);
    //! exit
    ~Robot_Arm();

    void startTrajectory(Goal joint_config);
    Goal setJointConfigurationGoal();
};

Robot_Arm::Robot_Arm(/* args */)
{
    
}

Robot_Arm::~Robot_Arm()
{
}


#endif // !ROBOT_ARM_CLIENT_H
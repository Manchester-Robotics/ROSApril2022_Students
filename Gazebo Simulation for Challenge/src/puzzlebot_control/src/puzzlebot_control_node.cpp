#include <ros/ros.h>
#include <geometry_msgs/Twist.h>
#include <std_msgs/Float64.h>
#include <std_msgs/Float32.h>
#include <control_msgs/JointControllerState.h>
#include "puzzlebot_control/Shared.hpp"


double v,w,w_r,w_l,prev_wl,prev_wr;

void cmd_vel_callback(const geometry_msgs::Twist::ConstPtr& msg);
void wl_callback(const control_msgs::JointControllerState::ConstPtr& msg);
void wr_callback(const control_msgs::JointControllerState::ConstPtr& msg);

int main(int arc, char ** argv)
{
    ROS_INFO("[PuzzleBot] Starting control node");
    ros::init(arc,argv,"puzzlebot_control");

    v = 0;
    w = 0;
    w_r = 0;
    w_l = 0;
    prev_wl = 0;
    prev_wr = 0;


    ros::NodeHandle nh;
    ros::Time current_time,prev_time;
    current_time = ros::Time::now();
    prev_time = ros::Time::now();
    std::map<std::string,std::string> topics = FetchTopics("/puzzlebot_controller",nh);
    std::map<std::string,double> params = FetchParameters("/puzzlebot_controller",nh);
   
    ros::Publisher pub_wl_command = nh.advertise<std_msgs::Float64>(topics["cmd_wL"],100);
    ros::Publisher pub_wr_command = nh.advertise<std_msgs::Float64>(topics["cmd_wR"],100);

    ros::Publisher pub_wl = nh.advertise<std_msgs::Float32>(topics["pub_wl"],100);
    ros::Publisher pub_wr = nh.advertise<std_msgs::Float32>(topics["pub_wr"],100);

    ros::Subscriber sub_wr = nh.subscribe(topics["sub_wr"],10,wr_callback);
    ros::Subscriber sub_wl = nh.subscribe(topics["sub_wl"],10,wl_callback);

    ros::Subscriber sub_cmd_vel = nh.subscribe(topics["cmd_vel"],10,cmd_vel_callback);
    int i = 0;
    ros::Rate loop_rate (100);
    double accel_max = params["acc_max"];
    double v_max = params["vel_max"];
    double L = params["L"];
    double R = params["R"];
    while(ros::ok()){

        ros::spinOnce();

        current_time = ros::Time::now();
        double dt = (current_time - prev_time).toSec();
        prev_time = current_time;

        double wr = (v - w * L / 2.0) / R; //inverted to match the behaivour of the real robot
        double wl = (v +  w * L / 2.0) / R;

        if(wr > v_max) wr = v_max;
        else if (wr < -v_max) wr = -v_max;

        if(wl > v_max) wl = v_max;
        else if (wl < -v_max) wl = -v_max;
        
        if((wl - prev_wl)/dt > accel_max) wl = prev_wl + accel_max;
        else if((wl - prev_wl)/dt < -accel_max) wl = prev_wl - accel_max;

        if((wr - prev_wr)/dt > accel_max) wr= prev_wr + accel_max;
        else if((wr - prev_wr)/dt < -accel_max) wr = prev_wr - accel_max;

        prev_wl = wl;
        prev_wr = wr;

        std_msgs::Float64 msgR,msgL;
        msgR.data = wr;
        msgL.data = wl;

        pub_wl_command.publish(msgR);
        pub_wr_command.publish(msgL);

        std_msgs::Float32 msg_wr,msg_wl;
        msg_wr.data = w_r;
        msg_wl.data = w_l;

        pub_wl.publish(msg_wl);
        pub_wr.publish(msg_wr);

        loop_rate.sleep();
    }
}

void cmd_vel_callback(const geometry_msgs::Twist::ConstPtr& msg){
    v = msg->linear.x;
    w = msg->angular.z;
}

void wl_callback(const control_msgs::JointControllerState::ConstPtr& msg){
    w_l = msg->process_value;
}

void wr_callback(const control_msgs::JointControllerState::ConstPtr& msg){
    w_r = msg->process_value;
}
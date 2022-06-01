#ifndef SHARED_HPP
#define SHARED_HPP

#include <math.h>
#include <ros/ros.h>


int sign(double x)
{
	if (x>0)
		return 1;
	else if (x<0)
		return -1;
	else
		return 0;
}
std::map<std::string,std::string> FetchTopics(std::string header,ros::NodeHandle& nh)
{
	std::map<std::string,std::string> topics;
	nh.getParam(header+"/topics/",topics);
	return topics;
}
    
std::map<std::string,double> FetchParameters(std::string header,ros::NodeHandle& nh){
	std::map<std::string,double> params;
	nh.getParam(header+"/parameters/",params);
	return params;
}

bool CheckTopics(std::map<std::string,std::string> topics,std::vector<std::string> required_topics){
	for(int i = 0; i < required_topics.size();i++){
        if(topics.count(required_topics[i]) < 1){
            ROS_ERROR("Missing topic: %s",required_topics[i].c_str());
			return false;
        }
    }
	return true;
}

bool CheckParameters(std::map<std::string,double> params,std::vector<std::string> required_params){
	for(int i = 0; i < required_params.size();i++){
        if(params.count(required_params[i]) < 1){
            ROS_ERROR("Missing parameter: %s",required_params[i].c_str());
			return false;
        }
    }
	return true;
}

std::map<std::string,std::string> InsertPrefix(std::map<std::string,std::string> topics, std::string prefix){
	std::map<std::string,std::string>::iterator i;
	for(i = topics.begin(); i != topics.end(); i++){
		i->second = prefix + i->second;
	}
	return topics;
}

double WrapToPi(double Ang){
    double result = std::fmod((Ang + M_PI),(2.0 * M_PI));
	if (result < 0)
		result += 2 * M_PI;
	
	return result - M_PI;
}



#endif
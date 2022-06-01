
# Gazebo Simulation for Challenge
This package contains the gazebo files to run the robot model and the track for the Manchester Robotics - Tec Challenge 2022 for Robotica inteligente lecture.
 
## Installation

Download the included folders and  add the folder in your usual catkin worspace, or create a new catkin workspace with folders. Up to you.  

If you have already the folders in your catkin workspace Merge the folder, and replace the duplicated files.  

## Usage

The parameters as they are once you run it should be good enough for you to work. To test it run following comand. 

 `roslaunch puzzlebot_world puzzlebot_tec_challenge.launch` 

You are going to see the following gazebo screen

The following topics are going to be available for you to start working with the challenge. 


- ### If you need to modify the camera settings

There are included in the files two cameras, the standard regular, and a wide angle one. After testing the regular should be enough but if you 
want to optimise the camera performance are welcome to get into the file, comment the standard camera code, and uncomment the wide angle. 
The path file to this setting is: 
> puzzlebot_gazebo/urdf/puzzlebot.gazebo

For parameters , please refer to the references included.  

- ### How am I supposed to switch the traffic lights on and off. 
 Good question.  
 Life sometimes is more complicated that we believe, you know?... Sometimes things dont go the way we want to...
and the short anwser is manually, the plugin is behaving oddly  so 

- ### If you need more signs or I want to change them.
You can just drag them around with the linear 
 



## Quick Troubleshooting
- #### Gazebo is not closing properly?
- #### Gazebo is not opening after quiting program?
- #### 


You can also raise a Git Issue if you have question, issues or doubts. 

## Extra references
Camera plugin  parameters - https://classic.gazebosim.org/tutorials?tut=ros_gzplugins
Wide angle plugin paramters - https://classic.gazebosim.org/tutorials?tut=wide_angle_camera&cat=
 
### Good luck and may the odds ever be in your favor!!!


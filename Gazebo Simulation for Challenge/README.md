
# Gazebo Simulation for Challenge
This package contains the gazebo simulation files to run the robot model and the track for the Manchester Robotics - Tec Challenge 2022 for the Robotica inteligente lecture.
 
## Installation

Download the included folders and merge the folder `src`  in your usual catkin workspace (usually `~/catkin_ws/src`) , or create a new catkin workspace with the folders. Up to you.  

If you have already the folders in your catkin workspace Merge the folder, and replace the duplicated files.  

## Usage

The parameters as they are should be good enough for you to start working. To test it, run following command: 

 `roslaunch puzzlebot_world puzzlebot_tec_challenge_update.launch` 

The robot topics should be exactly the same, except for the camera. 

The puzzlebot will have the topic `/video_source/raw` , and the simulation will create a topic called  `/camera/image_raw` 

My suggestion is to create a ROS Node file for the simulation only, and have another one for the real robot, as you will have to tune both.  

- ### If you need to modify the camera settings (OPTIONAL).

There are included in the files two cameras, the standard regular, and a wide-angle one. After testing, the regular should be enough but if you 
want to optimise the camera performance, you are welcome. To change camera settings, get into the file:

> puzzlebot_gazebo/urdf/puzzlebot.gazebo

The wide-angle camera is commented. Just uncomment the plugin code you prefer to use, and comment the other camera. This is done with the comment tags:

`<!-- camera plugin code inside -->`

For parameters , please refer to the references included.  

- ### How am I supposed to switch the traffic lights on and off? 

You don't have to. Download the lastest version and lights (green and red) should be automatically working in both traffics lights.  The lights will change every 20 seconds. 

- ### If you need more signs or I want to change them.
You can just drag them around with the "Translate mode" which let you move linearly the object. Check the "Gazebo GUI Reference" if you need help finding these options.   

You can also spawn new signals, clicking in the "Insert" tab and the list of objects available in the world will be shown. 

If you hit a signal or delete it by accident, you can just launch the simulation again, and everything will be back in place. 

## Quick Troubleshooting
- #### Gazebo is not closing properly?
  If you closed the gazebo window, and terminal is still hanging. Use ` Ctl + C`  to kill the process. 
  
- #### Gazebo is not opening after quiting program?
  If the launcher does not display the interface, or the interface shuts down by itself during launching, the gazebo server and client process may be still stuck. Kill both with the following commands. 
  
  `killall gzserver` 
  `killall gzclient` 

- #### I have a different problem.

You can also raise a Git Issue if you have question, issues or doubts. 

## Extra references
- Gazebo GUI - https://classic.gazebosim.org/tutorials?cat=guided_b&tut=guided_b2
- Camera plugin  parameters - https://classic.gazebosim.org/tutorials?tut=ros_gzplugins
- Wide angle plugin paramters - https://classic.gazebosim.org/tutorials?tut=wide_angle_camera&cat=
 
### Good luck and may the odds ever be in your favor!!!


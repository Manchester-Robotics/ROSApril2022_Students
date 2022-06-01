
# Gazebo Simulation for Challenge
This package contains the gazebo simulation files to run the robot model and the track for the Manchester Robotics - Tec Challenge 2022 for the Robotica inteligente lecture.
 
## Installation

Download the included folders and merge the folder `src`  in your usual catkin workspace (usually `~/catkin_ws/src`) , or create a new catkin workspace with the folders. Up to you.  

If you have already the folders in your catkin workspace Merge the folder, and replace the duplicated files.  

## Usage

The parameters as they are should be good enough for you to start working. To test it, run following command: 

 `roslaunch puzzlebot_world puzzlebot_tec_challenge.launch` 

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

Short anwser is manually. The plugin is behaving oddly. We are working on fixing it, but for now you can modify the color manually. You need to run the simulation after every change. We will keep you post it about the plugin. 

To change the parameter you need to access the SDF file, very similar to the URDF files we tackled in class. In the simulation you have two diffent traffic lights: Traffic_Light, and Traffic_Light2.

There is a folder for each one (with the corresponding name) in the following path:

> puzzlebot_world/models/

Inside each folder, you will find a file called "model.sdf". As we learned in class this will have one base for the trafic light, and each light as a link. 

Here is the example code for a green light. 

> <link name='green_light'>
  <!--visual for green light-->  
      <visual name='visual'>
      <pose frame=''>0 -0.014 0.098 0 0 0</pose>
       <!--<pose frame=''>0 0 0 0 -0 0</pose>-->
        <geometry>
          <box>
            <size>0.02 0.001 0.02</size>
          </box>
        </geometry>    
        <material>
          <script>
            <uri>file://media/materials/scripts/gazebo.material</uri>
           <!-- EDIT ME FOR CHANGING COLOR--> 
           <name>Gazebo/Green</name>
          </script>
        </material>
      </visual>
      <!--collision for green light 
      <collision name='collision'>
        <pose frame=''>0 0 0 0 -0 0</pose>
        <geometry>
          <box>
            <size>0.02 0.001 0.02</size>
          </box>
        </geometry>
      </collision>-->  
      <!--inertial for green light-->
      <inertial>
        <pose frame=''>0 0 0 0 -0 0</pose>
        <mass>0.001</mass>
        <inertia>
          <ixx>0.166667</ixx>
          <ixy>0</ixy>
          <ixz>0</ixz>
          <iyy>0.166667</iyy>
          <iyz>0</iyz>
          <izz>0.166667</izz>
        </inertia>
      </inertial>
    </link>
    
You need then to change color in the line `<name>Gazebo/Green</name>`. Red, Yellow, Orange, Green, and Gray for off are the color useful for you. 

Save the file, and you are ready to relaunch the simulation. No need to recompile catkin.  

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


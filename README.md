# RT_final_assignment

## Exercise requirements
The assignment requires to develop a software architecture to control a mobile robot inside a simulation environment in ROS. In particular, both the modules that simulate the robot and the ones used for localization, mapping and path planning are already available. Therefore, it is asked to implement the user interface that interacts with the robot controller in order to allow the user to switch between one of the following driving modes:
 1) _Authonomous drive_: makes the robot reach autonomously a position (x, y) in the map;
 2) _Manual drive_: makes the user directly drive the robot by using the keyboard;
 3) _Assisted drive_: makes the user directly drive the robot by using the keyboard while a collision system is running in the background to avoid crashes;

## Installing and runnning
The simulation requires to install [ROS Noetic](http://wiki.ros.org/noetic/Installation), in particular the ``ros-noetic-desktop-full`` integration is raccomended so that all the necessary packages to use Gazebo and Rviz are already available. Moreover, you will require the ``slam_gmapping`` package that you can install with the command:
``
sudo apt install ros-noetic-slam-gmapping
``
Once that you've done that, you have to include the package published in this repository in the src folder of your ROS workspace and build it again. 
Then, provided that you have firstly run the master node with `roscore`, you can start the simulation environment with the following command:

``
$ rosrun stage_ros stageros$(rospack find second_assignment)/world/my_world.world
``

Finally, to see the robot moving inside the circuit and interact with it, you can run the controller and ui nodes by using the following commands:

``
$ rosrun second_assignment controller_node
``

``
$ rosrun second_assignment ui_node

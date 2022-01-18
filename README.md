# RT_final_assignment

## Exercise requirements
The assignment requires to develop a software architecture to control a mobile robot inside a simulation environment in ROS. In particular, both the modules that simulate the robot and the ones used for localization, mapping and path planning are already available. Therefore, it is asked to implement the user interface that interacts with the robot controller in order to allow the user to switch between one of the following driving modes:
 1) _Authonomous drive_: makes the robot reach autonomously a position (x, y) in the map;
 2) _Manual drive_: makes the user directly drive the robot by using the keyboard;
 3) _Assisted drive_: makes the user directly drive the robot by using the keyboard while a collision system is running in the background to avoid crashes;

## Installing and runnning
The simulation requires to install [ROS Noetic](http://wiki.ros.org/noetic/Installation), in particular the _ros-noetic-desktop-full_ integration is raccomended so that all the necessary packages to use Gazebo and Rviz are already available. Moreover, you will require the [slam_gmapping](https://github.com/CarmineD8/slam_gmapping) package.

Once that you've everything ready, you have to include the package published in this repository in the src folder of your ROS workspace and build it again. 
Then, provided that you have firstly run the master node with `roscore`, you can start the simulation with the following command:

``
$ roslaunch final_assignment.launch
``

The command launches both the files _simulation_gmapping_ and _move_base_, plus the nodes _teleop_twist_keyboard_, _user_interface_ and _collision_avoidance_. In particular, the latter two are the ones which have been specifically developed for the assignment.

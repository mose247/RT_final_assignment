# RT_final_assignment


## Exercise requirements
The assignment requires to develop a software architecture to control a mobile robot inside a simulation environment in ROS. In particular, both the modules that simulate the robot and the ones used for localization, mapping and path planning are already available. Therefore, it is asked to implement just the user interface that interacts with the robot controller in order to allow the user to switch between one of the following driving modes:
 1) **_Authonomous drive_**: makes the robot reach autonomously a position (x, y) in the map;
 2) **_Manual drive_**: makes the user directly drive the robot by using the keyboard;
 3) **_Assisted drive_**: makes the user directly drive the robot by using the keyboard while a collision system is running in the background to avoid crashes;


## Installing and runnning
The simulation requires to install [ROS Noetic](http://wiki.ros.org/noetic/Installation), in particular the _ros-noetic-desktop-full_ integration is raccomended so that all the necessary packages to use Gazebo and Rviz are already available. Moreover, you will require the [slam_gmapping](https://github.com/CarmineD8/slam_gmapping) package.

Once that you've everything ready, you have to include the package published in this repository in the src folder of your ROS workspace and build it again. 
Then, provided that you have firstly run the master node with `roscore`, you can start the simulation with the following command:

``
$ roslaunch final_assignment.launch
``

The command launches both the files **_simulation_gmapping_** and **_move_base_**, plus the nodes **_teleop_**, **_user_interface_** and **_collision_avoidance_**. In particular, the latter two are the ones that have been specifically developed for the assignment.


## Software architecture
The architecture of the user interface that was required is highlighted in the following image.

![Assignment_3-11](https://user-images.githubusercontent.com/91455159/149918889-30514938-7aa4-4f80-b46e-69c1e1144db9.jpg)

The idea that lays behind it is that the nodes **_move_base_**, **_teleop_** and **_collision_avoidance_**, that are responsable of setting the robot's velocity, do not publish it directly on the **_/cmd_vel_** topic, which is the one used to move the robot in the simulated environment. Instead, the following intermediate topics have been defined:
 - **_/automatic/cmd_vel_**: on which the node **_move_base_** publishes the velocity computed authomatically to reach an arbitrary point in the map;
 - **_/manual/cmd_vel_**: on which the node **_teleop_** publishes the velocity resulting from the user's input;
 - **_/assisted/cmd_vel_**: on which the node **_collision_avoidance_** publishes the velocity resulting from the user's input, properly updated to avoid collisions (if necessary);

Then, the **_user_interface_** node, that is subscribed to each of topics above, is in charcge of deciding which velocity to publish on **_/cmd_vel_** according to the driving mode selected by the user.


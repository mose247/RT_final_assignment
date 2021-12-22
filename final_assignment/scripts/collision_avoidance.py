#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

# global variables
pub= None               # publisher to /cmd_vel topic
astd_vel= Twist()       # velocity message where to save the updated velocity

# Callbacks
def scan_callback(msg):
    regions = {
        'right':  min(min(msg.ranges[0:143]), 10),
        'fright': min(min(msg.ranges[144:287]), 10),
        'front':  min(min(msg.ranges[288:431]), 10),
        'fleft':  min(min(msg.ranges[432:575]), 10),
        'left':   min(min(msg.ranges[576:719]), 10),
    }

    avoid_collision(regions)

def astd_vel_callback(msg):
    global astd_vel
    astd_vel= msg

# Utility functions
def avoid_collision(regions):
    global astd_vel
    # save the current linear and angular velocities obtained as the result of the
    # user's keyboard input
    linear_x= astd_vel.linear.x
    angular_z= astd_vel.angular.z

    state_description = ''

    # update the linear and angular velocities in order to avoid collisions
    if regions['front'] > 0.7 and regions['fleft'] > 0.7 and regions['fright'] > 0.7:
        state_description = 'case 1 - no obstacle detected'

    elif regions['front'] < 0.7 and regions['fleft'] > 0.7 and regions['fright'] > 0.7:
        state_description = 'case 2 - obstacle in the front'
        # don't go straight
        if (linear_x > 0) and (angular_z == 0):
            linear_x= 0
            angular_z= 0

    elif regions['front'] > 0.7 and regions['fleft'] > 0.7 and regions['fright'] < 0.7:
        state_description = 'case 3 -  obstacle in the fright'
        # don't turn fright
        if (linear_x > 0) and (angular_z < 0):
            linear_x= 0
            angular_z= 0

    elif regions['front'] > 0.7 and regions['fleft'] < 0.7 and regions['fright'] > 0.7:
        state_description = 'case 4 -  obstacle in the fleft'
        # don't turn fleft
        if (linear_x > 0) and (angular_z > 0):
            linear_x= 0
            angular_z= 0

    elif regions['front'] < 0.7 and regions['fleft'] > 0.7 and regions['fright'] < 0.7:
        state_description = 'case 5 - obstacle in the front and fright'
        # don't go straight or turn fright
        if (linear_x > 0) and (angular_z <= 0):
            linear_x= 0
            angular_z= 0

    elif regions['front'] < 0.7 and regions['fleft'] < 0.7 and regions['fright'] > 0.7:
        state_description = 'case 6 -  obstacle in the front and fleft'
        # don't go straight or turn fleft
        if (linear_x > 0) and (angular_z >= 0):
            linear_x= 0
            angular_z= 0

    elif regions['front'] < 0.7 and regions['fleft'] < 0.7 and regions['fright'] < 0.7:
        state_description = 'case 7 -  obstacle in the front and fleft and fright'
        # don't go straight, turn fright or fleft
        if (linear_x > 0):
            linear_x= 0
            angular_z= 0

    elif regions['front'] > 0.7 and regions['fleft'] < 0.7 and regions['fright'] < 0.7:
        state_description = 'case 8 -  obstacle in the fleft and fright'
        # don't turn fright or fleft
        if (linear_x > 0) and (angular_z != 0):
            linear_x= 0
            angular_z= 0

    else:
        state_description = 'unknown case'
        rospy.loginfo(regions)

    # update the  linear and angular velocities
    astd_vel.linear.x= linear_x
    astd_vel.angular.z= angular_z

    # display the obstacle's state
    rospy.loginfo(state_description)
    # publish the modified velocity on /assisted/cmd_vel
    pub.publish(astd_vel)



def main():
    # initialize the node
    rospy.init_node('drive_assistant')

    # define a publisher to the /assisted/cmd_vel topic
    global pub
    pub= rospy.Publisher('/assisted/cmd_vel', Twist, queue_size= 1)

    # define a subscriber to the /scan topic
    sub1= rospy.Subscriber('/scan', LaserScan, scan_callback)

    # define a subscriber to the /manual/cmd_vel topic
    sub2= rospy.Subscriber('/manual/cmd_vel', Twist, astd_vel_callback)

    # prevent the node from exiting
    rospy.spin()



if __name__ == '__main__':
    main()

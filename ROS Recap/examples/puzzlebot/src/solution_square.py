#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32
from geometry_msgs.msg import Twist
from math import pi


class square:
    def __init__(self):
        #initialise wheel velocity variables
        self.wr = 0.0
        self.wl = 0.0

        #Setup ROS subscribers and publishers
        rospy.Subscriber('/wr',Float32,self.wr_callback)
        rospy.Subscriber('/wl',Float32,self.wl_callback)

        self.w_pub = rospy.Publisher('/cmd_vel',Twist,queue_size=10)

        #setup node
        rospy.init_node("Square")
        self.rate = rospy.Rate(10)

        rospy.on_shutdown(self.stop)

    # Callbacks for wheel velocities and commands
    def wr_callback(self,msg):
        self.wr = msg.data

    def wl_callback(self,msg):
        self.wl = msg.data

    # Main function
    def run(self):
        #Variable initialisations
        distance = 0.0
        angle = 0.0
        current_time = rospy.get_time()
        last_time = rospy.get_time()
        state = 0
        count = 1
        no_sides = 4

        # Create message for publishing
        msg = Twist()
        msg.linear.x = 0
        msg.linear.y = 0
        msg.linear.z = 0
        msg.angular.x = 0
        msg.angular.y = 0
        msg.angular.z = 0

        # Main Loop
        while not rospy.is_shutdown():
            # Compute time since last loop
            current_time = rospy.get_time()
            dt = current_time - last_time
            last_time = current_time
            # Update distance and angle from the velocity measurements
            distance += 0.05 * (self.wr + self.wl) * 0.5 * dt
            angle += 0.05 * (self.wr - self.wl) / 0.18 * dt
            self.wr = 0
            self.wl = 0
            # state 0 = moving along a straight
            if state == 0:
                msg.linear.x = 0.2
                msg.angular.z = 0.0
                # If at end of a side
                if distance > 0.5:
                    #Reset distance
                    distance = 0.0
                    # If we have not finished the square
                    if count < no_sides:
                        # go to corner and count how many sides are done
                        state = 1
                        count += 1
                    # otherwise we have finished a square
                    else:
                        #stop
                        state = 2
            # State 1 = Turning a corner
            elif state == 1:
                msg.linear.x = 0.0
                msg.angular.z = 1.0
                # If finished turning through 90 degrees
                if angle > pi/2:
                    # Go back to moving straight
                    angle = 0.0
                    state = 0
            # State 3 = Motion completed
            elif state == 2:
                # Stop and signal
                msg.linear.x = 0
                msg.angular.z = 0
                print("Motion Completed")
                rospy.signal_shutdown("Square Completed")
            # If invalid state, stop
            else:
                msg.linear.x = 0
                msg.angular.z = 0

            # Publish message and sleep
            self.w_pub.publish(msg)

            self.rate.sleep()
            
    # Separate stop function for stopping when ROS shuts down
    def stop(self):
        print("Stopping")
        msg = Twist()
        msg.linear.x = 0
        msg.linear.y = 0
        msg.linear.z = 0
        msg.angular.x = 0
        msg.angular.y = 0
        msg.angular.z = 0
        self.w_pub.publish(msg)

if __name__ == "__main__":
    sq = square()

    try:
        sq.run()
    except rospy.ROSInterruptException:
        None

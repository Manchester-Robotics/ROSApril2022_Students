#!/usr/bin/env python
# Library that contains the basic files for ros to work
import rospy
# Library that contains standard ROS msgs
from std_msgs.msg import String

def talker():

    # Publisher object used to forward msgs to the network, it has a max buffer of 10 msgs to prevent lose of data
    pub = rospy.Publisher('chatter', String, queue_size=10)
    # Node initialisation into the system
    rospy.init_node('talker',anonymous=True)
    rate = rospy.Rate(10) # Rate at which ros will work, in this case 10hz
    # Main loop that will be executed at a freq. of 10Hz
    while not rospy.is_shutdown():

        # Piece of code used to send a string to both a topic and the terminal using ros logging services
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        # Wait to match the 10Hz rate
        rate.sleep()

if __name__ == '__main__':
    # Try catch exception handling. If we interrupt the execution of the code using crtl C the code in the except
    # statement will be executed
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

#!/usr/bin/env python3
# https://cyaninfinite.com/ros-cv-bridge-with-python-3/

import rospy, cv2
from sign_rec.srv import check, data
from sensor_msgs.msg import Image
import os, rospkg, random
import cv2
from cv_bridge import CvBridge

class SendSample():

    # Check if the prediction is correct
    def check_callback(self,req):

        self.pub_flag = True

        if req.preditction == int(self.type):
            return "Correct"
        else:
            return "Incorrect"

    # Pick an image at random from a folder at random within the data folder
    def data_callback(self,req):

        self.type = random.choice(self.list_dir)
        image_dir = os.listdir(os.path.join(self.data_path, self.type))
        img = cv2.imread(os.path.join(self.data_path, self.type, random.choice(image_dir)))
        image_message = self.bridge.cv2_to_imgmsg(img, encoding="passthrough")
        return image_message

    # Initialise publisher
    def __init__(self):
        rospy.init_node("get_samples")
        rate = rospy.Rate(1)
        self.image_queue = []

        rp = rospkg.RosPack()
        self.data_path = os.path.join(rp.get_path("sign_rec"), "src", "data")
        self.list_dir = os.listdir(self.data_path)
        s_check = rospy.Service('check_results', check, self.check_callback)
        s_data = rospy.Service('send_data', data, self.data_callback)
        self.bridge = CvBridge()
        rospy.spin()

if __name__ == "__main__":
    SendSample()

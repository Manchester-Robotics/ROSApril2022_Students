#!/usr/bin/env python3

import rospy, cv2
import numpy as np
from tensorflow.keras.models import load_model
import os, rospkg
from sign_rec.srv import check, data

# Constant definition
frameWidth = 640  # CAMERA RESOLUTION
frameHeight = 480
brightness = 180

class DetectStop():

    def format_image(self,data):
        aux_img = self.imgmsg_to_cv2(data)
        aux_img = cv2.resize(aux_img, (frameWidth, frameHeight))
        return aux_img

    def imgmsg_to_cv2(self,msg):
        return np.frombuffer(msg.data, dtype=np.uint8).reshape(msg.height, msg.width, -1)

    def grayscale(self,img):
        # Grayscale the image

        return img

    def equalize(self,img):
        # Equalize the histogram

        return img

    def preprocessing(self,img):
        # TODO: Write grayscale and equalize functions using cv2
        img = cv2.resize(img, (32, 32))
        img = self.grayscale(img)
        img = self.equalize(img)
        img = img / 255
        # the image needs to be reshaped to be used as an input tensor for tensorflow
        return img.reshape(1, 32, 32, 1)

    def __init__(self):
        rospy.init_node("tf_process")
        rate = rospy.Rate(1)
        self.image_queue = []

        rp = rospkg.RosPack()
        script_path = os.path.join(rp.get_path("sign_rec"), "src", "saved_model","my_model")
        get_data = rospy.ServiceProxy('send_data', data)
        check_results = rospy.ServiceProxy('check_results', check)
        # Use tensorflow to load the model

        # TODO: Call "Send data" to ask for an image and "check_results" to verify your prediction


        while not rospy.is_shutdown():

            raw_img = get_data()
            img = self.format_image(raw_img.img)
            img_prerp = self.preprocessing(img)

            # TODO:Use the model to make a prediction and check the results

            probabilityValue = np.amax(predictions)
            if probabilityValue > threshold:
		        # TODO: Call "check_results" to verify your prediction. A service is called by passing its request arguments to the service
                print(classIndex)
            else:
                print('Not found')

            rate.sleep()

if __name__ == "__main__":
    DetectStop()

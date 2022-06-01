#!/usr/bin/env python
import rospy
import tf2_ros
import numpy as np
from geometry_msgs.msg import PoseStamped, TransformStamped
from gazebo_msgs.msg import ModelStates


class StateGatherer():
    def __init__(self):

        self.br = tf2_ros.TransformBroadcaster()
        rospy.init_node("pose_tf")
        rospy.wait_for_service('/gazebo/set_link_state')
        rospy.Subscriber("gazebo/model_states", ModelStates, self.callback)

    def main(self):
        rospy.spin()


    def callback(self, data):

	try: 

		aux_idx = data.name.index("puzzlebot")

		t = TransformStamped()
		t.header.stamp = rospy.Time.now()
		t.header.frame_id = "world"
		t.child_frame_id = "base_link"
		t.transform.translation = data.pose[aux_idx].position
		t.transform.rotation = data.pose[aux_idx].orientation
		self.br.sendTransform(t)

	except:
		pass

if __name__ == '__main__':
    aux = StateGatherer()
    aux.main()

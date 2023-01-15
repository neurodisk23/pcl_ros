#!/usr/bin/env python
from roslib import message
import rospy
import numpy as np
import sensor_msgs.point_cloud2 as pc2
from sensor_msgs.msg import PointCloud2, PointField
import ros_numpy

#listener
def listen():
    rospy.init_node('listen', anonymous=True)
    rospy.Subscriber("/velodyne_points", PointCloud2, callback_kinect)
    rospy.spin()

def callback_kinect(data) :
    points = ros_numpy.point_cloud2.pointcloud2_to_array(data)
    points_x = points['x']
    points_y = points['y']
    points_z = points['z']
if __name__ == '__main__':
    try:
        listen()
    except rospy.ROSInterruptException:
        pass

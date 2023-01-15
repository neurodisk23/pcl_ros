#!/usr/bin/env python
from roslib import message
import rospy
import sensor_msgs.point_cloud2 as pc2
from sensor_msgs.msg import PointCloud2, PointField

#listener
def listen():
    rospy.init_node('listen', anonymous=True)
    rospy.Subscriber("/velodyne_points", PointCloud2, callback_kinect)
    rospy.spin()

def callback_kinect(data) :
    # pick a height
    height =  int (data.height)
    print("height", height)
    # pick x coords near front and center
    width = int (data.width)
    print("width", width)
    # examine point

if __name__ == '__main__':
    try:
        listen()
    except rospy.ROSInterruptException:
        pass

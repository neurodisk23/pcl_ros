# velodyne_lidar_subscriber.py

import rospy
from sensor_msgs.msg import PointCloud2
import sensor_msgs.point_cloud2 as pc2

def cloud_callback(cloud_msg):
    # Convert the incoming ROS message to a list of points
    points = list(pc2.read_points(cloud_msg, skip_nans=True, field_names=("x", "y", "z")))

    # Do processing on the point cloud here...

    rospy.loginfo("Received a Velodyne LiDAR point cloud with %d points." % len(points))

if __name__ == '__main__':
    rospy.init_node("lidar_subscriber_node")
    cloud_sub = rospy.Subscriber("/velodyne_points", PointCloud2, cloud_callback)

    rospy.spin()

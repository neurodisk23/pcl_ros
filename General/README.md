# README.md

## Velodyne LiDAR Point Cloud Subscriber

This package contains a ROS subscriber for Velodyne LiDAR point clouds. The subscriber listens to the `/velodyne_points` topic and processes incoming point clouds using the `cloud_callback` function.

The point cloud data is converted to a list of points using the `pc2.read_points` function from the `sensor_msgs.point_cloud2` module. The list of points can then be processed as desired. In this example, a simple message is printed to the log indicating the number of points in the point cloud.

## Usage

1. Clone the repository to your ROS workspace:


```
$ cd ~/catkin_ws/src
$ git clone https://github.com/<username>/velodyne_lidar_subscriber.git
```


2. Build the package:


```
$ cd ~/catkin_ws
$ catkin_make
```


3. Run the subscriber:


```
$ rosrun velodyne_lidar_subscriber velodyne_lidar_subscriber.py

```


## Notes

- The subscriber assumes that the Velodyne LiDAR point clouds are being published on the `/velodyne_points` topic. If this is not the case, you will need to modify the `cloud_sub` line in `velodyne_lidar_subscriber.py` to match the appropriate topic name.

- The processing of the point cloud in the `cloud_callback` function is left up to the user to implement. This can include filtering, clustering, visualization, or any other desired processing.

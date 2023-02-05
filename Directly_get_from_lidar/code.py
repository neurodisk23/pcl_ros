import numpy as np
import pyvelodyne

# Connect to the Velodyne LiDAR sensor
velo = pyvelodyne.Velodyne("192.168.0.10")

# Get a frame of LiDAR data
frame = velo.get_frame()

# Convert the frame to a NumPy array
points = np.frombuffer(frame, dtype=np.float32).reshape(-1, 4)

# Access the XYZ coordinates and intensity values of the LiDAR data
x = points[:, 0]
y = points[:, 1]
z = points[:, 2]
intensity = points[:, 3]

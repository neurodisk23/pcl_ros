import numpy as np
import cv2
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Read point cloud data from file
point_cloud = np.loadtxt('point_cloud_data.txt')

# Define parameters for the checkerboard pattern
board_size = (6, 9)
square_size = 0.02

# Convert the point cloud data to 2D image coordinates
img_points = np.zeros((board_size[0]*board_size[1], 2), dtype=np.float32)
for i in range(board_size[0]*board_size[1]):
    img_points[i,0] = point_cloud[i,0]/point_cloud[i,2]
    img_points[i,1] = point_cloud[i,1]/point_cloud[i,2]

# Find the corners of the checkerboard in the image
ret, corners = cv2.findChessboardCorners(img_points, board_size)

if ret:
    # Draw the corners on the image
    img = cv2.cvtColor(point_cloud, cv2.COLOR_GRAY2RGB)
    cv2.drawChessboardCorners(img, board_size, corners, ret)

    # Display the image and the 3D point cloud
    plt.subplot(121), plt.imshow(img), plt.title('Checkerboard Detection')
    ax = plt.subplot(122, projection='3d')
    ax.scatter(point_cloud[:,0], point_cloud[:,1], point_cloud[:,2])
    ax.set_title('Point Cloud Data')
    plt.show()
else:
    print("Checkerboard not found.")

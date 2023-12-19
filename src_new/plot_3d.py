import numpy as np
import matplotlib.pyplot as plt
import scipy
import matplotlib.pyplot as plt
from matplotlib.colors import LightSource
from tqdm import tqdm
import os
import open3d as o3d


object = r"Buddha_diff_intrinsic"

input_file = r"./results/images/" + object + r"/int_depth_mesh_b0.ply"

# input_file = r"./gt_pointclouds/gt_" + object + r".ply"

pcd = o3d.io.read_point_cloud(input_file) # Read the point cloud

points_3d = np.asarray(pcd.points)


fig = plt.figure()
ax = fig.add_subplot(projection='3d')
SUBSAMPLE_FACTOR = 1
ax.scatter(points_3d[::SUBSAMPLE_FACTOR, 0], 
            points_3d[::SUBSAMPLE_FACTOR, 1], 
            points_3d[::SUBSAMPLE_FACTOR, 2], 
            marker='.', s=0.5)

#dog aspect
# ax.set_box_aspect([1, 1/2, 1])

#shoe aspect
# ax.set_box_aspect([1, 1/2, 1])
plt.show()
import open3d
import numpy as np

# mesh = open3d.io.read_triangle_mesh("airplane_0630.off")
# open3d.visualization.draw_geometries([mesh])


# pcd = open3d.io.read_point_cloud("plane.pcd")
# open3d.visualization.draw_geometries([pcd])

# pcd = open3d.io.read_point_cloud("test.pcd")
# open3d.visualization.draw_geometries([pcd])

points = np.loadtxt('plane.pts').astype(np.float32)
pcd = open3d.geometry.PointCloud()
pcd.points = open3d.utility.Vector3dVector(points)
open3d.visualization.draw_geometries([pcd])
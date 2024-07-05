# import libraries
import open3d as o3d

# Load data in variables
pcd = o3d.io.read_point_cloud('sample.ply')

# Explore the dataset
print(pcd)
print(pcd.points[1])
print(pcd.points[1:10])
print(pcd.colors[0])

# Visualize the dataset
o3d.visualization.draw_geometries([pcd])
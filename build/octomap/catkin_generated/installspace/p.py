# #!/usr/bin/env python

# import rospy
# from sensor_msgs.msg import PointCloud2
# from octomap_msgs.msg import Octomap
# import octomap

# def callback(data):
#     # 将PointCloud2数据转换为Octomap数据
#     octree = octomap.OcTree(0.1)  # 设置Octomap的分辨率
#     octree.fromPointCloud2(data)
#     octomap_msg = Octomap()
#     octomap_msg.header = data.header
#     octomap_msg.binary = True
#     octomap_msg.id = 1
#     octomap_msg.resolution = octree.getResolution()
#     octomap_msg.data = octree.writeBinary()

#     pub.publish(octomap_msg)

# def listener():
#     rospy.init_node('octomap_publisher', anonymous=True)
#     rospy.Subscriber('/velodyne_points', PointCloud2, callback)
#     rospy.spin()

# if __name__ == '__main__':
#     pub = rospy.Publisher('/octomap', Octomap, queue_size=10)
#     listener()

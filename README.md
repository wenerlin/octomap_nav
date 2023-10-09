# octomap_nav
# 第一步：启动octomap_server
# source ./devel/setup.bash
# roslaunch octomap_server octomap_mapping.launch
# 第二步：启动 gazebo 模型
# source ./devel/setup.bash
# roslaunch ship_rviz_gazebo ship_gazebo.launch
# 第三步：启动 导航模块 和 rviz
# source ./devel/setup.bash
# roslaunch nav_demo nav06_test.launch
# 第四步：保存扫描出来的模型
# source ./devel/setup.bash
# rosrun octomap_server octomap_saver -f 文件名.bt
# 第五步：查看模型
# octovis 文件名.bt

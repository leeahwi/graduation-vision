# Preserved ROS 1 catkin source

This archive contains the original hg_lineDetection package and its integration fixes, not prebuilt ROS binaries. ROS 1 and the original Melodic-era Python/cv_bridge environment are required. No ROS runtime or catkin build was verified for this release.

Extract this archive, copy hg_lineDetection into ~/catkin_ws/src/, prepare ROS dependencies (rospy, roscpp, std_msgs, sensor_msgs, cv_bridge, image_transport, OpenCV, NumPy, Matplotlib) for your ROS/Python distribution, then:

```bash
cd ~/catkin_ws
catkin_make
source devel/setup.bash
roslaunch hg_lineDetection lineDetection.launch
```

A separate camera node must publish sensor_msgs/Image on /stereo/left/image_raw. Alternative launch files: lineDetectionDiff.launch and lineDetectionHough.launch. See https://github.com/leeahwi/graduation-vision#ros-차선-인식 for outputs and limitations (fixed image assumptions and Python 2/3 behavior). Existing author and license metadata are preserved in the package and PROVENANCE.md.

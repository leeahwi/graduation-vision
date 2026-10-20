cmake_minimum_required(VERSION 3.16)
project(GraduationVision VERSION 1.0.0 LANGUAGES CXX)

add_subdirectory(lane-detection)
add_subdirectory(object-detection)
# ROS 1 is built independently in a catkin workspace; see README.md.

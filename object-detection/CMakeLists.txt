cmake_minimum_required(VERSION 3.0.0)
#defines the mnimum version of CMake required

project(Live_ObjectDetection VERSION 0.1.0)

include(CTest)
enable_testing()

set(OpenCV_DIR /Users/hwiah/Documents/opencv_4/install/lib/cmake/opencv4)
find_package(OpenCV REQUIRED)

include_directories(${OpenCV_INCLUDE_DIRS})

add_executable(Live_ObjectDetection main.cpp)

target_link_libraries(Live_ObjectDetection ${OpenCV_LIBS})

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})

include(CPack)
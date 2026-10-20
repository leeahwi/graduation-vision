cmake_minimum_required(VERSION 3.16)
project(Live_ObjectDetection VERSION 0.1.0 LANGUAGES CXX)

find_package(OpenCV REQUIRED COMPONENTS core imgproc videoio highgui dnn)

add_executable(Live_ObjectDetection main.cpp)
target_compile_features(Live_ObjectDetection PRIVATE cxx_std_17)
target_include_directories(Live_ObjectDetection PRIVATE ${OpenCV_INCLUDE_DIRS})
target_link_libraries(Live_ObjectDetection PRIVATE ${OpenCV_LIBS})

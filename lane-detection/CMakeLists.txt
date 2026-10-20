cmake_minimum_required(VERSION 3.0.0)
#defines the mnimum version of CMake required

project(Live_LaneDetection VERSION 0.1.0)

set(CMAKE_CXX_STANDARE 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

include(CTest)
enable_testing()

set(OpenCV_DIR /Users/hwiah/Documents/opencv_4/install/lib/cmake/opencv4)
find_package(OpenCV REQUIRED)

include_directories(${OpenCV_INCLUDE_DIRS})

if(MSVC)
   add_compile_options(/W4)
else()
   add_compile_options(-Wall -Wextra -pedantic)
endif()
 
find_package(GSL REQUIRED)
link_libraries(GSL::gsl GSL::gslcblas)

add_executable(Live_LaneDetection main.cpp)

target_link_libraries(Live_LaneDetection ${OpenCV_LIBS})

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})

include(CPack)
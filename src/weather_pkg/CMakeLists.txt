cmake_minimum_required(VERSION 3.5)
project(weather_pkg)

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(std_msgs REQUIRED)

install(
  DIRECTORY weather_pkg
  DESTINATION lib/python3.8.10/site-packages
)

install(
  PROGRAMS weather_pkg/weather_node.py
  DESTINATION lib/weather_pkg
)

ament_package()


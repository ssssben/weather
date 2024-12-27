cmake_minimum_required(VERSION 3.5)
project(weather_pkg)

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)

install(PROGRAMS
  weather_pkg/weather_node.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()


cmake_minimum_required(VERSION 3.5)
project(weather_pkg)

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(std_msgs REQUIRED)

add_executable(weather_node src/weather_node.py)

install(PROGRAMS
  src/weather_node.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()


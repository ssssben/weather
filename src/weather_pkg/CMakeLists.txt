cmake_minimum_required(VERSION 3.5)
project(weather_pkg)

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(std_msgs REQUIRED)

install(PROGRAMS
  scripts/weather_node.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_python_install_package()

ament_add_gtest(test_weather_node
  test/test_weather_node.py
)

ament_package()


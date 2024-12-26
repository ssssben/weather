cmake_minimum_required(VERSION 3.5)
project(weather_pkg)

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(std_msgs REQUIRED)

install(PROGRAMS
  weather_pkg/weather_node.py  # 正しいディレクトリパスに変更
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()


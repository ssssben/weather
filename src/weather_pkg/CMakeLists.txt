cmake_minimum_required(VERSION 3.5)
project(weather_pkg)

# 必要なパッケージを見つける
find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(std_msgs REQUIRED)

# Python パッケージをインストールする
install(PROGRAMS
  scripts/weather_node.py
  DESTINATION lib/${PROJECT_NAME}
)

# Pythonパッケージのインストールを有効化
ament_python_install_package(${PROJECT_NAME})

ament_package()


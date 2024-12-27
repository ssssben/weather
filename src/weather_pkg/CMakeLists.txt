cmake_minimum_required(VERSION 3.5)
project(weather_pkg)

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(ament_cmake_pytest REQUIRED)  # pytest関連のパッケージを追加
install(
  DIRECTORY weather_pkg/
  DESTINATION lib/${PROJECT_NAME}
)
ament_add_pytest_test(test_weather_node
  test/test_weather_node.py
)

ament_package()


cmake_minimum_required(VERSION 3.5)
project(weather_pkg)

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)

ament_python_install_package()

ament_add_pytest_test(test_weather_node
  TEST_SOURCES
    src/weather_pkg/test/test_weather_node.py
)

ament_package()


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
find_package(pytest REQUIRED)
if(BUILD_TESTING)
  add_test(
    NAME test_weather_node
    COMMAND pytest ${CMAKE_CURRENT_SOURCE_DIR}/test/test_weather_node.py
  )
endif()

ament_package()


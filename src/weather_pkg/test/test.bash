#!/bin/bash

source /opt/ros/foxy/setup.bash

rosdep update
rosdep install --from-paths src --ignore-src -r -y

colcon build --symlink-install

python3 -m pytest src/weather_pkg/test/test_weather_node.py


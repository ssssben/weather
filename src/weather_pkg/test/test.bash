#!/bin/bash
set -e

source ~/ros2_ws/install/setup.bash

ros2 run weather_pkg weather_node &
NODE_PID=$!

python3 -m unittest discover -s ~/ros2_weather_ws/src/weather_pkg/weather_pkg/tests -p "*.py"

kill $NODE_PID


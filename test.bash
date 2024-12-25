#!/bin/bash

source /opt/ros/humble/setup.bash
source ~/ros2_ws/install/setup.bash

ros2 run weather_pkg weather_node &

sleep 10

ros2 topic echo /weather_info --once

if [ $? -ne 0 ]; then
    echo "Error: Topic /weather_info was not published successfully!"
    exit 1
fi

echo "Test passed: Weather info published successfully"


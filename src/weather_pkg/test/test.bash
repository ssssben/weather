#!/bin/bash

WORKSPACE_DIR="/root/ros2_ws"

source $WORKSPACE_DIR/install/setup.bash

export OPENWEATHERMAP_API_KEY="7c8ebb86284de8568f27c0e05f1cd4ac"

timeout 30 ros2 run weather_pkg weather_node

echo "テストが完了しました。"


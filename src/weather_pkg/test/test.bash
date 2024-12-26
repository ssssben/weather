#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws

colcon build

source $dir/ros2_ws/install/setup.bash

export OPENWEATHERMAP_API_KEY="7c8ebb86284de8568f27c0e05f1cd4ac"

timeout 30 ros2 run mypkg weather_node

echo "テストが完了しました。"


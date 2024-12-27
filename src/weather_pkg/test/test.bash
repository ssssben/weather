#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_weather_ws
colcon build
source $dir/.bashrc
timeout 30 python3 ~/ros2_weather_ws/src/weather_pkg/weather_pkg/weather_node.py > /tmp/mypkg.log

cat /tmp/mypkg.log |
grep 'Weather in Dalian'

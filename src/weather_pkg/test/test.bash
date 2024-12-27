#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_weather_ws
colcon build
source /root/.bashrc   # 絶対パスで明示的に指定
timeout 30 python3 /root/ros2_weather_ws/src/weather_pkg/weather_pkg/weather_node.py > /tmp/mypkg.log

grep 'Weather in Dalian' /tmp/mypkg.log   # catを省略


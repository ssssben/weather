#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build --symlink-install
source install/setup.bash
ros2 run weather_pkg weather_note
timeout 30 ros2 run weather_pkg weather_note > /tmp/weather_pkg.log

cat /tmp/weather_pkg.log |
grep 'Dalian'

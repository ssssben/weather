#!/bin/bash

# ROS2のセットアップ
source /opt/ros/humble/setup.bash
source ~/ros2_ws/install/setup.bash

# ノードをバックグラウンドで起動
ros2 run weather_pkg weather_node &

# ノードの起動を待機
sleep 10

# トピックの確認 (ここでは '/weather_info' トピックを確認)
ros2 topic echo /weather_info --once

# エラーチェック
if [ $? -ne 0 ]; then
    echo "Error: /weather_info topic was not published successfully!"
    exit 1
fi

echo "Test passed: Weather info published successfully"


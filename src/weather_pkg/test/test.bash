#!/bin/bash

WORKSPACE_DIR="/root/ros2_weather_ws"

# ROS 2 環境のセットアップ
source /opt/ros/foxy/setup.bash
source $WORKSPACE_DIR/install/setup.bash

# API キーの環境変数を設定
export OPENWEATHERMAP_API_KEY="7c8ebb86284de8568f27c0e05f1cd4ac"

# ノードをタイムアウト付きで実行
if timeout 30 ros2 run weather_pkg weather_node; then
    echo "テストが成功しました。"
else
    echo "テストが失敗しました。" >&2
    exit 1
fi


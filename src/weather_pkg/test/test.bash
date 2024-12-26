#!/bin/bash

# 作業ディレクトリを設定
WORKSPACE_DIR="/root/ros2_ws"

# ROS2の環境設定をロード
source $WORKSPACE_DIR/install/setup.bash

# APIキーの設定
export OPENWEATHERMAP_API_KEY="7c8ebb86284de8568f27c0e05f1cd4ac"

# weather_nodeを実行（30秒間のタイムアウトを設定）
timeout 30 ros2 run weather_pkg weather_node

echo "テストが完了しました。"


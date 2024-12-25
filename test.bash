#!/bin/bash
set -e

# Set up ROS 2
sudo apt update
sudo apt install -y software-properties-common
sudo add-apt-repository universe
sudo apt update
sudo apt install -y curl gnupg lsb-release
sudo curl -sSL http://repo.ros2.org/repos.key | sudo apt-key add -
sudo sh -c 'echo "deb [arch=amd64,arm64] http://repo.ros2.org/ubuntu/main $(lsb_release -cs) main" > /etc/apt/sources.list.d/ros2-latest.list'
sudo apt update
sudo apt install -y ros-foxy-desktop
source /opt/ros/foxy/setup.bash
sudo apt install -y python3-colcon-common-extensions
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
git clone https://github.com/ros2/examples.git
cd ~/ros2_ws/
colcon build
source install/setup.bash
echo "source /opt/ros/foxy/setup.bash" >> ~/.bashrc
echo "source ~/ros2_ws/install/setup.bash" >> ~/.bashrc
source ~/.bashrc

# Set up Python environment
python3 -m pip install --upgrade pip
python3 -m pip install rclpy
python3 -m pip install requests

# Run the weather node script
export OPENWEATHERMAP_API_KEY=$1
python3 weather_node.py

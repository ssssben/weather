#!/bin/bash

# Exit on any error
set -e

echo "Running tests..."

# Example: ROS 2 environment setup and test execution
source /opt/ros/foxy/setup.bash
colcon build
colcon test
colcon test-result --verbose

echo "All tests passed successfully."

